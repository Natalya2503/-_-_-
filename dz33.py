# def is_even(number: int) -> bool:
"""
Проверяет, является ли число четным.

    :param number: Проверяемое число
    :return: True, если число четное, иначе False
    """
    # return number % 2 == 0
import pytest

def is_even(number: int) -> bool:
    return number % 2 == 0

def test_is_even_base():
    expected_result = 10
    actual_result = is_even(10)
    assert actual_result == expected_result

def test_is_even_negative_number():
    expected_result = -2
    actual_result = is_even(-2)
    assert actual_result == expected_result

def test_is_even_type_number():
    expected_result = 5.5
    actual_result = is_even(5.5)
    assert actual_result == expected_result

def test_is_even_odd_number():
    expected_result = 7
    actual_result = is_even(7)
    assert actual_result == expected_result
    
    

