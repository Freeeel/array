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


class ZateExt(Zate):

    def add_year(self, year):
        return f'{self.year + year}'

    def minus_year(self, year):
        return f'{self.year - year}'

    def add_mounth(self, mounth):
        return f'{self.month + mounth}'

    def minus_mounth(self, mounth):
        return f'{self.month - mounth} '

    def add_day(self, day):
        return f'{self.day + day}'

    def minus_day(self, day):
        return f'{self.day - day}'


zate = ZateExt(2023, 12, 25)

print(zate.add_year(3))
print(zate.minus_year(10))

print(zate.add_mounth(4))
print(zate.minus_mounth(2))

print(zate.add_day(10))
print(zate.minus_day(3))
