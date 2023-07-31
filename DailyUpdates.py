import sys
from datetime import date, datetime
import calendar
from meteostat import Point, Daily

# TODO: Create database with tables for QUOTES, WARDROBE, NOTES


def updateQuote() -> str:
    # TODO: read a random row from an excel sheet/ database
    # TODO: make that^ only happen once a day, and not once per GUI refresh - value assigned randomly each day?
    return "<i>A ship is safe in harbor. But that's not where a ship is meant to be.</i>"


def updateWeather(zip):
    print("updateWeather has this zip code: " + zip)
    # TODO: get location
    vancouver = Point(49.2497, -123.1193, 70)
    start = datetime(2022, 6, 30)
    data = Daily(vancouver, start, start)
    data = data.fetch()
    min = data['tmin'].values.astype(float)
    max = data['tmax'].values.astype(float)
    tmax = float(max[0])
    tmin = float(min[0])
    print(tmin)
    print(tmax)
    # TODO: current,1-day,3-day,7-day outlook options
    return [tmin, tmax, 'Leawood, KS']


def updateDate() -> str:
    now = datetime.now()
    curr_date = date.today()
    nameofday = calendar.day_name[curr_date.weekday()]
    year = now.strftime("%Y")
    month = now.strftime("%B")
    day = now.strftime("%d")

    todayDate = nameofday + "\n" + month + " " + day + ", " + year

    return str(todayDate)


def updateTime():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    rightAligned_time = "<p align='right'>" + current_time + "</p>"
    return rightAligned_time


class DailyUpdates:
    pass
