print("Welcome to family restaurant!")
number_of_people = input("How many people are in the dinner group?")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("Your table is not ready, you will have to wait to be seated")
else:
    print("Your table is ready, see a host to be seated")
