#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """
    prints a text with 2 new lines after characters: ., ? and :
    text must be a string, otherwise TypeError exception is raised
    There should'nt be space at beginning or end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = (".", "?", ":")
    previous_char = ''
    for char in text:
        if char != ' ' or (char == ' ' and previous_char != ' '):
            print(char, end='')
        if char in punctuations:
            print("\n\n", end='')
        previous_char = char


if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")
