import random

random_number = random.randint(1, 101)

counter = 1

while True:
    if counter == 6:
        break

    guessed_number = int(input("Enter your guess(between 1 and 100): "))

    if random_number == guessed_number:
        counter += 1
        print("You Guessed Correctly")
        break

    elif random_number < guessed_number:
        print("Too High Try Again")
        if guessed_number > 100:
            print("Please let your number be between 1 and 100")
        else:
            counter +=1
    elif random_number > guessed_number:
        print("Too Low Try Again")
        if guessed_number < 1:
            print("Please let your number be between 1 and 100")
        else:
            counter += 1

print()

if counter == 1:
    print("Legendary")
elif counter == 2:
    print("Excelent")
elif counter == 3:
    print("Good")
elif counter == 4:
    print("Good")
elif counter == 5:
    print("Close!")
else:
    print("Better Luck")

print("You attempted", counter, " times")
print("The correct number is", random_number)

