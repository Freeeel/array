from datetime import datetime


class Period:
    def __init__(self, start, end):
        self.start = start_time
        self.end = end_time

    def getSeconds(self):
        res = self.end - self.start
        return res.total_seconds()

    def getMinutes(self):
        res = self.end - self.start
        return res.total_seconds() / 60

    def getHours(self):
        res = self.end - self.start
        return res.total_seconds() / 3600

    def getDays(self):
        res = self.end - self.start
        return res.days


start_time = datetime(2023, 4, 12, 3, 53, 34)
end_time = datetime(2023, 9, 25, 12, 12, 54)
period = Period(start_time, end_time)

print(period.getSeconds())
print(period.getMinutes())
print(period.getHours())
print(period.getDays())
