## Project Documentation 

### Requirements Outline 

#### The Need
The frequency of accidental fires in Australia has jumped in the past couple of years. Fires can start because of multiple reasons such as natural causes (bushfires from sunlight, lightning strikes and volcanic activity) but are mainly caused by human error (85-90%). Instances of neglect such as unattended cooking, overloaded powerstrips/excess electricity and poor management cause a plethora of fires annually.

#### Proposed Solution
We will design an alarm system that will be put next to stove tops that will ring a highly intense noise when the burner has been left unattended for more than 3 minutes. It will use heat sensors to check. The user can also press a button that, when pressed sets a timer for 5 minutes, lighting an LED that gets brighter the more the timer goes down. 

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

### Algorithms
**Flowchart:**
[Excalidraw Flowchart](https://excalidraw.com/#json=o52NDQPMBlxHZ63smCXED,PVgHCd79aU0KJ1tnWESsAA)

**Pseudocode:**
This is a simple prototype pseudocode:

**Main Routine:**

Set up the heat sensor, buttons, LED and buzzer

WHILE TRUE

  Check the heat sensor
  Run the Heat Detection subroutine

  Check if the timer button has been pressed
  Run the Timer subroutine

  Check if the end button has been pressed

  IF the end button is pressed THEN
    Turn off the buzzer
    Turn off the LED
    Reset the timer
     Reset the heat detection timer
  END IF

END WHILE

**Subroutine 1 :**

START Heat Detection

Read the heat sensor

IF a high temperature is detected THEN

 Start tracking how long the heat is detected

 IF the high temperature has been detected for 3 minutes THEN
    Turn on the buzzer
END IF

ELSE

 Reset the heat detection timer

END IF

RETURN

**Subroutine 2:**

START Timer

Check if the timer button has been pressed

IF the button is pressed THEN

  Add 5 minutes to the timer

  IF the timer is not already running THEN
    Start the timer
  END IF

END IF

**Subroutine 3:**


WHILE the timer is running

  Calculate the remaining time

  As the timer gets closer to finishing
    Increase the LED brightness

  IF the timer reaches zero THEN
    Turn on the buzzer
    Stop the timer
  END IF

END WHILE

### Testing and Debugging
#### Test case 1: Stove on for 3 minutes
| Input | Process | Output |
|-------|---------|--------|
|Heat sensor detects a high temperature continuously for 3 minutes |Program records when heat is first detected and continuously checks if temp remains above threshold|    An alarm rings after 3 minutes of continuous heat being detected

**Outline:** I used variables to store time when heat was first detected and compared to current time, also making sure the timer reset if the temp dropped below threshold before the 3 minutes

**Evaluation** 
The test/demo was successful because the program was able to detect a constant temp above the heat threshold (set to room temp for testing). I adjusted the threshold and timer values for the demo to make it quick and simple but still essentially be the same as the normal code.

#### Test case 2: Button is pressed twice
|Input|Process|Output|
|-----|-------|------|
|The button is pressed 2 times| The program detects 2 button presses and adds time accordingly| LED turns on dimly and the set timer is set

**Outline:** The button input needed to reliably detect individual presses. I needed to check the wiring and GPIO pins because the buttons were initially not being detected correctly. 

**Evaluation:** The test was successful once the button inputs and wiring were corrected as before the buttons weren't being detected. I extensively tested each button individually to see which GP pins were connected and if they were connected to GND or not. The most challenging part was identifying why the button presses were initially not detected and after testing I realised the fault was in my wiring. Overall, the program could be improved by adding some sort of code that prevents one press from being counted multiple times.


#### Test case 3: Stove is not on
|Input|Process|Output|
|-----|-------|------|
|Heat sensor does not detect any high temp| THe program checks the snsor value and determines the heat is below the threshold| Nothing happens and the LED and buzzer remain off |

**Outline:** The program needed to make sure the heat timer did not run when the stove was off. I added an else statement that resets the heat detected and start time to 0 when sensor reading is below threshold

**Evaluate** This test had no errors as the program remained inactive when the heat sensor did not detect a high enough value. I tried with various temps and tested if the timer went to 0 when the temp dropped. All tests were successful and stopped the buzzer from turning on. 


### PMI
Plus: What is good about the solution? Does it meet the need and requirements well? Does it function perfectly? Is the code efficient?

Minus: What leaves a bit to be desired? Does it perhaps not completely suit the need? Does it miss out on some test cases / requirements? Is the code inefficient / does it lack functions or data structures? Does the final product not completely function?

Implication: Look at the positive and negative points, then evaluate the implications of what you have learned from these for the person you are evaluating. How will this knowledge impact their final outcome / what improvements they may need to make?

**Kevin Zhu**

|   Plus    |   Minus   |   Implication |
|-----------|-----------|---------------|
|The circuitry functions properly, without any visible errors or misplaced wiring. In the end the program achieves its task (to detect heat at a constant temp for set time and output an alarm) with the use of a heat sensor, a few buttons, a led and a buzzer. | Demo was a bit too long, in the middle where nothing happened. | A way to improve this in the future is to add efficient code but overall the program works flawlessly


**Alfonso Delgado**
|   Plus    |   Minus   |   Implication |
|-----------|-----------|---------------|
|Nice clean code - sets up all the variables and needed Pins in a clear and orderly way. Has clear comments, explaining how each line of code functions. Works as intended. Smart use of space - using two circuit boards.  |Wires can maybe be organised a tad bit better. Buttons don't have a distinct way to identify them. |A way you can improve this is to make the buttons more distinct, such as maybe colour the end button, a red.

**Fayaaz Kabir**
|   Plus    |   Minus   |   Implication |
|-----------|-----------|---------------|
|The idea is really good, the actual execution also works and meets functional requirements.|The execution is somewhat confusing at some points, and having it be turned on and off manually doesn't seem like a good idea.|Overall, the idea and execution of the idea work well, with a few setbacks. The design appears to be a smaller demonstration of a much larger project, so the manual button ons and offs and the short times do make sense in this context.

**Aarav Rangi**
|   Plus    |   Minus   |   Implication |
|-----------|-----------|---------------|
|The program meets its main requirements and the heat sensor, LED and buzzer work together well. |Some parts of the code could be simpler and easier to understand. | Improving and simplifying the code could make the program easier to fix and improve later.



### Final Evaluations

**Evaluate your Final Test in Relation to Functional Criteria:**

Overall, my final product was successful at meeting most of the functional requirements that I idenitified at the beginning. The heat sensor was able to detect when the temp was above a chosen threshold and begin tracking how long that temp had been continuosly detected. After the requred amount of time (3mins) the buzzer would activate to alert the user. The timer button also worked by adding a certain time for every press, meaning multiple presses would stack the timer forcing an LED to gradually become brighter as the time decreased. The end button was able to stop the buzzer and essentially reset the main parts of the system. There were some minor issues I discovered during testing primarily with wiring and these were resolved through research about the pico and repeated testing. 

**Evaluate your Final Test in Relation to Non-Functional Criteria:**

The final product also satisfied a majority of the non-functional requriements. The heat sensor worked well and could repeatedly detect a change in temperature to give input to the program. I modified the heat threshold and timer values during testing so that I could demonstrate the program in less time but use the same logic as my final program. The buttons were a bit harder mainly beacuse of the wiring, and the LED successfully increased in brightness as the timer progressed, providing a visual indication of the remaining time. However, the button detection could still be improved by implementing a more reliable debouncing system rather than only using a short delay.


**Evaluate your Final Performance in Relation to the Identified Need:**

The need that this project was intended to address was the prevention of fires due to unattended cooking. My final prototype of the project fulfills this by detecting high temperatures and notifying the user by sounding an alarm once the temperature has been reached for a certain duration of time. The added timer system serves as a reminder of when the stove has been left unattended for too long. While the project is just a prototype and requires more development to be incorporated into an actual kitchen, it demonstrates the core idea of the proposed solution. The use of the temperature sensor along with the buzzer and the timer with an LED creates multiple reminders for the user. Therefore, I believe the project effectively addresses the identified need and shows how technology could potentially be used to reduce the risk of unattended cooking.

    **Evaluate your Project in Relation to Project Management:**

    Throughout the development there were MANY areas of managment. The structure given to help time management was rather helpful as it ensured that I stayed on track and had a way of checking if I was falling behind or not. There were 2 main components in the task, the circuitry and the code. I mostly did the code and Zachary helped with the circuitry, dividing the work between us. Although final circuit was assembled by me Zachary was a huge help. The code took a long time as it was confusing for me and I took multiple lessons understanding the components and how to code them. There were several challenges, particularly when wiring and testing the buttons, as they were initially not being detected by the program. To solve this, I tested the components individually, checked which GPIO pins they were connected to and adjusted the wiring where necessary.

    Overall the project management was decent, it could be further improved by having more layoff/time to test rather than cramming it in the last week. I could have tested the circuit sooner as this may have allowed the wiring issues to be identified sooner. Generally however, I was able to manage the problems that occurred and make changes to the program and circuit until the main features were working.

    **Evaluate your Project in Relation to Peer Feedback:**

    The peer feedback given was mainly positive and confirmed that the main features were all working properly. The feedback included that the program was effectively organized, the circuitry worked properly, and the combination of the heat sensor, LED, and buzzer were operating together successfully to fulfill the objective of the project. The use of comments and organised variables in the code was also identified as a positive aspect.

    However some peers suggested that the wiring could have been organised more neatly and the buttons should be easier to identify. The feedback was useful because it showed that while the functionality of the project was successful, there were still improvements that could make the final product more user-friendly.

    **Justify Future Improvements you could make to your Final Product:**

    If I were to continue developing this project, one of the main improvements I would make would be to improve the physical design of the circuit. The buttons could be labelled or given different colours so that the user can immediately identify which button starts the timer and which button stops the alarm. The wiring could also be organised more neatly to make the circuit easier to understand, troubleshoot and use.

    ### Bibliography 
    - [MicroPython Website](https://micropython.org/resources/docs/en/latest/index.html) Really helped me understand the heat sensor, PWM for led and buzzer, GPIO pins and buttons. Has a range of sub sections/different things to help with on website
    - [LED Fading help](https://randomnerdtutorials.com/raspberry-pi-pico-pwm-micropython/?utm_source=chatgpt.com) Helped me understand the LED fading and also provided the pin/GPIO diagram that helped in wiring.
    - [Raspberry Pico Pi tutorials](https://core-electronics.com.au/courses/raspberry-pi-pico-workshop/) - These helped me understand the code and wiring a little bit as well as explaining key details/functions
    - [Initial LED Source](https://techcraftandhacks.in/led-brighter-dimmer/) This was my original source to understand the LED as that was the part I was stuck on, at that time. Later on, I found out it was in c++ for arduino so I changed it.
    - Zachary used various other undocumented sources for the heat sensor and other parts