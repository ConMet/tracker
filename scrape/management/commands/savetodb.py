from django.core.management.base import BaseCommand, CommandError
from scrape.models import WebScrape
from scrape.scrape import *

# This class may be instantiated via terminal command 'python manage.py savetodb'
# Loops through cleaned scraped data (class seen in scrape.py),
# and correctly appends to each corresponding column in the database.


class Command(BaseCommand):
    help = 'Saves scraped data to database'

    def handle(self, *args, **options):
        for i in Scrape.clean_scrape():
            a = WebScrape(date=i[0], counties=i[1],
                          cases=i[2], deaths=i[3])
            a.save()

        self.stdout.write("Saving today's data to the database.", ending=" ")
