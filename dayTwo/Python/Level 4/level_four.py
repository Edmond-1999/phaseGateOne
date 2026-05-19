def add_two_numbers(first_number, second_number):
    sum_of_numbers = first_number + second_number
    return sum_of_numbers

print(add_two_numbers(2, 3))

def even_number_checker(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_number_checker(4))

def squared_number(number):
    squared = number ** 2
    return squared

print(squared_number(5))

def temperature_converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(temperature_converter(16))

def largest_of_three(first_number, second_number, third_number):
    largest = first_number
    if second_number > largest:
        largest = second_number
    if third_number > largest:
        largest = third_number
    return largest

print(largest_of_three(5, 3, 9))
