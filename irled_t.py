from gpiozero import PWMLED
from picamzero import Camera
from time import sleep
import os
from datetime import datetime


home_dir = os.environ['HOME'] #set the location of your home directory
led = PWMLED(13)
cam = Camera()

def take_IR_photo(filename):
    led.value = 1
    cam.take_photo(filename) #save the image to your desktop
    led.value = 0

try: 
    while True:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(home_dir, f"photo_{timestamp}.jpg")
        take_IR_photo(filename)
        print(f"Photo taken: {filename}")
        sleep(1)


except KeyboardInterrupt:
    print("Program terminated by user.")
    led.close() # Cleanly close the led connection
    cam.close() # Cleanly close the camera connection

except Exception as e:
    print(f"An error occurred: {e}")
    led.close()
    cam.close()