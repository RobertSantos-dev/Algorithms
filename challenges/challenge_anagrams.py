def letter_modifier(letters, first, last):
    at = letters[last]
    limit = first - 1

    for i in range(first, last):
        if letters[i] <= at:
            limit = limit + 1
            letters[i], letters[limit] = letters[limit], letters[i]
    letters[limit + 1], letters[last] = letters[last], letters[limit + 1]
    return limit + 1


def word_ordering(word_list, first, last):
    if first < last:
        letter = letter_modifier(word_list, first, last)
        word_ordering(word_list, letter + 1, last)
        word_ordering(word_list, first, letter - 1)


def str_for_list(string):
    return [string[i] for i in range(len(string))]


def list_for_str(list_str):
    string = ''
    for i in list_str:
        string += i
    return string


def is_anagram(first_string, second_string):
    if (not first_string and not second_string):
        return ('', '', False)

    word_one = str_for_list(first_string.lower())
    word_two = str_for_list(second_string.lower())

    word_ordering(word_one, 0, len(first_string) - 1)
    word_ordering(word_two, 0, len(second_string) - 1)
    return (
        list_for_str(word_one),
        list_for_str(word_two),
        list_for_str(word_one) == list_for_str(word_two)
    )
