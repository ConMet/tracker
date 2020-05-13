from scrape.models import WebScrape
from scrape.scrape import *

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
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


#global job_frame

# Registers the 'pulldata' job. This creates a schedule for pulling all data from the WebScrape
# table in the database and returns a Pandas data frame of that data. The job itself is stored
# in its own table in the database.
@register_job(scheduler, 'cron', hour=1, minute=49, misfire_grace_time=None, max_instances=1)
def pulldata():
    df = pd.DataFrame(list(WebScrape.objects.all().values()))
    df[['cases', 'deaths']] = df[['cases', 'deaths']].apply(pd.to_numeric)
    register_events(scheduler)
    sns.set(style="darkgrid")
    sns.lineplot(x='date', y='cases', data=df)
    plt.title('Test Plot')
    plt.show()
    return df


print('Scrape scheduler running...')
print('Current data pulled from database...')
