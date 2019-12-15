import datetime


class HolidayManager(object):

    NEW_YEAR = None
    EPIPHANY = None
    LIBERATION = None
    LABOUR_DAY = None
    REPUBLIC_DAY = None
    ASSUMPTION_DAY = None
    ALL_SAINTS = None
    IMMACULATE_DAY = None
    CHRISTMAS = None
    STEPHEN = None

    SATURDAY = 5
    SUNDAY = 6

    def __init__(self, tempDate:datetime.date=None):
        if tempDate is not None:
            self.tempDate = tempDate
            self.init_static_holidays(year=self.tempDate.year)
        else:
            year = datetime.datetime.now().year
            self.init_static_holidays(year=year)

    def init_static_holidays(self, year: int) -> None:
        """
        Method that initialize static holidays date with the year parameter
        :param year: int
        :return:
        """
        self.NEW_YEAR = datetime.date(year, 1, 1)
        self.EPIPHANY = datetime.date(year, 1, 6)
        self.LIBERATION = datetime.date(year, 4, 25)
        self.LABOUR_DAY = datetime.date(year, 5, 1)
        self.REPUBLIC_DAY = datetime.date(year, 6, 2)
        self.ASSUMPTION_DAY = datetime.date(year, 8, 15)
        self.ALL_SAINTS = datetime.date(year, 11, 1)
        self.IMMACULATE_DAY = datetime.date(year, 12, 8)
        self.CHRISTMAS = datetime.date(year, 12, 25)
        self.STEPHEN = datetime.date(year, 12, 26)

    def checkholidays(self, date: datetime.date) -> bool:
        return self.checkeaster(date) or\
               self.check_static_holidays(date) or\
            self.check_weekend(date)
        pass

    def checkeaster(self, date: datetime.date) -> bool:
        if date == self.calculate_easter(date.year):
            return True
        else:
            return False

    def check_static_holidays(self, date: datetime.date) -> bool:
        if self.NEW_YEAR == date or\
            self.EPIPHANY == date or\
            self.LIBERATION == date or\
            self.LABOUR_DAY == date or\
            self.REPUBLIC_DAY == date or\
            self.ASSUMPTION_DAY == date or\
            self.ALL_SAINTS == date or\
            self.IMMACULATE_DAY == date or\
            self.CHRISTMAS == date or\
                self.STEPHEN == date:
            return True
        else:
            return False

    def check_weekend(self, date: datetime.date):
        if date.weekday() == self.SATURDAY or date.weekday() == self.SUNDAY:
            return True
        else:
            return False

    def calculate_easter(self, year: int) -> datetime.date:
        """
        Calculates easter date with Gauss method
        :param year:
        :return: easter date
        """
        a = year % 19
        b = year % 4
        c = year % 7
        d = ((19 * a) + self.__get_M(year=year)) % 30
        e = ((2 * b) + (4 * c) + (6 * d) + self.__get_N(year=year)) % 7

        month = 0
        day = 0

        if d+e < 10:
            day = (d + e + 22)
            month = 3
        else:
            day = (d + e - 9)
            month = 4

        return datetime.date(year, month, day)

    def __get_M(self, year: int) -> int:
        if 1900 <= year <= 2199:
            return 24
        if (2200 <= year <= 2299) or (2400 <= year <= 2499):
            return 25
        if 2300 <= year <= 2399:
            return 26

    def __get_N(self, year: int) -> int:
        if 1900 <= year <= 2099:
            return 5
        if 2100 <= year <= 2199:
            return 6
        if 2200 <= year <= 2299:
            return 0
        if 2300 <= year <= 2499:
            return 1