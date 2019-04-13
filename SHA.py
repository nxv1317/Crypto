'''
In this example we will be exploring the SHA algorithm

The SHA algorithm is a hash function. A hash function is a special mathematical function that goes one way and can not be reversed.

The common application of SHA is for storing password securely.

The SHA algorithm follows the avalanche effect, this means that if one small aspect of the text has been changed then it will result in the entire hash being different.

This is how the algortihm works: 
1) The first step is to intialise 5 random hex values
2) The message will be padded and then a 1 will be appended to the end and enough 0's will be appended until the message value is 448 bits. The length of the entire message in 64 bits is added to the end, producing the message which is 512 bits long.
3) The message is divided into 32 16bit blocks (making a grand total of 512 bits
4) For each chunk 80 iterations is needed. For each value between 16 and 79 the XOR operations will be performed and the circular shifts are performed at this stage.
5) The hash values will be stored in variables
6) The swaps between the has variables are performed at this stage
7) The result of the overall hash chunk is appended to the overall hash value
8) At this stage the logical or operation is performed on the 5 hashed vaslues
'''
import hashlib 

hashText = str(input("Please enter the text to be hashed: "))
hash_object = hashlib.sha256(str(hashText).encode('utf-8'))
print('Hash', hash_object.hexdigest())

