from django.core.management.base import BaseCommand, CommandError
from scrape.models import WebScrape
from scrape.scrape import *

# This class may be instantiated via terminal command 'python manage.py savetodb'
# Loops through cleaned scraped data (class seen in scrape.py),
# and correctly appends to each corresponding column in the database.


class SaveToDB(BaseCommand):
    help = 'Saves scraped data to database'

    for x in range(len(Scrape.clean_scrape())):
        for z, y in enumerate(Scrape.clean_scrape()[x]):
            if x == 0:
                a = WebScrape(date=y, counties=[
                              x+1][z], cases=[x+2][z], deaths=[x+3][z])
                a.save()

    print("Saving today's data to the database.")
