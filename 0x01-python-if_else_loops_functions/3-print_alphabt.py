#!/usr/bin/python3
alpbet = ''.join([chr(m) for m in range(ord('a'), ord('z') + 1)])
filteredalpbet = ''.join(
        [letter for letter in alpbet if letter not in ('q', 'e')]
)
print("{}".format(filteredalpbet), end='')
