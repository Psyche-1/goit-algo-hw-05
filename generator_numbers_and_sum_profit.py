from typing import Callable
import re

def generator_numbers(text: str):
    """Function that get text, find float numbers and return it as a generator"""
    pattern = r' \d+\.\d+'

    matches = re.findall(pattern, text)

    for i in matches:
        yield i

def sum_profit(text: str, func: Callable[[str], str]) -> float:
    """Function that return sum of numbers get from other function"""
    return sum(float(i) for i in func(text))



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
