from string import ascii_lowercase, ascii_uppercase
from .errors.NonPositiveRotationError import NonPositiveRotationError


def caesar_cypher(string, rotation_key):
    cyphered_string = ''
    for c in string:
        cyphered_string += get_char_caesar_cypher(c, rotation_key)
    return cyphered_string


def get_char_caesar_cypher(char, rotation_key):
    if (type(rotation_key) is not int) or rotation_key <= 0:
        raise NonPositiveRotationError("Rotation key must be positive.")
    if char in ascii_lowercase:
        return ascii_lowercase[(ascii_lowercase.index(char) + rotation_key) % len(ascii_lowercase)]
    elif char in ascii_uppercase:
        return ascii_uppercase[(ascii_uppercase.index(char) + rotation_key) % len(ascii_uppercase)]
    return char
