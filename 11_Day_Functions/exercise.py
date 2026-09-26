# Level 1
# 1
def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(3, 5))

#2
def area_of_circle(radius):
    pi = 3.14
    return pi * radius * radius

print(area_of_circle(5))

#3
def add_all_nums(*args):
    for num in args:
        if not isinstance(num, (int,float)):
            raise ValueError(f"{num!r} is not a number")
    
    total = 0
    for num in args:
        total += num
    return total

print(add_all_nums(1, 2, 3, 4.5, 5))

#4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(convert_celsius_to_fahrenheit(0))

#5
def check_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    else:
        raise ValueError(f"{month!r} is not a valid month")

print(check_season('December'))

#6
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        raise ValueError("Slope is undefined for vertical lines")
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(1, 2, 3, 4))

#7
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("No real roots")
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    return root1, root2

print(solve_quadratic(1, -5, 6))

#8
def print_list(lst):
    for item in lst:
        print(item)
print_list(['apple', 'banana', 'cherry'])

#9
def reverse_list(lst):
    return lst[::-1]
print(reverse_list(['apple', 'banana', 'cherry']))

#10
def capitalize_list(lst):
    return [item.capitalize() for item in lst]
print(capitalize_list(['apple', 'banana', 'cherry']))

#11
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item(['apple', 'banana'], 'cherry'))

#12
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
print(remove_item(['apple', 'banana', 'cherry'], 'banana'))

#13
def sum_of_numbers(num):
    if num < 0:
        raise ValueError("Number must be non-negative")
    return sum(range(num + 1))
print(sum_of_numbers(5))

#14
def sum_of_odds(num):
    if num < 0:
        raise ValueError("Number must be non-negative")
    return sum(i for i in range(num + 1) if i % 2 != 0)
print(sum_of_odds(5))

#15
def sum_of_evens(num):
    if num < 0:
        raise ValueError("Number must be non-negative")
    return sum(i for i in range(num + 1) if i % 2 == 0)
print(sum_of_evens(5))

#level 2
#1
def evens_and_odds(num):
    if num < 0:
        raise ValueError("Number must be non-negative")
    evens = sum(1 for i in range(1,num + 1) if i % 2 == 0)
    odds = sum(1 for i in range(1,num + 1) if i % 2 != 0)
    return evens, odds
print(evens_and_odds(100))

#2
def factorial(num):
    if num < 0:
        raise ValueError("Number must be non-negative")
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result
print(factorial(5))

#3
def is_empty(lst):
    return len(lst) == 0

print(is_empty([]))
print(is_empty(['apple', 'banana']))

#4
from collections import Counter
from math import sqrt


def _validate_numbers(numbers):
    if not numbers:
        raise ValueError("The list must not be empty")
    if not all(isinstance(number, (int, float)) for number in numbers):
        raise TypeError("All list items must be numbers")


def calculate_mean(numbers):
    _validate_numbers(numbers)
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    _validate_numbers(numbers)
    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    return sorted_numbers[middle]


def calculate_mode(numbers):
    _validate_numbers(numbers)
    counts = Counter(numbers)
    highest_count = max(counts.values())
    return [number for number, count in counts.items() if count == highest_count]


def calculate_range(numbers):
    _validate_numbers(numbers)
    return max(numbers) - min(numbers)


def calculate_variance(numbers):
    _validate_numbers(numbers)
    mean = calculate_mean(numbers)
    return sum((number - mean) ** 2 for number in numbers) / len(numbers)


def calculate_std(numbers):
    return sqrt(calculate_variance(numbers))


values = [1, 2, 2, 3, 4]
print("Mean:", calculate_mean(values))
print("Median:", calculate_median(values))
print("Mode:", calculate_mode(values))
print("Range:", calculate_range(values))
print("Variance:", calculate_variance(values))
print("Standard deviation:", calculate_std(values))

#5
def greet_user(name="Guest"):
    return f"Hello, {name}!"
print(greet_user())
print(greet_user("Alice"))

#6
def show_args(**kwargs):
    return kwargs
print(show_args(name="Alice", age=30, city="New York"))
# Received: name: Alice, age: 30, city: New York
print(show_args(name="Bob", pet="Fluffy, the bunny"))
# Received: name: Bob, pet: Fluffy, the bunny

#level 3
#1
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))
