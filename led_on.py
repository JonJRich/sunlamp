from gpiozero import PWMLED, TimeOfDay
from datetime import time, datetime
from time import sleep
from signal import pause 



####DEFINE PARAMETERS

#Define LED inputs
ledbright = PWMLED(13)
ledwarm = PWMLED(17)

#Define time zones
on_zone = TimeOfDay(time(8,0,0,0), time(22,0,0,0)) # lamp on
off_zone = TimeOfDay(time(22,0,0,0), time(8,0,0,0)) # lamp off
day_zone = TimeOfDay(time(11,0,0,0), time(12,0,0,0)) # bright white
night_zone = TimeOfDay(time(12,0,0,0), time(13,0,0,0)) # warm white

#Define fade time from colour temperatures and on/off fade
temp_fade = 120 #seconds

print("Parameters defined")



###DEFINE FUNCTIONS

#Temperature settings
def night_temp():
    ledwarm.value = 1
    ledbright.value = 0

def day_temp():
    ledbright.value = 1
    ledwarm.value = 0

#Off function
def lamp_off():
    ledwarm.value = 0
    ledbright.value = 0

#Fade settings

def fade_on_day(duration):
    ledbright.pulse(duration,0,1, False)
    ledbright.value = 1

def fade_on_night(duration):
    ledwarm.pulse(duration,0,1, False)
    ledwarm.value = 1

def fade_off_night(duration):
    ledwarm.pulse(0,duration,1, False)
    ledwarm.value = 0

def fade_to_day_temp(duration):
    ledwarm.value = 1
    ledwarm.pulse(0,duration,1)
    ledbright.pulse(duration,0,1,False)
    ledbright.value = 1

def fade_to_night_temp(duration):
    ledbright.value = 1
    ledbright.pulse(0,duration,1)
    ledwarm.pulse(duration,0,1,False)
    ledwarm.value = 1

#Temperature zone settings
def day_on():
    fade_on_day(temp_fade)
    day_temp()

def night_on():
    fade_on_night(temp_fade)
    night_off()

def night_off():
    fade_off_night(temp_fade)
    lamp_off()

def sunrise_temp():
    night_temp()
    fade_to_day_temp(temp_fade)
    day_temp()

def sunset_temp():
    day_temp()
    fade_to_night_temp(temp_fade)
    night_temp()

#Check Day and Lamp On, even if it crosses midnight
def check_day_zone():
    if current_time > day_start and day_end > current_time and current_time > on_start and on_end > current_time:
        print("Day zone activated")
        day_on()

def check_day_zone_24():
    if current_time > day_start or day_end > current_time and current_time > on_start and on_end > current_time:
        print("Day zone activated")
        day_on()

def day_check_24():
    if day_start < day_end:
        check_day_zone()
    else: 
        check_day_zone_24()

#Check Night, even if it crosses midnight
def check_night_zone():
    if current_time > night_start and night_end > current_time and current_time > on_start and on_end > current_time:
        print("Night zone activated")
        night_temp()

def check_night_zone_24():
    if current_time > night_start or night_end > current_time and current_time > on_start and on_end > current_time:
        print("Night zone activated")
        night_temp()

def night_check_24():
    if night_start < night_end:
        check_night_zone()
    else: 
        check_night_zone_24()

def test_cycle():
    print("Fade on night")
    fade_on_night(temp_fade)
    sleep(5)
    print("Sunrise start")
    sunrise_temp()
    sleep(5)
    print("Day start")
    day_temp()
    sleep(temp_fade)
    print("Sunsset start")
    sunset_temp()
    sleep(5)
    print("Night start")
    night_temp()
    sleep(temp_fade)
    fade_off_night(temp_fade)
    sleep(temp_fade)


#print("Functions defined")

###RUNNING SCRIPT

print("Running mood lamp")

#Check current time and convert all times to strings 
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

night_zone_start = night_zone.start_time
night_zone_end = night_zone.end_time

day_zone_start = day_zone.start_time
day_zone_end = day_zone.end_time

off_zone_start = off_zone.start_time
off_zone_end = off_zone.end_time

on_zone_start = on_zone.start_time
on_zone_end = on_zone.end_time


night_start = night_zone_start.strftime("%H:%M:%S")
night_end = night_zone_end.strftime("%H:%M:%S")

day_start = day_zone_start.strftime("%H:%M:%S")
day_end = day_zone_end.strftime("%H:%M:%S")

off_start = off_zone_start.strftime("%H:%M:%S")
off_end = off_zone_end.strftime("%H:%M:%S")

on_start = on_zone_start.strftime("%H:%M:%S")
on_end = on_zone_end.strftime("%H:%M:%S")

print("Checking times")

day_check_24()
night_check_24()

#print("Running test loop")
#test_cycle()
#print("Finished test loop")

print("listening mode started")

on_zone.when_activated = night_on
night_zone.when_activated = sunset_temp
day_zone.when_activated = sunrise_temp
off_zone.when_activated = night_off

pause ()