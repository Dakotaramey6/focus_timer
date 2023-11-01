# SUDO: Build a function that takes user input and then a loop to act as the timer
import time
import datetime


timer_input = input('How long would you like to focus? (In minutes) ')

get_current_date = datetime.datetime.now()
am_pm = get_current_date.strftime('%p')
hour = get_current_date.hour
minute = get_current_date.minute


def countdown(timer):
    focus_until_time = int(minute) + timer
    print('Focusing until ' + str(hour) + ':' + str(focus_until_time) +
          ' ' + am_pm + '  ctrl + c to end early.')
    timer_minutes = timer * 60
    for i in range(timer_minutes):
        print("\033[K", timer_minutes - i, end='\r')
        time.sleep(1)
    print('Times up!', end='\n')


countdown(int(timer_input))
