from machine import Pin, ADC, PWM
import time

heat_line = 40000


heat_detected = 0
heat_start_time = 0
timer_active = 0  #if not active 0 if active then 1
total_timer = 0  #total time left on timer even after stacking
timer_start = 0
buzzer = 0
auto_alarm_limit = 300

#main program
heat_sensor = ADC(Pin(26)) 
timer_button = Pin(14, Pin.IN, Pin.PULL_UP)
end_button = Pin(15, Pin.IN, Pin.PULL_UP)

buzzer = PWM(Pin(20))
buzzer.freq(2000)
buzzer.duty_u16(0)
led = PWM(Pin(16))

while True:
    current_time = time.time()
    sensor_reading = heat_sensor.read()
    timer_pressed = timer_button.value() #checks how many times it is pressed

    if sensor_reading > heat_line:   #if the reading is more than 100 degrees it starts a timer for 3 minutes
        if heat_detected == 0:
            heat_detected = 1
            heat_start_time = current_time
        if current_time - heat_start_time >= auto_alarm_limit:   # Once it has been more than 3 minutes the buzzer turns on
            buzzer.duty_u16(32768)
        
    else: 
       heat_detected = 0
       heat_start_time = 0
    

    if timer_pressed == 0:

        total_timer = total_timer + 300    #Adds 5 mins to the timer

        if timer_active == 0:  #If the timer is off currently
            timer_active = 1   #Turn the timer on
            timer_start = current_time  #Saves when the time started

        time.sleep(0.3)   #small delay

    if timer_active == 1:
        tp = current_time - timer_start   #Time passed
        time_left = total_timer - tp
        if time_left <= 0:
            buzzer.duty_u16(32768)
            timer_active = 0   # timer turns off as its finished
            total_timer = 0   # resets total timer


#led brightness
    if timer_active == 1:
        if time_left > 240:
            led.duty_u16(10000)
        elif time_left > 180:
           led.duty_u16(20000)
        elif time_left > 120:
            led.duty_u16(30000)
        elif time_left > 60:
            led.duty_u16(45000)
        else:
           led.duty_u16(65535)

# End BUtton
    if end_button.value() == 0:
        buzzer.duty_u16(0)
        led.duty_u16(0)
        timer_active = 0
        total_timer = 0
        heat_detected = 0
        heat_start_time = 0
        time.sleep(0.5)

    time.sleep(0.01)   #so pico doesnt overheat quickly
