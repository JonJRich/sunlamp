# Sunlamp

## Introduction

The sun is a magical thing, not only does it give us a light and warmth but through it's regular rising and setting it drives our circadian rythmn - the natural process that regulates our sleep–wake cycle.

But sometimes that connection with the natural rythmn of the sun breaks. If you're in the northern hemisphere in the depths of winter the idea of waking up at 8am and going to bed ast 4pm with the sun might sound ideal, but isn't exactly theasible. Equally sometimes you might need to be up late, or very early, sometimes by choice, and sometimes not.

So I created "Sunlamp".

An ambient lamp that can be programmed to mimic the natural light cycle of the sun, giving you a subtle reminder of the suns natural process through out the day. Gradually illuminating with a soft warm light, before rising to a bright light and repeating the cycle in reverse for the sunset.

Powered by a Raspberry Pi running on [Balena](https://www.balena.io) the lamp times and fade durations can be set remotely from anywhere in the world. The lights in the lamp are LED strips containing both Warm White and Bright Light LEDs. The lamp I've made is a simple wooden box with a clear lid, but this project could be adapted for any container, equally the LED strips could be used on their own as ambient lighting.

### Scheduling the On/Off and Warm/Bright timelines

The Sunlamp code contains two concurrent but independent timelines, one for **on/off** and one for **Warm/Bright**.

The time its takes for the lamp to fade on/off and to transition between Warm/Bright and back can also be configured.

From the balena dashboard the following variables can be set:

| Environment vairable | Description                                                                          | Options                                        | Default |
| -------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------- | ------- |
| LED_PIN_WARM         | Pin number on Raspberry Pi for Warm White LEDS                                       | Integer                                        | 17      |
| LED_PIN_BRIGHT       | Pin number on Raspberry Pi for Bright White LEDS                                     | Integer                                        | 13      |
| LAMP_ON_START        | Turns the lamp on over the fade duration                                             | Time formatted as HH:MM, using a 24hour clock. | 7:00    |
| LAMP_BRIGHT_START    | Transitions from Warm White to Bright White over the fade duration                   | Time formatted as HH:MM, using a 24hour clock. | 9:00    |
| LAMP_WARM_START      | Transitions from Bright White to Warm White over the fade duration                   | Time formatted as HH:MM, using a 24hour clock. | 16:00   |
| LAMP_OFF_START       | Turns the lamp off over the fade duration                                            | Time formatted as HH:MM, using a 24hour clock. | 20:00   |
| FADE_DURATION        | The time its takes for the lamp to fade on/off and to transition between Warm/Bright | Seconds                                        | 30      |

Please note:

- Currently the timelines need to be set so that the order aboves run chronologically
- Within the two timlines the start of one phase is automatically the end of the other, so LAMP_ON_END = LAMP_OFF_START, this ensures the timelines are complete and keeps the number of variables to a minimum.

**Currently Work In Progress**
