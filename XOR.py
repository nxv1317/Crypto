from itertools import cycle

#XOR CIPHER
def xorcipher(message,key):
    '''
    In simple english the XOR cipher performs the XOR operation on the message on the key. 
    In the example what we do is we convert the message and key to their ASCII equivilent using the ord() python function, then we perfrom the XOR operation. 
    The mathematical formula for the XOR cipher is: e(x) = x XOR k 
    SYMBOLS MEANING:
    e(x) = this means to encrypt the plaintext x
    XOR = this is the exclusive OR, XOR is a logical operation which only outputs true when the inputs differ, for example: 0 XOR 0 = FALSE, 0 XOR 1 = TRUE, 1 XOR 0 = TRUE, 1 XOR 1 = FALSE
    k = shift (or key) 
    '''
    ciphered = ''.join(chr(ord(c)^ord(k)) for c,k in zip(message, cycle(key)))
    print("{} ^ {} = {}".format(message,key,ciphered))
    message = ''.join(chr(ord(c)^ord(k)) for c,k in zip(ciphered, cycle(key)))
    print("{} ^ {} = {}".format(ciphered,key,message))