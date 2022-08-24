import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#GPIO4 is set for output of control pulse.
gp_out = 4
GPIO.setup(gp_out, GPIO.OUT)

#Make PWM instance with 'GPIO4 output'
#GPIO.PWM([pin_number],[frequency_Hz])
#SG92R is PWM_cycle:20ms(=50Hz), control_pulse:0.5ms~2.4ms(=2.5%~12%).
servo = GPIO.PWM(gp_out, 50)

#Start of pulse output. sevo.start([duty cycle 0~100%])
servo.start(0)
#time.sleep(1)

for i in range(3):
	#turn servo to control angle with changing the value of duty cycle.
	servo.ChangeDutyCycle(2.5)
	time.sleep(0.5)
	
	servo.ChangeDutyCycle(7.25)
	time.sleep(0.5)
	
	servo.ChangeDutyCycle(12)
	time.sleep(0.5)
	
	servo.ChangeDutyCycle(7.25)
	time.sleep(0.5)

servo.stop()
GPIO.cleanup()