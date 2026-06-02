from machine import Pin
import time

col_pins = [
    Pin(3, Pin.IN, Pin.PULL_UP),
    Pin(9, Pin.IN, Pin.PULL_UP),
    Pin(20, Pin.IN, Pin.PULL_UP)]

row_pins = [
    Pin(6, Pin.OUT),
    Pin(4, Pin.OUT),
    Pin(10,Pin.OUT)]

KEYS = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

for r in row_pins:
    r.value(1)
    
def scan():
    for x,r in enumerate(row_pins):
        r.value(0)
    
        for y, c in enumerate(col_pins):
            if c.value() == 0:
                r.value(1)
                return KEYS[x][y]
        
        r.value(1)
        
    return None

last = None
while True:
    key = scan()
    if key != last:
        if key is not None:
            print(key)
        last = key
    time.sleep(0.03)