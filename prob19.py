# Project Euler Problem #19

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.

# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


class Year(object):
    def __init__(self, year):
        self.year = year

    def __repr__(self):
        return "{}".format(self.year)

    def __eq__(self, year):
        return self.year == year

    def __le__(self, year):
        return self.year <= year

    def __ge__(self, year):
        return self.year >= year

    def incYear(self):
        self.year += 1

    def isLeapYear(self):
        if self.year % 100 == 0:
            return self.year % 400 == 0
        return self.year % 4 == 0


class Month(object):

    MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    MONTH_TO_NUM_DAYS = dict(zip(MONTHS, DAYS))
    MONTH_TO_NUM = dict(zip(MONTHS, range(1, len(MONTHS) + 1)))

    def __init__(self, month):
        assert(month in self.MONTHS)
        self.month = month

    def __iter__(self):
        for m in self.MONTHS:
            yield m

    def __repr__(self):
        return self.month

    def monthNumber(self):
        return self.MONTH_TO_NUM[self.month]

    def daysInMonth(self, isLeapYear=False):
        if self.month == "Feb" and isLeapYear:
            return 29
        else:
            return self.MONTH_TO_NUM_DAYS[self.month]

    @staticmethod
    def monthsPerYear(self):
        return len(self.MONTHS)

    def incMonth(self):
        """
        Increments the month and returns a bool representing whether a new year boundary was passed.
        """
        monthNum = self.monthNumber()
        self.month = self.MONTHS[monthNum % len(self.MONTHS)]
        return monthNum == 12

    def _print_debug(self):
        print self.MONTHS_TO_NUM_DAYS
        print self.MONTH_TO_NUM


class Day(object):
    DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    DAYS_PER_WEEK = len(DAYS)
    DAY_TO_NUM = dict(zip(DAYS, range(1, DAYS_PER_WEEK + 1)))

    def __init__(self, day):
        self.day = day

    def __repr__(self):
        return self.day

    def __eq__(self, day):
        return self.day == day

    def dayNumber(self):
        return self.DAY_TO_NUM[self.day]

    def __add__(self, numDays):
        """
        Advance the specified number of days.
        """
        leftoverDays = numDays % self.DAYS_PER_WEEK
        newDayNum = (leftoverDays + self.dayNumber()) % self.DAYS_PER_WEEK
        self.day = self.DAYS[newDayNum]
        return self


# Starting on Monday Jan 1st, 1900.
YEAR_ONE = 1900
YEAR_COUNT_BEGIN = 1901
YEAR_COUNT_END = 2000


# Advances to the first day of the next month.
def advanceMonth(curr_year, curr_month, curr_day):

    newYear = curr_year
    newMonth = curr_month
    newDay = curr_day

    # Determine the number of days in the current month.
    monthDays = curr_month.daysInMonth(curr_year.isLeapYear())

    # Increment month and year.
    yearPassed = newMonth.incMonth()
    if yearPassed:
        newYear.incYear()

    # Determine the new current day.
    newDay += monthDays

    return newYear, newMonth, newDay


def main():
    curr_year = Year(YEAR_ONE)
    curr_month = Month("Jan")
    curr_day = Day("Mon")
    totalFirstSundays = 0

    while curr_year <= YEAR_COUNT_END:
        curr_year, curr_month, curr_day = advanceMonth(curr_year, curr_month, curr_day)
        if curr_year >= YEAR_COUNT_BEGIN and curr_day == "Sun":
            totalFirstSundays += 1
        print curr_year, curr_month, curr_day, totalFirstSundays

    print "Answer = ", totalFirstSundays

main()
