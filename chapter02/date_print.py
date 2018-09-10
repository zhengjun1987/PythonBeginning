#! /usr/bin/env python3

months = [
    'January',
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] \
          + ['st']

year = input("Year:")
month = input("Month:")
day = input("Day(1-31):")

month_number = int(month) - 1
day_number = int(day) - 1

month_name = months[month_number]
ordinal = day + endings[day_number]
print(month_name+" " +ordinal + ", " + year )
# zhengjuns-MacBook-Pro:chapter02 zhengjun$ chmod a+x date_print.py
# zhengjuns-MacBook-Pro:chapter02 zhengjun$ /Users/zhengjun/Desktop/PythonBeginning/chapter02/date_print.py
# Year:2018
# Month:9
# Day(1-31):10
# September 10th, 2018
