#-*- coding:utf-8 -*-
import datetime
import time

#使用format

d1 = datetime.date(2013, 12, 25)
print format(d1)
#out : 2013-12-25

d2 = datetime.datetime(2013, 12, 25)
print format(d2)
#out : 2013-12-25 00:00:00




#string转datetime
str = '2012-11-19'
date_time = datetime.datetime.strptime(str,'%Y-%m-%d')
print date_time

datetime.datetime(2012,11,19,0,0)


#datetime转string
date_time.strftime('%Y-%m-%d')

#out : '2012-11-19'

#datetime转时间戳

time_time = time.mktime(date_time.timetuple())

print time_time

# out : 1353254400.0

#时间戳转string

time.strftime('%Y-%m-%d',time.localtime(time_time))

# out : '2012-11-19'

#date转datetime

date = datetime.date.today()
pirint date

print datetime.date(2012,11,19)

#将date转换为str，在由str转换为datetime
print datetime.datetime.strptime(str(date),'%Y-%m-%d')

print datetime.datetime(2012,11,19,0,0)
