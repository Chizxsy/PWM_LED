from gpiozero import PWMLED
from picamera2 import Picamera2
from time import sleep
import os
from datetime import datetime

home_dir = os.environ['HOME']
led = PWMLED(13)
cam = Picamera2()
cam.configure(cam.create_still_configuration()) # Configure for still image capture

def take_photo_with_led_pulse(filename):
    """Takes a photo and pulses the LED during the shutter period."""
    led.value = 1  # Turn LED on at full brightness (start of shutter)
    cam.start_and_capture_file(filename)
    led.value = 0  # Turn LED off (end of shutter)

try:
    while True:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(home_dir, f"photo_{timestamp}.jpg")
        take_photo_with_led_pulse(filename)
        print(f"Photo taken: {filename}")
        sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    print("Program terminated by user.")
    led.close()
    cam.close()

except Exception as e:
    print(f"An error occurred: {e}")
    led.close()
    cam.close()