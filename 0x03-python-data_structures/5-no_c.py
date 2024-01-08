#!/usr/bin/python3
def no_c(my_string):
    no_c_string = ''.join([char for char in my_string if char.lower() != 'c'])
    return no_c_string


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
