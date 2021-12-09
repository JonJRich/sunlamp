from gpiozero import PWMLED, TimeOfDay
from datetime import time
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

night_zone = TimeOfDay(time(21,2,0,0), time(21,3,0,0)) # warm white
day_zone = TimeOfDay(time(21,3,0,0), time(23)) # bright white

print("Zone times GO!")

#GO!

print("GO!")

night_zone.when_activated = night_temp
day_zone.when_activated = day_temp

pause ()



# MINIMUM_TEMP + ((MAXIMUM_TEMP-MINIMUM_TEMP)*(x/60))
# MAXIMUM_TEMP - ((MAXIMUM_TEMP-MINIMUM_TEMP)*(x/60))

# MINIMUM_TEMP = 3000
# MAXIMUM_TEMP = 6000
# MAXIMUM_BRIGHTNESS = 1.0

#temperature = 0

# def set_temp(temp_to_set_to):
  #  global temperature 