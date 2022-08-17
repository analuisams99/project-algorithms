def letter_count(word):
    letter_dict = dict()

    for letter in word.lower():
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    return letter_dict


def is_anagram(first_string, second_string):
    first = letter_count(first_string)
    second = letter_count(second_string)

    return True if first == second else False
