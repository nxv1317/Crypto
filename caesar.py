def caesarCipher(plainText):
    '''
    In simple english, the caesar cipher takes the text input from the user and then shifts each character in the input by 3.
    The mathematical formula for Caesar cipher is: e(x) = (x + k) mod 26
    SYMBOL MEANINGS: 
    e(x) = this means to encrypt the plaintext x
    x = the plaintext 
    k = shift (or key) 
    mod 26 = perfom the mod 26 operation, the reason why it is 26 is because there are 26 letters in the english alphabet
    '''
    caesar_cipher_Text = []#initialize array for the ciphered text


    caesar_deciphered_Text = []#initialize array for the deciphered text

    shift = 3 #in the classical caesar cipher, the text was shifted by 3 values

    #loop through each character in the plain text, get then ascii value, add the shift then add it to the ciphered text array

    for char in plainText: 
        caesar_cipher_Text.append(chr(ord(char) + shift))
    
    print("The ciphered text is: {}".format(caesar_cipher_Text))

#do the opposite in order to get the deciphered text, get the ascii value then subtract the shift to get the original text
    for value in caesar_cipher_Text:
        caesar_deciphered_Text.append(chr(ord(value) - shift))
    
    print("The deciphered text is: {}".format(caesar_deciphered_Text))
