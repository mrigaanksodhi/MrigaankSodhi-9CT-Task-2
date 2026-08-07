from machine import Pin, ADC, PWM
import time

heat_line = 100


heat_detected = 0
heat_start_time = 0
timer_active = 0  #if not active 0 if active then 1
total_timer = 0  #total time left on timer even after stacking
buzzer = 0
auto_alarm_limit = 300

#main program
heat_sensor = ADC(Pin(26)) 
timer_button = ADC(Pin(14))
end_button = ADC(Pin(16))

buzzer = Pin(20, Pin.out)
led = Pin(16, Pin.out)

while True:
    current_time = time.time()
    sensor_reading = heat_sensor.read()
    timer_pressed = timer_button.value() #checks how many times it is pressed

    if sensor_reading > heat_line:   #if the reading is more than 100 degrees it starts a timer for 3 minutes
      heat_detected = 1
      heat_start_time = current_time
    if current_time - heat_start_time >= auto_alarm_limit:   # Once it has been more than 3 minutes the buzzer turns on
         buzzer.value(1)
    else: 
       buzzer(0)
    if timer_pressed:
      if timer_active == 0:

      




            #def start_timer(seconds):  Method 1
                #while seconds >= 0:
                    #seconds = seconds - 1
                    #time.sleep(1)
while time <= 300:   # Method 2
    time = time + 1
    time.sleep(1)
    if time == 300:
     print ('hello') #testing if it works

# Automatic alarm function







#timer set to 5 minutes function
    #timer = 5 minutes (find out how to add)






#stacking the 5 minutes function

#led brightness
    #LED value.0 slowly goes up
    
    int brightness = 0    #Sets initial brightness to 0 and goes upto 255
    int fadeAmount = 1    #Goes up by 1 each time
    void setup() {
        pinMode(ledPin, OUTPUT);
    }
    void loop() {
        brightness = brightness + fadeAmount; #changes the brightness
    }
    if brightness == 255:   #When brightness maxed it stops fade amount:
        fadeAmount = 0
    if timer == 0:          #When timer stops brightness auto maxes
        brightness = 255