def get_user_wants():
    zipcode = input("What zipcode are you located at?\nEnter a 5 digit zipcode. ")
    while not(zipcode.isnumeric() and len(zipcode) == 5):
        zipcode = input("Invalid zipcode, please enter a new 5 digit zipcode. ")

    distances = ["1", "5", "10", "25", "50"]
    distance = input("How many miles do you want to search?\nType an integer 1, 5, 10, 25, 50. ")
    while not(distance.isnumeric() and distance in distances):
        distance = input("Invalid distance, please type an integer from the list. ")

    return zipcode, distance
