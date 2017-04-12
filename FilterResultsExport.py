import time
import datetime
from datetime import timedelta

pyspark

time.sleep(10)
mydata = sc.textFile("/IO/results.csv")
mydata.count()

today_long = datetime.datetime.now()
today = (today_long.date()).strftime("%-m/%-d/%Y")
day_1 = ((today_long - datetime.timedelta(days =1)).date()).strftime("%-m/%-d/%Y")
day_2 = ((today_long - datetime.timedelta(days =2)).date()).strftime("%-m/%-d/%Y")
day_3 = ((today_long - datetime.timedelta(days =3)).date()).strftime("%-m/%-d/%Y")
day_4 = ((today_long - datetime.timedelta(days =4)).date()).strftime("%-m/%-d/%Y")
day_5 = ((today_long - datetime.timedelta(days =5)).date()).strftime("%-m/%-d/%Y")
day_6 = ((today_long - datetime.timedelta(days =6)).date()).strftime("%-m/%-d/%Y")

mydata_filt= mydata.filter(lambda x: today in x or day_1 in x or day_2 in x or day_3 in x or day_4 in x or day_5 in x or day_6 in x)

mydata_filt.saveAsTextFile("/IO/FilteredResults/")