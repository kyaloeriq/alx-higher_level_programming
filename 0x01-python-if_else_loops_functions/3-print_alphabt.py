#!/usr/bin/python3
alpbet = ''.join([chr(m) for m in range(ord('a'), ord('z') + 1)])
# initialize an empty string to store the filtered alphabet
filteredalpbet = ''
for letter in alpbet:
    if letter != 'q' and letter != 'e':
        filteredalpbet += letter
print("{}".format(filteredalpbet), end='')
