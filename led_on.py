from gpiozero import PWMLED
from time import sleep
from signal import pause 

ledbright = PWMLED(17)
ledwarm = PWMLED(13)

print("LEDs instantiated")

while True:
    ledbright.value = 0 
    ledwarm.value = 1 
    sleep(2)
    ledbright.value = 0.1 
    ledwarm.value = 0.9 
    sleep(0.1)
    ledbright.value = 0.2 
    ledwarm.value = 0.8 
    sleep(0.1)
    ledbright.value = 0.3 
    ledwarm.value = 0.7 
    sleep(0.1)
    ledbright.value = 0.4
    ledwarm.value = 0.6
    sleep (0.1)
    ledbright.value = 0.5
    ledwarm.value = 0.5
    sleep(1)
    ledbright.value = 0.6
    ledwarm.value = 0.4
    sleep (0.1)
    ledbright.value = 0.7
    ledwarm.value = 0.3
    sleep (0.1)
    ledbright.value = 0.8
    ledwarm.value = 0.2
    sleep (0.1)
    ledbright.value = 0.9
    ledwarm.value = 0.1
    sleep (0.1)
    ledbright.value = 1
    ledwarm.value = 0
    sleep(2)
    ledbright.value = 0.9
    ledwarm.value = 0.1
    sleep (0.1)
    ledbright.value = 0.8
    ledwarm.value = 0.2
    sleep (0.1)
    ledbright.value = 0.7
    ledwarm.value = 0.3
    sleep (0.1)
    ledbright.value = 0.6
    ledwarm.value = 0.4
    sleep (0.1)
    ledbright.value = 0.5
    ledwarm.value = 0.5
    sleep(1)
    ledbright.value = 0.4
    ledwarm.value = 0.6
    sleep (0.1)
    ledbright.value = 0.5
    ledwarm.value = 0.5
    sleep(1)
    ledbright.value = 0.4
    ledwarm.value = 0.6
    sleep (0.1)
    ledbright.value = 0.3 
    ledwarm.value = 0.7 
    sleep(0.1)
    ledbright.value = 0.2 
    ledwarm.value = 0.8 
    sleep(0.1)
    ledbright.value = 0.1 
    ledwarm.value = 0.9 
    sleep(0.1)

print("Exited while loop")
