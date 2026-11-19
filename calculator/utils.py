import re

NUM_OR_DOT_REGEX = re.compile(r"^[0-9.]$")


def convertToNumber(value):
    number = float(value)

    if number.is_integer():
        number = int(number)

    return number


def IsNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))


def IsValidNumber(string: str):
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False

    return valid


def IsEmpty(string: str):
    return len(string) == 0
