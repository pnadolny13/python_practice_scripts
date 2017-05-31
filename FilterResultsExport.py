import time
import datetime
from datetime import timedelta

pyspark

time.sleep(10)
mydata = sc.textFile("/IO/results.csv")
mydata.count()

today_long = datetime.datetime.now()
today = (today_long.date()).strftime("%-m/%-d/%Y")
day_list = [1,2,3,4,5,6];
count = 1;
for day in day_list:
  "day_"+ str(count) = ((today_long - datetime.timedelta(days =count)).date()).strftime("%-m/%-d/%Y")
  count = count +1

mydata_filt= mydata.filter(lambda x: today in x or day_1 in x or day_2 in x or day_3 in x or day_4 in x or day_5 in x or day_6 in x)

mydata_filt.saveAsTextFile("/IO/FilteredResults/")
