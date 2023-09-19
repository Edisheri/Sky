<<<<<<< HEAD
def uppercase_first_letters(input_str):
    """
    Converts the first letter of each word in input string to uppercase.
    :param input_str: str value to convert the first letter of each word to uppercase
    :return: str value of input_str with the first letter of each word in uppercase
    """
    return ' '.join(word.capitalize() for word in input_str.split())
=======
def uppercase_str(input_str):
    """
    Converts the input string to uppercase.
    :param input_str: str value to convert to uppercase
    :return: str value of input_str in uppercase
    """
    return input_str.upper()
>>>>>>> a22199e19ac03711172e06fde2acc82cb86859d4
