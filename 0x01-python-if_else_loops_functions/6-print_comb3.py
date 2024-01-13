#!/usr/bin/python3
# prints all possible combinations of two digits
for m in range(10):
    for n in range(m + 1, 10):
        if m == 8 and n == 9:
            print("{:01d}{:01d}".format(m, n), end='')
        else:
            print("{:01d}{:01d}, ".format(m, n), end='')
print()
