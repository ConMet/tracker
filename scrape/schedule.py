from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from datetime import date
from scrape.models import WebScrape
from scrape.scrape import *
import pandas as pd

# Defining the function to be scheduled, use DjangoJobStore
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')

# Registers the 'dataschedule' job. This creates a schedule for webscraping and storing that
# data on a daily basis. The job itself is stored in its own table in the database.
@register_job(scheduler, 'cron', hour=15, minute=30, misfire_grace_time=None, max_instances=1)
def dataschedule():
    for i in Scrape.clean_scrape():
        a = WebScrape(date=i[0], counties=i[1], cases=i[2], deaths=i[3])
        a.save()
    print(date.today())
    # Monitoring per-execution
    register_events(scheduler)
    scheduler.start()

# Registers the 'pulldata' job. This creates a schedule for pulling all data from the WebScrape
# table in the database and returns a Pandas data frame of that data. The job itself is stored
# in its own table in the database.
@register_job(scheduler, 'cron', hour=12, minute=24, misfire_grace_time=None, max_instances=1)
def pulldata():
    df = pd.DataFrame(list(WebScrape.objects.all().values()))
    return df


print('Scrape scheduler running...')
print('Current data pulled from database...')
