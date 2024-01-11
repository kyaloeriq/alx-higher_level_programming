#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Use del statement to delete the key
    del a_dictionary[key]
    return a_dictionary


def print_sorted_dictionary(new_dict):
    # Use sorted() function to print the dictionary
    sorted_dict = dict(sorted(new_dict.items()))
    print(sorted_dict)


if __name__ == "__main__":
    a_dictionary = {
            'language': "C", 'Number': 89, 'track': "Low",
            'ids': [1, 2, 3]
    }
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
