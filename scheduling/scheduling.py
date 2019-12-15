import schedule
import threading
import time
import datetime


class JobSchedule(object):

    SECOND  = 0
    MINUTE  = 1
    HOUR    = 2
    DAY     = 3
    WEEK    = 4

    NEW_YEAR = "0101"
    EPIPHANY = "0106"
    LIBERATION = "0425"
    LABOUR_DAY = "0501"
    REPUBLIC_DAY = "0206"
    ASSUMPTION_DAY = "0815"
    ALL_SAINTS = "1101"
    IMMACULATE_DAY = "1208"
    CHRISTMAS = "1225"
    STEPHEN = "1226"

    def __init__(self, job, time_schedule, repetition, static_holiday, *args):
        self.job = job
        self.args = args
        self.time_schedule = time_schedule
        self.repetition = repetition
        self.static_holiday = static_holiday


class SchedulingError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ScheduleManager(object):
    manager = schedule.Scheduler()

    def __init__(self, jobs: list, jobs_static_holidays: list):
        """
        Constructor with a jobs list to schedule
        :param jobs: a list of JobSchedule
        """
        self.jobs =  jobs
        self.static_jobs = jobs_static_holidays
        t = threading.Thread(target=self.__init_jobs)
        t1 = threading.Thread(target=self.__init_static_holidays_jobs)
        t.start()
        t1.start()

    def __init_jobs(self):
        for job in self.jobs:
            if isinstance(job, JobSchedule):
                if job.repetition == JobSchedule.SECOND:
                    self.manager.every(job.time_schedule).seconds.do(job.job, *job.args)
                elif job.repetition == JobSchedule.MINUTE:
                    self.manager.every(job.time_schedule).minutes.do(job.job, *job.args)
                elif job.repetition == JobSchedule.HOUR:
                    self.manager.every(job.time_schedule).hours.do(job.job, *job.args)
                elif job.repetition == JobSchedule.DAY:
                    self.manager.every(job.time_schedule).days.do(job.job, *job.args)
                elif job.repetition == JobSchedule.WEEK:
                    self.manager.every(7).days.do(job.job, *job.args)
                else:
                    raise SchedulingError("Job repetition not valid.")
            else:
                raise SchedulingError("Error: job in job list is not an instance of JobSchedule")

    def __init_static_holidays_jobs(self):
        for sj in self.static_jobs:
            if isinstance(sj, JobSchedule):
                self.check_static_holidays(job=sj)
            else:
                raise SchedulingError("Error: job in job list is not an instance of JobSchedule")

    def check_static_holidays(self, job: JobSchedule):
        now = datetime.datetime.now().date()
        if (job.static_holiday == JobSchedule.NEW_YEAR and now.month == 1 and now.day == 1) or\
                (job.static_holiday == JobSchedule.EPIPHANY and now.month == 1 and now.day == 6):
            self.__start_check_on_thread(job)
        elif job.static_holiday == JobSchedule.LIBERATION and now.month == 4 and now.day == 25:
            self.__start_check_on_thread(job)
        elif job.static_holiday == JobSchedule.LABOUR_DAY and now.month == 5 and now.day == 1:
            self.__start_check_on_thread(job)
        elif job.static_holiday == JobSchedule.REPUBLIC_DAY and now.month == 6 and now.day == 2:
            self.__start_check_on_thread(job)
        elif job.static_holiday == JobSchedule.ASSUMPTION_DAY and now.month == 8 and now.day == 15:
            self.__start_check_on_thread(job)
        elif job.static_holiday == JobSchedule.ALL_SAINTS and now.month == 11 and now.day == 1:
            self.__start_check_on_thread(job)
        elif now.month == 12 and ((job.static_holiday == JobSchedule.IMMACULATE_DAY and now.day == 8) or\
                                  (job.static_holiday == JobSchedule.CHRISTMAS and now.day == 25 ) or\
                                  (job.static_holiday == JobSchedule.STEPHEN and now.day == 26)):
            self.__start_check_on_thread(job)

    def __start_check_on_thread(self, job: JobSchedule):
        t = threading.Thread(target=job.job, args=job.args)
        t.start()

    def run_checks(self):
        while True:
            self.manager.run_pending()
            time.sleep(1)