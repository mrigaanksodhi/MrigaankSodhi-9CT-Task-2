## Project Documentation 

### Requirements Outline 

#### The Need
The frequency of accidental fires in Australia has jumped in the past couple of years. Fires can start because of multiple reasons such as natural causes (bushfires from sunlight, lightning strikes and volcanic activity) but are mainly caused by human error (85-90%). Instances of neglect such as unattended cooking, overloaded powerstrips/excess electricity and poor management cause a plethora of fires annually.

#### Proposed Solution
We will design a alarm system that will be put next to stove tops that will ring a highly intense noise when the burner has been left unattended for more than 3 minutes. It will use heat sensors to check. The user can also press a button that, when pressed sets a timer for 5 minutes, lighting an LED that gets brighter the more the timer goes down. 

#### Key Actions
-  **Automatic Alarm:**  After 3 minutes unattended an automatic intense buzzer will ring 
- **Timer:** There will be a button that if clicked starts a 5 minute timer to leave stove 
- **Stack Button** If the button is pressed multiple times each click stacks 5 minutes
- **LED Brightness Timer:** As time goes on the LED will get brighter and it reaches peak brightness at the end of the set time
- **Alarm:** There will be another intense buzzer at the end of the timer reminding users to not forget about their stove
- **End Button:** Once sounded the alarm will not turn off unless user clicks clicks a button

#### Functional Requirements 
- **Automatic Alarm:** If the sensor detects a stable high temperature for 3 minutes, at the end of which a buzzer will ring continuously.
- **Timer:** When clicked, program must start a timer that lasts 5 minutes
- **Stack Button:** When clicked multiple times program stacks the 5 minutes
- **LED Brightness Timer:** LED must light up when button clicked then increase in brightness over the 5 minutes
- **Alarm:** If the 5 minutes is up a buzzer will ring continuously 
- **End Button:** Once clicked the buzzer ringing will stop and light will turn off


#### Test Cases

| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|     Stove on for 3 minutes  |   Heat sensor detects high temperature                |High pitched alarm rings
| Button is pressed twice          | Button presses are detected          | LED turns on (dim) and 10 minute timer is set               | 
| Stove is not on         | Heat sensors dont detect anything           | Nothing happens, no LED turns on                  |

#### Non-Functional requrements
- Heat sensors - Should consistently detect heat input every once per second
- Buttons - Should always turn off and on timer with additional clicks stacking time
- LED - Should always go from dim to bright in the duration that the timer is on
- 

