import RPi.GPIO as GPIO      # using RPi.GPIO module
from time import sleep       # import function sleep for delay
GPIO.setmode(GPIO.BCM)       # GPIO numbering
GPIO.setwarnings(False)      # enable warning from GPIO
AN2 = 25                     # set pwm2 pin on MDDS10 to GPIO 25
AN1 = 24                     # set pwm1 pin on MDDS10 to GPIO 24
DIG2 = 23                    # set dir2 pin on MDDS10 to GPIO 23
DIG1 = 18                    # set dir1 pin on MDDS10 to GPIO 18
GPIO.setup(AN2, GPIO.OUT)    # set pin as output
GPIO.setup(AN1, GPIO.OUT)    # set pin as output
GPIO.setup(DIG2, GPIO.OUT)   # set pin as output
GPIO.setup(DIG1, GPIO.OUT)   # set pin as output
sleep(1)                     # delay for 1 seconds
p1 = GPIO.PWM(AN1, 100)      # set pwm for M1
p2 = GPIO.PWM(AN2, 100)      # set pwm for M2
