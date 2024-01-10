#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                common_set.add(i)
    return common_set


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
