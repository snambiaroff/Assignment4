def swap_first_two_chars(string):

    first_char = string[0]
    second_char = string[1]
    new_string = second_char + first_char + string[2:]
    return new_string


def combine_strings(string1, string2):

    combined_string = string1 + " " + string2
    return combined_string


string1 = "abc"
