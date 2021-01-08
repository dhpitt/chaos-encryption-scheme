# A first crack at a hypothetical encryption scheme
# for text (and images) using the logistic map.
# Using the initial population (x0) as a key, 
# For values of r >= 3.56995, we see oscillation between
# more than 256 values, meaning that we can use the first 255 
# to encode 256 ascii characters or channels of an image.
# every value is converted to the output of a logistic map
# at time = value. 

from logMap import logisticEqWithRounding
import struct
import base64

def encryptText1(inputString,key):
    # a simpler version that encrypts values from 1-26
    # key is a tuple (r,x0).
    hashes = logisticEqWithRounding(key[0],key[1],26,4)
    encrypted = [hashes[ord(char) - 97] for char in inputString]
    return encrypted

def decryptText1(input,key):
    hashes = logisticEqWithRounding(key[0],key[1],26,4)
    decrypted = [chr(hashes.index(char)+97) for char in input]
    return ''.join(decrypted)

testKey = (3.7,0.1)
outTest = encryptText1("thequickbrownfoxjumpedoverthelazydog",testKey)
print(outTest)

print("Decrypted: " + decryptText1(outTest,testKey))


