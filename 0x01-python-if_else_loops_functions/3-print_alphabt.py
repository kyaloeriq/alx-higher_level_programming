#!/usr/bin/python3
alpbet = ''.join([chr(m) for m in range(ord('a'), ord('z') + 1)])
filteredalpbet = ''
for letter in alpbet:
    if letter not in ('q', 'e'):
        filteredalpbet += letter
print("{}".format(filteredalpbet), end='')
