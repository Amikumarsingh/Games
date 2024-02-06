logo = '''
 _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                                        
'''
print(logo)
print("Welcome to Number Guessing Game?")
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "13", "14", "15",
         "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
"31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45",
"46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
"61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75",
"76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
"91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]

import random
randam_number = random.choice(number)
def easy():
    number_of_attempt = 10
    print("you have 10 attempts to guess the number.")

    end_of_game = False
    while not end_of_game:
        guess = input("Make a guess:")
        number_of_attempt -= 1
        print(f"Your are left with {number_of_attempt} number of  attempt.")
        if guess == randam_number:
            print("That's right! You guessed it right...")
            print("YOU WON!!!!")
            print("THANK YOU ...BYE!!!")
            end_of_game = True
        elif guess > randam_number:
            print("It's too high think of the number smaller than it. ")
        elif guess < randam_number:
            print("It's too low think of number grater than it.")
        if number_of_attempt == 0:
            print("You ran out of attempts!...")
            print("YOU LOOSE!!!!!!")
            print("THANK YOU ...BYE!!!")
            end_of_game = False
def hard():
    print("You have 5 attempts to guess the number.")
    end_of_game = False
    number_of_attempts = 5
    while not end_of_game:
        guess = input("Make a guess:")
        number_of_attempts -= 1
        print(f"You are left with {number_of_attempts}  attempts.")
        if guess == randam_number:
            print("That's right! You guessed it right...")
            print("YOU WON!!!!")
            print("THANK YOU ...BYE!!!")
            end_of_game = True
        elif guess > randam_number:
            print("It's too high think of the number smaller than it. ")
        elif guess < randam_number:
            print("It's too low think of number grater than it.")

        if number_of_attempts == 0:
            print("You ran out of attempts!...")
            print("YOU LOOSE!!!!!!")
            print("THANK YOU ...BYE!!!")
            end_of_game = True

choose =input("Choose a difficulty. Type 'easy' or 'hard'.")
print("I'm thinking of number between 1 to 100.")
if choose == 'easy':
    easy()
elif choose == 'hard':
    hard()
