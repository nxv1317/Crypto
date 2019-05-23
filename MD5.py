''' 
In this example we will be exploring the MD5 algorithm
The MD5 algorithm is a hash function. A hash function is a special mathematical function that goes one way and can not be reversed.

MD5 is a widely used cryptographic hash function with a 128-bit hash value. Itia an Internet standard (RFC 1321), 
The common application of MD5 is for checking the integrity of data stored in files. MD5 Hash.

This is how the algortihm works: 
- The information which needs to be hashed is a sequence of bits. Let's keep things simple so we will assume that it is a sequence of bytes. 
  A few extra bytes (the "padding of 0's") are appended to that sequence of bytes, 
  so that the number of extra bytes is between the values 9 and 72 (inclusive) and the total length after padding is a multiple of 64. 


- The padded data is then split into speperate blocks of values which are 64 bytes. 
  The blocks will each then be processed one by one. 
  Processing of each block (64 bytes)takes as input a 128-bit value (16 bytes) and this will return the output of the processing from the previous block, 
  which in effect outputs a new 128-bit value.


- Since the first block has no previous block, a conventional fixed value is used to start the process. 


- The complete MD5 output is the 128-bit value you get after processing the last block.

'''

import hashlib
mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())
