# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
year_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
week_dict = {1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'sunday', 7: 'monday'}
# tuesday = 1
# sun-> 6,
# year = 1901
# first_day = 1


def one_year():

    day = 1
    year = 1901
    num_sundays = 0
    while year < 2001:
        month = 1
        while month < 13:
            if day % 7 == 6:
                num_sundays += 1
            day += year_dict[month]
            if month == 2 and year % 4 == 0:
                day += 1
            month += 1
        year += 1
    return num_sundays
print(one_year())
