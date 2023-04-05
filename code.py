from machine import Pin
from time import sleep

motion = False
def handle_interrupt(pin):
    global motion
    motion = True
    global interrupt_pin
    interrupt_pin = pin

pir = Pin(13, Pin.IN)
pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
while True:
  if motion:
    print('MOTION DETECTED')
    sleep(5)
    print('MOTION STOPPED')
    motion = False