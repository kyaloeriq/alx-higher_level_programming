#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
    language that combines remarkable power with very clear syntax"
print(open(__file__).readlines()[1].split('"')[1][39:66], "with Python")
# print(str)
