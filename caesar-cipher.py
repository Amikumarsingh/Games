logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26
def encrypt(plain_text , shift_text):
    cipher_text = " "
    for letters in plain_text:
        position = alphabet.index(letters)
        new_position = position + shift_text
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")

def decrypt(cipher_text , shift_amount):
    decoded_text = " "
    for letters in cipher_text:
        position = alphabet.index(letters)
        original_position = position - shift_amount
        original_letter = alphabet[original_position]
        decoded_text += original_letter
    print(f"The decoded text is: {decoded_text}")
if direction == "encode":
          encrypt(plain_text=text, shift_text=shift)
elif direction == "decode":
          decrypt(cipher_text=text , shift_amount=shift)
should_continue = True
if should_continue == True:
    while should_continue == True:
        result = input("Type 'yes' if you want to run again. Otherwise type 'no'\n")
        if result == "yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26
            if direction == "encode":
                encrypt(plain_text=text, shift_text=shift)
            elif direction == "decode":
                decrypt(cipher_text=text, shift_amount=shift)
        else:
            print("Good Bye!.....")
            should_continue = False









