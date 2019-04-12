import random 

'''
This code generates a random key based on the users input. It will shuffle the text. For example if the plaintext is "Hello", it will generate a key that is a scrambled version of that, for example "lelho"
'''
plaintext = str(input("Please enter the plaintext here: ")) #the user enters the plain text

def keygen(plaintext):
    chars = list(plaintext) #stores each individual character of the plaintext into a list
    random.shuffle(chars) #shuffles the characters in the plain text
    print(''.join(chars)) #joins the shuffled text to a string and then prints the output

if keygen(plaintext) == plaintext: #checks if the shuffle function generates the same character sequence as the plaintext, we can't have it generating the exact same!
  keygen(plaintext) #if that is the case then run the function again until it is different
else:
  print("Success") #else it will print "success"