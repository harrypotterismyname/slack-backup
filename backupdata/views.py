from backupdata.models import crawl_all_channel, Channel, Message
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext


def home(request):
    if request.user.is_authenticated():

        return HttpResponseRedirect('/team')
    variables = {}
    return render_to_response('index.html', variables, context_instance=RequestContext(request))


@login_required
def channels(request):
    channels, groups = crawl_all_channel(request.user)
    variables = {'channels': channels, 'groups': groups}
    return render_to_response('channels.html', variables, context_instance=RequestContext(request))


@login_required
def channel_detail(request, channel_id):
    channel = Channel.objects.get(id=channel_id)

    #channel.crawl_history()
    messages = Message.objects.filter(channel=channel)
    variables = {'channel': channel, 'messages': messages}
    return render_to_response('channel.html', variables, context_instance=RequestContext(request))


@login_required
def team(request):
    user = request.user

    team = user.get_team()
    members = team.parse_members()

    variables = {'members': members}
    return render_to_response('members.html', variables, context_instance=RequestContext(request))