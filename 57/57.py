import calendar


class Zate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getWeekdayCount(self):
        return calendar.weekday(self.year, self.month, self.day)

    def getWeekdayName(self):
        weekday_index = self.getWeekdayCount()
        return calendar.day_name[weekday_index]

    def getMonthName(self):
        return calendar.month_name[self.month]


zate = Zate(2008, 7, 30)

print(zate.getYear())
print(zate.getMonth())
print(zate.getDay())
print(zate.getWeekdayCount())
print(zate.getWeekdayName())
print(zate.getMonthName())
