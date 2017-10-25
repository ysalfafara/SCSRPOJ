import csv,sys,os

project_dir = 'C:/Users/Yesha/website/website'
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from sample.models import ReviewSites

data = csv.reader(open('C:/Users/Yesha/website/agoda_reviews.csv'), delimiter=",")

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



