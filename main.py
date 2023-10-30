# SUDO: Build a function that takes user input and then a loop to act as the timer
import time
import datetime
import sys


timer_input = input('How long would you like to focus? (In minutes) ')

get_current_date = datetime.datetime.now()
am_pm = get_current_date.strftime('%p')
hour = get_current_date.hour
minute = get_current_date.minute

def countdown(timer):
    focus_until_time =  int(timer) + int(minute)
    timer *= 60
    print('Focusing until ' + str(hour) + ':' + str(focus_until_time) + ' ' + am_pm + ' Press ctrl + c to end early.')
    while timer > 0:
        sys.stdout.write('\r' + str(timer))
        sys.stdout.flush()
        time.sleep(1)
        timer -= 1
    print('Times up!')

countdown(int(timer_input))