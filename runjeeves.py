from apscheduler.schedulers.blocking import BlockingScheduler
import runpy

def run_jeeves():
	exec(open("jeeves.py").read())
	

scheduler = BlockingScheduler()
scheduler.add_job(run_jeeves, 'interval', hours=1)
scheduler.start()


