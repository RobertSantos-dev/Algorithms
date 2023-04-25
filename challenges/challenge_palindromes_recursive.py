def is_palindrome_recursive(word, low_index, high_index):
    try:
        if (high_index < low_index and word != ''):
            return True
        if (word[low_index] == word[high_index]):
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False

    except IndexError:
        return False
