import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pinList = [4, 17, 27, 22]

engine1F = 4
engine1B = 17
engine2F = 27
engine2B = 22

# loop through pins and set mode and state to 'high'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

print "Going Forward Engine 1 and 2"
GPIO.output(engine1F, GPIO.HIGH) 
GPIO.output(engine2F, GPIO.HIGH)
sleep(2)
GPIO.output(engine1F, GPIO.LOW)
GPIO.output(engine2F, GPIO.LOW)
print "Stopped"
sleep(2)

print "Going Backward Engine 1 and 2"
GPIO.output(engine1B, GPIO.HIGH)
GPIO.output(engine2B, GPIO.HIGH)
sleep(2)
GPIO.output(engine1B, GPIO.LOW)
GPIO.output(engine2B, GPIO.LOW)
print "Stopped" 
print "Stopping motor"
GPIO.cleanup()
