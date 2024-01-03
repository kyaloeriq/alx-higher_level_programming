#!/usr/bin/python3
betalp = ''.join([
    chr(m) if m % 2 == 0 else chr(m - 32)
    for m in range(ord('z'), ord('a') - 1, -1)
])
print("{}".format(betalp), end='')
