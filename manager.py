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

    def __init__(self, tempDate:datetime.date=None):
        if tempDate is not None:
            self.tempDate = tempDate
            self.init_static_holidays()
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


    def init_static_holidays(self) -> None:
        """
        Method that initialize static holidays date with tempDate valorized
        :return: None
        """
        self.NEW_YEAR = datetime.date(self.tempDate.year, 1, 1)
        self.EPIPHANY = datetime.date(self.tempDate.year, 1, 6)
        self.LIBERATION = datetime.date(self.tempDate.year, 4, 25)
        self.LABOUR_DAY = datetime.date(self.tempDate.year, 5, 1)
        self.REPUBLIC_DAY = datetime.date(self.tempDate.year, 6, 2)
        self.ASSUMPTION_DAY = datetime.date(self.tempDate.year, 8, 15)
        self.ALL_SAINTS = datetime.date(self.tempDate.year, 11, 1)
        self.IMMACULATE_DAY = datetime.date(self.tempDate.year, 12, 8)
        self.CHRISTMAS = datetime.date(self.tempDate.year, 12, 25)
        self.STEPHEN = datetime.date(self.tempDate.year, 12, 26)


    def checkholidays(self, date: datetime.date):
        pass

    def checkeaster(self, date: datetime.date):
        pass

    def check_weekend(self, date: datetime.date):
        pass

    def calculate_easter(self, date: datetime.date):
        pass
