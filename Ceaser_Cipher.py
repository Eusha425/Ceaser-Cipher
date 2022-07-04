# function to return back the index of a character 
# takes the user input message and an initial index of 0 as parameters 
def return_index(message, index):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(alphabets)): 
        if message[index:index+1] == alphabets[i]:
            return i
        
# function to encrypts each character of the user input text
# takes the index value of each character and the key shift as parameters 
# returns the encrypted character 
def encryption(index, key):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = ""
    if alphabets[index] == alphabets[25]: # to check if the character is z
        # key value decreased by one as the character index starts from 0 
        cipher_text = alphabets[0 + key - 1] # jumps to the index 0 as there are no characters after z
    else:
        cipher_text = alphabets[index + key]
    return cipher_text

# function to verify if the user input key shift is valid
# returns the key after verification
def key_verify():
    key = int(input("Enter The key to shift: "))    # take integer input to know the key shift of the message
    while key <= 0:
        print("Invalid key")
        key = int(input("Enter The key to shift: "))
    return key

# variable declaration
message = input("Enter your text: ")   # for user input text
cipher_message = ""                    # to hold the encrypted text
key = key_verify()                     # the key shift for each characters 
message = message.lower()

# to encrypt each individual characters of the text
for i in range(len(message)):
    if message[i:i+1] == " ": # checking if the message contains any spaces
        cipher_message = cipher_message + " "
    else:
        index = return_index(message, i)
        cipher_message = cipher_message + encryption(index, key)

print(cipher_message)