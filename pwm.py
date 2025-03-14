    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    pwm = GPIO.PWM(18, 50000)  # 5 kHz frequency
    pwm.start(50)  # Start with 50% duty cycle
    time.sleep(30)
    pwm.stop()
    GPIO.cleanup()