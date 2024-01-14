#!/usr/bin/python3
# prints string in uppercase followed by a new line
def uppercase(str_input):
    rslt_str = ''
    for char in str_input:
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase
            rslt_str += chr(ord(char) - ord('a') + ord('A'))
        else:
            # Keep non-alphabetic characters unchanged
            rslt_str += char
    print("{}".format(rslt_str))


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
