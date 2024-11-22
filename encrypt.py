import os
def main():
    user_option = input('Hello, welcome to advanced encrypter and decrypter made by DannyBlue and Qubi. To decrypt input (d), encrypt (e). If you want to Quit type q : \n')
  
    if user_option == "e":
        text = input('Enter your message to encrypt: \n')
        custom_key = input('Enter your secret key to encrypt: \n')
        encryption = encrypt(text, custom_key)
        print(encryption)
    
    elif user_option == "d":
        print("You have entered the decryption center for the DannyBlue and Qubi advanced encrypter \n")
        text = input('Enter your message to decrypt: \n')
        custom_key = input('Enter your secret key to decrypt: \n')
        decryption = decrypt(text, custom_key)
        print()
        print(decryption)
    elif user_option == 'q':
  	    quit()
    else:
        print('Error, look at the first line.')

    

def vigenere(message, key, direction):
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()`-=~_+[]{};:,.<>/? '"
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        # Find the right key character to encode/decode
        key_char = key[key_index % len(key)]
        key_index += 1

        # Define the offset and the encrypted/decrypted letter
        offset = alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset*direction) % len(alphabet)
        final_message += alphabet[new_index]
    
    return final_message
    
def decrypt(message, key):
    return vigenere(message, key, -1)
  
def encrypt(message, key):
    return vigenere(message, key, 1)

def clean_terminal_screen():
    """
    Cleans the terminal screen by performing a system
    clear command. Cls on windows and Clear on UNIX ones.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
  
while True:
  main()
  print()