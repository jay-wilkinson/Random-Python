#!/usr/bin/python3
# Random 39 Hex Digit Generator  
from random import randint
b = 21267647932558653966460912964485513216
e = 340282366920938463463374607431768211455
l = 39
for i in range(0, 10):
    x = hex(randint(b, e))
    print(i, ':', x)

# print(int(0x10000000000000000000000000000000))
# print(int(0x9c0e735bb59145ef94b3df99a5f92d29))
# print(int(0xffffffffffffffffffffffffffffffff))
