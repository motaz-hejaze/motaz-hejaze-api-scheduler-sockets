from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from . import apiConnector

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apiConnector.update_items_table , 'interval' , seconds=30)
    scheduler.start()