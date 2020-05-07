from apscheduler.schedulers.background import BackgroundScheduler

# Start the scheduler
sched = BackgroundScheduler(daemon=True)
job = None


# Defining the function to be scheduled

def dbschedule():
    print('One tick!')

# Schedules above function to be run at 4:00pm daily


def start_job():
    global job
    job = sched.add_job(dbschedule, 'cron', hour='16')
    try:
        sched.start()
    except:
        pass
