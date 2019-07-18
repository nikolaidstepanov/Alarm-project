# -*- coding: utf-8 -*-
import music
import datetime

now = datetime.datetime.now()


class Time:

    def __init__(self):
        self.CurrentMonth = 0
        self.CurrentDay = 0
        self.CurrentHour = 0
        self.CurrentMinute = 0
        self.FutureMonth = 1
        self.FutureDay = 1
        self.FutureHour = 1
        self.FutureMinute = 1

    def set_time_now(self):
        self.CurrentMonth = now.month
        self.CurrentDay = now.day
        self.CurrentHour = now.hour
        self.CurrentMinute = now.minute

        return self.CurrentMonth, self.CurrentDay, self.CurrentHour, self.CurrentMinute

    def validate_now_time(self, month, day, hour, minute):
        self.CurrentMonth, self.CurrentDay, self.CurrentHour, self.CurrentMinute = self.set_time_now()
        if (month < self.CurrentMonth) or (day < self.CurrentDay) or (hour < self.CurrentHour) or (minute < self.CurrentMinute):
            error = 6
            return error
        else:
            error = 0
            return error


class FutureTime(Time):

    def set_time_alarm(self, day, hour, minute):
        for i in range(10):
            if (hour == '0' + str(i)):
                hour = i
        for i in range(10):
            if (minute == '0' + str(i)):
                minute = i
        self.FutureDay = int(day)
        self.FutureHour = int(hour)
        self.FutureMinute = int(minute)

        return self.FutureDay, self.FutureHour, self.FutureMinute

    def alarm_clock(self, future_month, future_day, future_hour, future_minute):
        while (self.CurrentMonth != future_month) or (self.CurrentDay != future_day) or (self.CurrentHour != future_hour) or (self.CurrentMinute != future_minute):
            timer = datetime.datetime.now()
            self.CurrentMonth = timer.month
            self.CurrentDay = timer.day
            self.CurrentHour = timer.hour
            self.CurrentMinute = timer.minute
        music.start()


def alarm_stop():
    music.stop()


def get_correct_time(month, hour, minute):
    ArrayMonth = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октябрь", "Ноябрь", "Декабрь"]
    month = str(ArrayMonth[month - 1])
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    return month, hour, minute


def get_month(month):
    month = month.lower()
    ArrayMonth = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октябрь",
                  "ноябрь", "декабрь"]
    month.lower()
    for i in range(12):
        if ArrayMonth[i] == month:
            month = i+1
            break
    else:
        month = -2
    return month


def validate_correct(month, day, hour, minute, str_day, str_hour, str_minute):
    error = 0
    str_day = len(str_day)
    str_hour = len(str_hour)
    str_minute = len(str_minute)

    # month is iterated over even
    for i in range(1, 12, 2):
        if month == i:
            if (day > 31) or (str_day > 2):
                error = 3
                break
            elif (month == 2) and (day > 29) and (str_day > 2):
                error = 3
                break
            elif (hour > 24) or (str_hour > 2):
                error = 4
                break
            elif (minute > 60) or (str_minute > 2):
                error = 5
                break
            else:
                error = 0
        elif (day > 30) or(str_day > 2):
            error = 3
            break
        elif (hour > 24) or (str_hour > 2):
            error = 4
            break
        elif (minute > 60) or (str_minute > 2):
            error = 5
            break
        else:
            error = 0

    return error


def validate_zero(str_month, str_day, str_hour, str_minute):
    str_month = len(str_month)
    str_day = len(str_day)
    str_hour = len(str_hour)
    str_minute = len(str_minute)

    if (str_month == 0) or (str_day == 0) or (str_hour == 0) or (str_minute == 0):
        error = 1
        return error
    else:
        error = 0
        return error


def change_music1():
    music.change_source(1)


def change_music2():
    music.change_source(2)


def change_music3():
    music.change_source(3)


def change_music4():
    music.change_source(4)


def change_music5():
    music.change_source(5)


def change_music6():
    music.change_source(6)


CurrentTime = Time()
FutureTimer = FutureTime()

CurrentTime.set_time_now()

NowMonth = CurrentTime.CurrentMonth
NowDay = CurrentTime.CurrentDay
NowHour = CurrentTime.CurrentHour
NowMinute = CurrentTime.CurrentMinute

NowMonth, NowHour, NowMinute = get_correct_time(NowMonth, NowHour, NowMinute)
