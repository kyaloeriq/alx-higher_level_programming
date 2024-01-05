#!/usr/bin/python3
# generate the alphabet and filter out e and q
filteredalpbet = ''.join([
    char for char in (chr(m) for m in range(ord('a'), ord('z') + 1))
    if char not in ('q', 'e')])

print("{}".format(filteredalpbet), end='')
