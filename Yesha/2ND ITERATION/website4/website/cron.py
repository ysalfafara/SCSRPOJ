from django.conf import settings
from django_cron import CronJobBase, Schedule
import csv,sys,os
import django
from sample.models import ReviewSites


project_dir = 'C:/Users/Yesha/website/website'
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

django.setup()

class insert_data_cron(CronJobBase):
    """
    Send an email with the user count.
    """
    RUN_EVERY_MINS = 5   #5minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.insert_data_cron'

    def do(self):
        data = csv.reader(open('C:/Users/Yesha/website/test.csv'), delimiter=",")

        for row in data:
            if row[0] != 'site':
                rs = ReviewSites()
                rs.site = row[0]
                rs.review = row[1]
                rs.month = row[2]
                rs.day = row[3]
                rs.year = row[4]
                rs.rate = row[5]
                rs.sentiment = row[6]
                rs.save()