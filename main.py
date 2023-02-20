from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.properties import StringProperty
import datetime

year = round(datetime.datetime.now().year / 27)
month = round(datetime.datetime.now().month / 9)
day = round(datetime.datetime.now().day / 27.3)

if datetime.datetime.now().month > 3 and \
        datetime.datetime.now().month < 6:
    year += 1

if datetime.datetime.now().month > 6 and \
        datetime.datetime.now().month < 9:
    year += 2

if datetime.datetime.now().month > 9 and \
        datetime.datetime.now().month < 12:
    year += 3

if datetime.datetime.now().day > 9 and \
    datetime.datetime.now().day < 18:
    day += 1

if datetime.datetime.now().day > 18 and \
    datetime.datetime.now().day < 27:
    day += 2

if month == 0:
    month = 1

if day == 0:
    day = 1

if year == 0:
    year = 1

class ADM(ScreenManager):
    pass

class Info(Screen):
    pass

class Date(Label):
    text = StringProperty(f'Month/Day/Year: {str(month)}/{str(day)}/{str(year)}')

class Jonan_Calendar_to_Moon(App):
    pass

if __name__ == '__main__':
    Jonan_Calendar_to_Moon().run()
