#!/usr/bin/python

from Raspi_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x6F, debug=True)

servoMin = 200  # Min pulse length out of 4096
servoMax = 400  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 50                       # 60 Hz
  print("%d us per period" % pulseLength)
  pulseLength /= 4096                     # 12 bits of resolution
  print("%d us per bit" % pulseLength)
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(50)                        # Set frequency to 60 Hz
while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWM(1, 0, servoMin)
#  pwm.setPWM(0, 0, servoMin)
  time.sleep(1)
  pwm.setPWM(1, 0, servoMax)
#  pwm.setPWM(0, 0, servoMax)
  time.sleep(1)


