#!/usr/bin/python3
def islower(c):
    for char in range(ord('a'), ord('z') + 1):
        if c == chr(char):
            return True
    return False


if __name__ == "__main__":
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))
