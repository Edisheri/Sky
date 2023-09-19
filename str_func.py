def uppercase_first_letters(input_str):
    """
    Converts the first letter of each word in input string to uppercase.
    :param input_str: str value to convert the first letter of each word to uppercase
    :return: str value of input_str with the first letter of each word in uppercase
    """
    return ' '.join(word.capitalize() for word in input_str.split())
