import time
from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()

print("Prepare GPIO pins")
# register the sensors and map to Raspberry Pi pins
sensor_left = DistanceSensor(echo=17, trigger=27, queue_len=2, pin_factory=factory)
sensor_right = DistanceSensor(echo=5, trigger=6, queue_len=2, pin_factory=factory)

# print out distance to sensor
while True:
    print(f'Left: {sensor_left.distance * 100:.3f}, Right: {sensor_right.distance * 100:.3f}')
    # force pause to avoid flooding output
    time.sleep(0.1)

