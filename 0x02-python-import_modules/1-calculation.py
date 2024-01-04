#!/usr/bin/python3
import calculator_1 as my_module


def main():
    a = 10
    b = 5

    rslt_add = my_module.add(a, b)
    rslt_sub = my_module.sub(a, b)
    rslt_mul = my_module.mul(a, b)
    rslt_div = my_module.div(a, b)

    print(f"{a} + {b} = {rslt_add}")
    print(f"{a} - {b} = {rslt_sub}")
    print(f"{a} * {b} = {rslt_mul}")
    print(f"{a} / {b} = {rslt_div}")


if __name__ == "__main__":
    main()
