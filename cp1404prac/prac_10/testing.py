"""
Author: Feng Yuan
Date: 2023-09-22
Time to Complete: 30 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/master/cp1404prac

Pseudo-code:
1. Define repeat_string function to repeat a string with spaces in between.
2. Define is_long_word function to check if a word's length is greater or equal to a given length.
3. Define format_sentence function to format a phrase as a sentence.
4. Define run_tests function to test the above functions and the Car class methods.
5. Import doctest to check if the code passes the doctests.
6. Call run_tests function.
7. Call doctest.testmod() to execute doctests in the code.

"""

import doctest
from cp1404prac.prac_09.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('the quick brown fox')
    'The quick brown fox.'
    """
    formatted_phrase = phrase.capitalize()
    if not formatted_phrase.endswith('.'):
        formatted_phrase += '.'
    return formatted_phrase


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car1 = Car()
    assert test_car1.fuel == 0, "Car does not set fuel correctly with default value"

    test_car2 = Car(fuel=10)
    assert test_car2.fuel == 10, "Car does not set fuel correctly with given value"


run_tests()
doctest.testmod()
