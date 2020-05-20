from scrape.models import WebScrape
from scrape.scrape import *

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from datetime import date, datetime
import time

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
    # Monitoring per-execution
    register_events(scheduler)
    scheduler.start()


print('Scrape scheduler running...')
print('Current data pulled from database...')
