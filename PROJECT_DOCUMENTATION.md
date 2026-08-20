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

### PMI
Plus: What is good about the solution? Does it meet the need and requirements well? Does it function perfectly? Is the code efficient?

Minus: What leaves a bit to be desired? Does it perhaps not completely suit the need? Does it miss out on some test cases / requirements? Is the code inefficient / does it lack functions or data structures? Does the final product not completely function?

Implication: Look at the positive and negative points, then evaluate the implications of what you have learned from these for the person you are evaluating. How will this knowledge impact their final outcome / what improvements they may need to make?

Kevin Zhu
Plus - The circuitry functions properly, without any visible errors or misplaced wiring. In the end the program achieves its task (to detect heat at a constant temp for set time and output an alarm) with the use of a heat sensor, a few buttons, a led and a buzzer.
Minus - Demo was a bit too long, in the middle where nothing happened. 
Implication - A way to improve this in the future is to add efficient code but overall the program works flawlessly

Alfonso Delgado
Plus - Nice clean code - sets up all the variables and needed Pins in a clear and orderly way. Has clear comments, explaining how each line of code functions. Works as intended. Smart use of space - using two circuit boards. 
Minus - Wires can maybe be organised a tad bit better. Buttons don't have a distinct way to identify them.
Implication - A way you can improve this is to make the buttons more distinct, such as maybe colour the end button, a red.

Fayaaz Kabir
Plus - The idea is really good, the actual execution also works and meets functional requirements.
Minus - The execution is somewhat confusing at some points, and having it be turned on and off manually doesn't seem like a good idea.
Implication - Overall, the idea and execution of the idea work well, with a few setbacks. The design appears to be a smaller demonstration of a much larger project, so the manual button ons and offs and the short times do make sense in this context.
### Final Evaluations

Evaluate your Final Test in Relation to Functional Criteria

Evaluate your Final Test in Relation to Non-Functional Criteria

Evaluate your Final Performance in Relation to the Identified Need

Evaluate your Project in Relation to Project Management

Evaluate your Project in Relation to Peer Feedback.

Justify Future Improvements you could make to your Final Product

