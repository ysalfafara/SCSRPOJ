import csv,sys,os
from sample.models import ReviewSites


project_dir = 'C:/Users/Yesha/website/website'
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

django.setup()

def insert_to_database():
    data = csv.reader(open('C:/Users/Yesha/website/booking_reviews.csv'), delimiter=",")

    for row in data:
        if row[0] != 'site':
            rs = ReviewSites()
            rs.site = row[0]
            rs.review = row[1]
            rs.date = row[2]
            rs.sentiment = row[3]
            rs.save()



