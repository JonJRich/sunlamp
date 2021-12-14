from gpiozero import PWMLED, TimeOfDay
from datetime import time, datetime
from time import sleep
from signal import pause 


ledbright = PWMLED(13)
ledwarm = PWMLED(17)

print("LEDs GO!")

#Temperature settings

def min_temp():
    ledwarm.value = 1
    ledbright.value = 0

def max_temp():
    ledbright.value = 1
    ledwarm.value = 0

print("Temperature settings GO!")

#Fade settings

def fade_to_max_temp(duration):
    ledwarm.value = 1
    ledwarm.pulse(0,duration,1)
    ledbright.pulse(duration,0,1,False)
    ledbright.value = 1

def fade_to_min_temp(duration):
    ledbright.value = 1
    ledbright.pulse(0,duration,1)
    ledwarm.pulse(duration,0,1,False)
    ledwarm.value = 1

print("Fade settings GO!")

#Temperature zone settings

def day_temp():
    min_temp()
    fade_to_max_temp(60)
    max_temp()
    pause()

def night_temp():
    max_temp()
    fade_to_min_temp(60)
    min_temp()
    pause()

print("Temperature zones GO!")

#Temperature zones throughout the day

night_zone = TimeOfDay(time(9), time(2)) # warm white
day_zone = TimeOfDay(time(2), time(9)) # bright white

print("Zone times GO!")

#GO!

#Convbert times to strings

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
night_zone_start = night_zone.start_time
night_zone_end = night_zone.end_time
day_zone_start = day_zone.start_time
day_zone_end = day_zone.end_time

night_start = night_zone_start.strftime("%H:%M:%S")
night_end = night_zone_end.strftime("%H:%M:%S")
day_start = day_zone_start.strftime("%H:%M:%S")
day_end = day_zone_end.strftime("%H:%M:%S")


#Check Day, even if it crosses midnight

def check_day_zone():
    if current_time > day_start and day_end > current_time:
        print("Day zone activated")
        day_temp()

def check_day_zone_24():
    if current_time > day_start or day_end > current_time:
        print("Day zone activated")
        day_temp()

def day_check_24():
    if day_start < day_end:
        check_day_zone()
    else: 
        check_day_zone_24()

#Check Night, even if it crosses midnight

def check_night_zone():
    if current_time > night_start and night_end > current_time:
        print("Night zone activated")
        night_temp()

def check_night_zone_24():
    if current_time > night_start or night_end > current_time:
        print("Night zone activated")
        night_temp()

def night_check_24():
    if night_start < night_end:
        check_night_zone()
    else: 
        check_night_zone_24()

# Check booth zones at once
        

day_check_24()
night_check_24()

# night_zone.when_activated = night_temp
# day_zone.when_activated = day_temp

pause ()
