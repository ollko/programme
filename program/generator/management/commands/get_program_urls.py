from datetime import datetime
import requests
import xml.etree.ElementTree as ET

from django.core.management.base import BaseCommand, CommandError

from generator.models import Record
from generator.utils import remove_symbols, convert_to_time


class Command(BaseCommand):
    help = "Get latest program data from api"

    def handle(self, *args, **options):
        sess = requests.Session()
        url = "https://xmltv.s-tv.ru/xchenel.php"
        payloads = {
            'login':'tv9280',
            'pass': 'TrhB4vlGBC',
            'show':'2',
            'xmltv': '1'
        }
        r = sess.get(url, params=payloads)
        xml = remove_symbols(r.content.decode('windows-1251'))

        root = ET.fromstring(xml)
        files = root.findall("File")
        for file in files:
            name = file.find('Name').text
            efirweek = file.find('EfirWeek').text
            channel = file.find('Channel').text
            channelid = file.find('ChannelID').text
            updated = convert_to_time(file.find('DateTime').text)
            variant = file.find('Variant').text
            r = Record(
                    name=name,
                    efirweek=efirweek,
                    channel=channel,
                    channelid=channelid,
                    updated=updated,
                    variant=variant
            )
            try:
                r.save()
            except Exception as e:
                print(e)
