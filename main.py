from machine import Pin, ADC, PWM
import time

heat_line = 100


heat_detected = 0
heat_start_time = 0
timer_active = 0  #if not active 0 if active then 1
total_timer = 0  #total time left on timer even after stacking
timer_start = 0
buzzer = 0
auto_alarm_limit = 300

#main program
heat_sensor = ADC(Pin(26)) 
timer_button = Pin(14, Pin.IN, Pin.PULL_DOWN)
end_button = Pin(15, Pin.IN, Pin.PULL_DOWN)

buzzer = Pin(20, Pin.OUT)
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
         buzzer.value(1)
      else: 
       heat_detected = 0
       heat_start_time = 0
    else: 
       buzzer.value(0)

    if timer_pressed:

        total_timer = total_timer + 300

        if timer_active == 0:
            timer_active = 1
            timer_start = current_time

        time.sleep(0.3)

# All that is left is end button and working on timer function

#led brightness
    if timer_active == 1:
        if total_timer > 240:
            led.duty_u16(10000)
        elif total_timer > 180:
           led.duty_u16(20000)
        elif total_timer > 120:
            led.duty_u16(30000)
        elif total_timer > 60:
            led.duty_u16(45000)
        else:
           led.duty_u16(65000)