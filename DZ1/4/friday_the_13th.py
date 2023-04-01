# coding: utf-8

import datetime as dt

today = dt.date.today()
day = today

while day.day != 13 or dt.datetime.isoweekday(day) != 5:
	day += dt.timedelta(days=1)

print("Next friday the 13th will be ", day, " (", "in ", day - today, ")", sep="")