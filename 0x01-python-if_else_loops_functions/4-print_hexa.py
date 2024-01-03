#!/usr/bin/python3
# a string of numbers from 0-98
numbers = ''.join([str(m) for m in range(0, 99)])
# a string of hexadecimal from a-f
hexdec = ''.join([hex(m)[2:] for m in range(ord('a'), ord('f') + 1)])
# printing of the concatenated result of numbers and hexdec
print("{}{}".format(numbers, hexdec))
