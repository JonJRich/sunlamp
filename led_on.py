from gpiozero import PWMLED, TimeOfDay
from datetime import time, datetime
from time import sleep
from signal import pause 
import os

#### DEFINE INPUTS

print("Defining inputs")

def parse_zone_configs(val):
    return datetime.strptime(val,'%H:%M')

LED_PIN_BRIGHT = 13
LED_PIN_WARM = 17

LAMP_ON_START = parse_zone_configs(os.getenv("LAMP_ON_START","8:00"))
LAMP_OFF_START = parse_zone_configs(os.getenv("LAMP_OFF_START","20:00"))

LAMP_WARM_START = parse_zone_configs(os.getenv("LAMP_WARM_START","16:00"))
LAMP_BRIGHT_START = parse_zone_configs(os.getenv("LAMP_BRIGHT_START","9:00"))

####DEFINE INSTANCES

#Define LEDs
print("Initialise LED instances")
ledbright = PWMLED(LED_PIN_BRIGHT)
ledwarm = PWMLED(LED_PIN_WARM)

#Define lamp state times
print("Initialise lamp state times")
on_zone = TimeOfDay(LAMP_ON_START, LAMP_OFF_START) # lamp on
off_zone = TimeOfDay(LAMP_OFF_START, LAMP_ON_START) # lamp off

#Define lamp temperature times
print("Initialise lamp temperature times")
bright_zone = TimeOfDay(LAMP_BRIGHT_START, LAMP_WARM_START) # bright white
warm_zone = TimeOfDay(LAMP_WARM_START, LAMP_BRIGHT_START) # warm white

#Define fade time from colour temperatures and on/off fade
print("Initialise lamp fade duration")
FADE_DURATION = int(os.getenv("FADE_DURATION","30")) #seconds

print("Parameters defined")

###DEFINE FUNCTIONS

#Temperature settings
def warm_on():
    ledwarm.value = 1
    ledbright.value = 0

def bright_on():
    ledbright.value = 1
    ledwarm.value = 0

#Off function
def lamp_off():
    ledwarm.value = 0
    ledbright.value = 0

#Fade settings
def fade_on_bright(duration):
    ledbright.pulse(duration,0,1, False)
    ledbright.value = 1

def fade_on_warm(duration):
    ledwarm.pulse(duration,0,1, False)
    ledwarm.value = 1

def fade_off_warm(duration):
    ledwarm.pulse(0,duration,1, False)
    ledwarm.value = 0

def fade_warm_to_bright(duration):
    ledwarm.value = 1
    ledwarm.pulse(0,duration,1)
    ledbright.pulse(duration,0,1,False)
    ledbright.value = 1

def fade_bright_to_warm(duration):
    ledbright.value = 1
    ledbright.pulse(0,duration,1)
    ledwarm.pulse(duration,0,1,False)
    ledwarm.value = 1

def test_cycle():
    print("-Fade on night")
    fade_on_warm(FADE_DURATION)
    sleep(5)
    print("--Sunrise start")
    fade_warm_to_bright(FADE_DURATION)
    sleep(5)
    print("---Daytime")
    bright_on()
    sleep(5)
    print("----Sunsset start")
    fade_bright_to_warm(FADE_DURATION)
    sleep(5)
    print("-----Nighttime")
    warm_on()
    sleep(5)
    print("------Turning off...")
    fade_off_warm(FADE_DURATION)
    sleep(5)
    print("Test cycle complete")

###RUNNING SCRIPT

print("Running mood lamp")

#print("Running test cycle")
#test_cycle()

#Check if lamp is not in off zone
if not off_zone.is_active:
    # if day zone active, do x
    if bright_zone.is_active:
        print("manually setting Bright Zone")
        fade_on_bright(FADE_DURATION)
    # if night zone active, do y
    else:
        print("manually setting Warm Zone")
        fade_on_warm(FADE_DURATION)

print("listening mode started")

on_zone.when_activated = fade_on_warm(FADE_DURATION)
warm_zone.when_activated = fade_bright_to_warm(FADE_DURATION)
bright_zone.when_activated = fade_warm_to_bright(FADE_DURATION)
off_zone.when_activated = fade_off_warm(FADE_DURATION)

pause ()