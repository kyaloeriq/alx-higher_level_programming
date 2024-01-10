#!/usr/bin/python3
def number_keys(a_dictionary):
    dic_l = list(a_dictionary)
    return len(dic_l)


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
