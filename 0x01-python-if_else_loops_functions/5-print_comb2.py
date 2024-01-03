#!/usr/bin/python3
# printing numbers from 0-99
for m in range(100):
    if m < 99:
        print("{:02d}, ".format(m), end='')
    else:
        print("{:02d}".format(m))
