#!/usr/bin/python3
# generate the alphabet and filter out e and q
def print_alphabt():
    print("{}".format(
        ''.join(chr(char) for char in range(ord('a'), ord('z') + 1)
                if chr(char) != 'e' and chr(char) != 'q')
    ), end='')


print_alphabt()
