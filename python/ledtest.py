# -*- coding: utf-8 -*-
# Copyright (c) 2018 Steven P. Goldsmith
# See LICENSE.md for details.

"""
Simple LED blink
-------------
Using the NanoPi Duo connect a 220Ω resistor to the anode (the long pin of
the LED), then the resistor to 3.3 V, and connect the cathode (the short
pin) of the LED to pin 12 (IOG11). The anode of LED connects to a
current-limiting resistor and then to 3.3V. Therefore, to turn on an LED,
we need to make pin 12 low (0V) level. It can be realized by programming.
See images/ledtest.jpg for schematic.

Note: Only Swig wrapper is used here since no callbacks are used and there
is no need for ctypes.
"""


import time
from armbianio.armbianio import *

# Detect SBC
rc = AIOInit()
if rc == 1:
    pin = 12
    # Pin 12 set to output
    AIOAddGPIO(pin, GPIO_OUT)
    AIOWriteGPIO(pin, 0)
    time.sleep(3)
    AIOWriteGPIO(pin, 1)
    AIOShutdown()
else:
    print "AIOInit error"