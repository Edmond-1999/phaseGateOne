def sum_of_two_numbers(my_list, number):
    new_list = []

    for index in range(len(my_list)):
        for count in range(len(my_list)):
            if my_list[index] + my_list[count] == number:
                new_list.append(my_list[index])
                new_list.append(my_list[count])
        if new_list[0] == my_list[index] and new_list[1] == my_list[count]:
            break

    return new_list


def range_between_largest_and_smallest_numbers(my_list):
    largest = my_list[0]

    for number in my_list:
        if number > largest:
            largest = number

    smallest = my_list[0]

    for number in my_list:
        if number < smallest:
            smallest = number

    range_of_numbers = []

    for index in range((largest - smallest) + 1):
        range_of_numbers.append(index)

    for index in range(len(range_of_numbers)):
        range_of_numbers[index] = smallest
        smallest += 1

    return range_of_numbers



def consonants_in_words(my_list):
    new_list = []
    for word in my_list:
        for letter in word:
            if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                ...
            else:
                my_list.remove(word)
                new_list.append(word)





