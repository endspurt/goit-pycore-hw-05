import re

def generator_numbers(text):
    # Use regular expressions to find all well-spaced numbers in the text
    for match in re.finditer(r'\b\d+\.\d+\b', text):
        yield float(match.group())  # Yield each number as a float

def sum_profit(text, func):
    # Sum all numbers generated by the generator function
    return sum(func(text))

# Example usage
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")