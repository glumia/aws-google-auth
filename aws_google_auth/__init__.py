#!/usr/bin/env python

__version__ = "0.0.37"

# HTTP request timeouts (in seconds).
# 3s is the default TCP retransmission window, that's why we use values slightly larger
# than multiples of 3.
CONNECT_TIMEOUT = 3.05
READ_TIMEOUT = 9.05
