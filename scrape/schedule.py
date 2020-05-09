from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
#from django.core import management
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from datetime import date
from scrape.models import WebScrape
from scrape.scrape import *

# Defining the function to be scheduled, use DjangoJobStore
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


# Deletes job executions older than 7 days.
# DjangoJobExecution.objects.delete_old_job_executions(604_800)


@register_job(scheduler, 'cron', hour=15, minute=30)
def dataschedule():
    for i in Scrape.clean_scrape():
        a = WebScrape(date=i[0], counties=i[1], cases=i[2], deaths=i[3])
        a.save()
    print(date.today())
    # Monitoring per-execution
    register_events(scheduler)
    scheduler.start()


print('Scrape scheduler running...')
