
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scheduler import tweetsUpdater

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tweetsUpdater.update_db, 'interval', days=15)
    scheduler.start()