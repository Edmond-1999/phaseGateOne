def prime_number_array(my_list):
    new_list = []
    for index in range(len(my_list)):
        for number in range(2, my_list[index]):
            if my_list[index] % number != 0:
                new_list.append(my_list[index]);
    return new_list

print(prime_number_array([5, 9, 3, 6, 2]))

def replace_neagtive(my_list):
    for index in range(len(my_list)):
        if my_list[index] < 0:
            my_list[index] = 0

    return my_list

print(replace_neagtive([5, -9, 3, -6, 2, -11]))

def move_all_zeros(my_list):
    for index in range(len(my_list)):
        if my_list[index] == 0:
            my_list.pop(index)
            my_list.append(0)

    return my_list

print(move_all_zeros([5, 0, 3, 0, 2, 0]))

def finding_duplicate_elements_in_array(my_list):
    new_list = []
    for index1 in range(len(my_list)):
        for index2 in range(len(my_list)):
            if my_list[index1] == my_list[index2]:
                new_list.append(my_list[index1])
    return new_list

print(finding_duplicate_elements_in_array([45, 60, 3, 0, 67, 2, 45, 3, 22, 0]))








