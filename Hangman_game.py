import random
word_list =  ["advark" , "baboon", "camel"]
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
lives = 6
choose_word = random.choice(word_list)
# guess = input("Enter a word?").lower()
display =[]
for letter in range(len(choose_word)):
    display += '_'
end_of_game= False
while not end_of_game:
    guess = input("Enter a letter which you think to be in 6 letter word?").lower()
    for position in range(len(choose_word)):
        letter = choose_word[position]
        if letter == guess:
            display[position] = letter
    print(display)



    if guess  not in choose_word:
        lives -= 1
        if lives == 0:
            print("you loose")
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("You won!")

    print(stages[lives])