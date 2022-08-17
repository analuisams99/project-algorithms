def is_palindrome_iterative(word):
    try:
        return word != '' and word == word[::-1]

    except TypeError:
        return False
