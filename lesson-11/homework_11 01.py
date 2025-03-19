class Data(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{"{:02d}".format(self.day)}-{"{:02d}".format(self.month)}-{"{:02d}".format(self.year)}'

    @classmethod
    def my_method(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        date = cls(day, month, year)
        return date

    @staticmethod
    def my_method_1(date_string):
        day, month, year = map(int, date_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date1 = Data.my_method('11-06-2013')
print(date1)
is_date = Data.my_method_1('11-06-2012')
print(is_date)
