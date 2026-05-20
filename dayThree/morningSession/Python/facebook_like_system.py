def the_likes_of_people(names_of_people):
    length_of_list = len(names_of_people)
    if length_of_list == 0:
        return "No one likes this"
    elif length_of_list == 1:
        return f"{names_of_people[0]} likes this"
    elif length_of_list == 2:
        return f"{names_of_people[0]} and {names_of_people[1]} like this"
    elif length_of_list == 3:
        return f"{names_of_people[0]}, {names_of_people[1]} and {names_of_people[2]} like this"
    else:
        return f"{names_of_people[0]}, {names_of_people[1]} and {length_of_list - 2} other(s) like this"



