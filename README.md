# MrigaankSodhi-9CT-Task-2
## Fire/Stove safety alarm

### Overview
This project is a stove safety alarm which prevents the hazards that can occur when leaving a stove unattended. It has a heat sensor that detects the stove's temperature.If the stove remains hot for the set time, an alarm sounds to alert the user.
The user can also manually start a timer by pressing a button. Each press adds 5 minutes to the timer, allowing the user to stack multiple 5-minute periods. An LED becomes brighter as the timer gets closer to finishing, and a buzzer sounds when the timer reaches zero.

### Components Used
- Raspberry Pi Pico
- Heat Sensor 
- 2 push buttons
- LED/Light globe
- Buzzer
- 2 Breadboards
- Jumper wires

### How the Program works
1. The program continuously reads the heat sensor.
2. If a high temperature is detected, the program starts tracking the amount of time that heat is present.
3. If the high temperature continues for the set amount of time, the buzzer turns on.
4. Pressing the timer button adds 5 minutes to the timer.
5. Pressing the timer button multiple times adds additional 5 minute periods.
6. While the timer is active, the LED gradually becomes brighter.
7. When the timer reaches zero, the buzzer sounds.
8. Pressing the end button turns off the buzzer and LED and resets the timer.
