from backupdata.models import Channel

__author__ = 'hongleviet'
import datetime
from django.db.models import Q



from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):



    def handle(self, *args, **options):
        now = datetime.datetime.now()
        channels = Channel.objects.filter( next_crawl_time__lt = now)[:10]


        for c in channels:
            c.crawl_history()