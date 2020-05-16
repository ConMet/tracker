from scrape.models import WebScrape
from scrape.scrape import *

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
'''import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns'''
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


# Registers the 'pulldata' job. This creates a schedule for pulling all data from the WebScrape
# table in the database and returns a Pandas data frame of that data. The job itself is stored
# in its own table in the database.

# *** Decided this shouldn't be a scheduled task, but rather something that the user initiates via
# a database query from the front-end. Making this a scheduled task muddles things and isn't optimal ***
'''@register_job(scheduler, 'cron', hour=14, minute=45, misfire_grace_time=None, max_instances=1)
def pulldata():

    # Instantiate WebScrape model, this time taking live values from database
    # and putting them back into a pandas dataframe.
    df = pd.DataFrame(list(WebScrape.objects.all().values()))
    register_events(scheduler)
    # Use to_numberic and to_datetime pandas methods for coercing cases, deaths,
    # and date values to their proper data types (for use in plotting and analysis).
    df[['cases', 'deaths']] = df[['cases', 'deaths']].apply(pd.to_numeric)
    df[['date']] = df[['date']].apply(pd.to_datetime)

    # Homogenizing rows with daily totals.
    df['counties'] = df['counties'].replace({'GrandTotal': 'Totals'})

    # Makes a data frame consisting exclusively of daily totals.
    totals = df.loc[df['counties'] == 'Totals']

    sns.set(style="darkgrid")
    sns.barplot(x='date', y='cases', data=totals)
    plt.title('Test Plot')
    plt.show()
    
    plt.savefig(response, format="png")

    return df'''


print('Scrape scheduler running...')
print('Current data pulled from database...')
