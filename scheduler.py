from apscheduler.schedulers.background import BackgroundScheduler

def send_reminder():
    print("🔔 Take your medication!")

scheduler = BackgroundScheduler()
scheduler.add_job(send_reminder, 'interval', hours=6)
scheduler.start()