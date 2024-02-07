from typing import Callable

text = "Мій дохід у січні був 1000.50, у лютому - 1500.75, а в березні - 2000.25"

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    total_profit = sum(func(text))
    return total_profit

# # Приклад використання:
# text = "Мій дохід у січні був 1000.50, у лютому - 1500.75, а в березні - 2000.25"
# total_profit = sum_profit(text, generator_numbers)
print("Загальний прибуток:", {total_profit})