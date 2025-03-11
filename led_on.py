import RPi.GPIO as GPIO
from picamera2 import Picamera2, Preview
import time


pwm_pin = 12 # PWM0 is pin BCM 12
pwm_freq = 50000 #PWM frequency - To minimize this ripple, the suggested PWM signal frequency is 10 kHz or higher, such as 50 kHz
dutycycle = 60

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(pwm_pin,GPIO.OUT)

picam2 = Picamera2()

pi_pwm = GPIO.PWM(pwm_pin,pwm_freq)		#create PWM instance with frequency
pi_pwm.start(0)	


pi_pwm.ChangeDutyCycle(dutycycle)

picam2.start_preview(Preview.QTGL) # or Preview.QT
picam2.start()
time.sleep(10)  # Preview for 5 seconds
picam2.stop_preview()
picam2.stop()