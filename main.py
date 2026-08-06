from machine import Pin, ADC
import time



#main program
heat_sensor = ADC(Pin(26)) 
buzzer = Pin(20, Pin.out)
led = Pin(16, Pin.out)







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