from gpiozero import PWMOutputDevice
from picamera2 import Picamera2
from time import sleep
import os
from datetime import datetime
import RPi.GPIO as GPIO #needed for hardware pwm, and cleanup

home_dir = os.environ['HOME']
pwm_pin = 13 # Choose a PWM pin
frequency = 100 #PWM frequency
cam = Picamera2()
cam.configure(cam.create_still_configuration())

GPIO.setmode(GPIO.BCM) #needed for hardware pwm cleanup.
GPIO.setup(pwm_pin, GPIO.OUT) #needed for hardware pwm cleanup.

pwm = GPIO.PWM(pwm_pin, frequency) #hardware pwm
pwm.start(0)

def take_photo_with_pwm_pulse(filename, pulse_duration=0.1): #pulse duration in seconds
    """Takes a photo and pulses the PWM during the shutter period."""
    pwm.ChangeDutyCycle(100) # Full duty cycle
    sleep(pulse_duration) #simulate shutter time
    cam.start_and_capture_file(filename)
    pwm.ChangeDutyCycle(0) # Turn off PWM

try:
    while True:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(home_dir, f"photo_{timestamp}.jpg")
        take_photo_with_pwm_pulse(filename)
        print(f"Photo taken: {filename}")
        sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")
    pwm.stop()
    GPIO.cleanup() #cleanup hardware pwm
    cam.close()

except Exception as e:
    print(f"An error occurred: {e}")
    pwm.stop()
    GPIO.cleanup()
    cam.close()