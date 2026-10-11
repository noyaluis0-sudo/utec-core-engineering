#!/usr/bin/env python3
for number in range(100):
    print("{:02d}".format(number), end="\n" if number == 99 else ", ")
