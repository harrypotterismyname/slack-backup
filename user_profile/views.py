import json
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from lib.utils import random_string
import requests
from slackbackup import settings
from user_profile.models import User


def slack_oauth_login(request):
    state = random_string(10)

    request.session['state'] = state

    url = 'https://slack.com/oauth/authorize?client_id=' + settings.SLACK_CLIENT_ID + "&state=" + state \
          + "&scope=read&redirect_uri=" + settings.DOMAIN + "/slack-oauth/callback"
    return HttpResponseRedirect(url)


def logout_view(request):
    if request.user.is_authenticated():
        logout(request.user)
    return HttpResponseRedirect("/")


def slack_oauth_callback(request):
    client_id = settings.SLACK_CLIENT_ID
    client_secret = settings.SLACK_CLIENT_SECRET
    code = request.GET.get('code', '')
    state = request.GET.get('state', '')
    if code == '':
        return  HttpResponse('Error: No code.')
    if  request.session.get('state','') != state:
        return  HttpResponse('Error: Wrong state.')

    redirect_uri = settings.DOMAIN + "/slack-oauth/callback"

    url = 'https://slack.com/api/oauth.access?client_id=' + client_id + "&client_secret=" \
          + client_secret + "&code=" + code + "&redirect_uri=" + redirect_uri

    r = requests.get(url)

    access_token = json.loads(r.content).get('access_token','')
    if access_token =='':
        return  HttpResponse('Error: No access token is issued.')

    print 'access_token: ' + access_token



    #check token
    auth_url = "https://slack.com/api/auth.test?token=" + access_token
    r = requests.get(auth_url)
    print r.content
    slack_id = json.loads(r.content)['user_id']
    slack_team_id = json.loads(r.content)['team_id']

    user_url =  "https://slack.com/api/users.info?token=" + access_token + "&user=" + slack_id
    r = requests.get(user_url)
    user_object = json.loads(r.content)
    email = user_object['user']['profile']['email']

    user, created = User.objects.get_or_create( slack_id = slack_id, username = email , email = email )
    if created:
        user.first_name = user_object['user']['profile'].get('first_name','')
        user.last_name =  user_object['user']['profile'].get('last_name','')
        user.slack_team_id =  slack_team_id
        user.slack_username =  user_object['user']['name']
        user.slack_avatar =  user_object['user']['profile'].get('image_24','')

    user.slack_access_token = access_token
    user.save()

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)


    return HttpResponseRedirect('/team')