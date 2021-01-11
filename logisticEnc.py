# A first crack at a hypothetical encryption scheme
# for text (and images) using the logistic map.
# Using the initial population (x0) as a key, 
# For values of r >= 3.56995, we see oscillation between
# more than 256 values, meaning that we can use the first 255 
# to encode 256 ascii characters or channels of an image.
# every value is converted to the output of a logistic map
# at time = value. 

from logMap import logisticEqWithRounding
from logMap import logisticRankedMap
import base64

def encryptText1(inputString,key):
    # a basic version that encrypts and decrypts lowercase letters only.
    # key is a tuple (r,x0).
    # The bad part of this system is that the encrypted data is stored
    # as a list of floats. 
    valMap = logisticEqWithRounding(key[0],key[1],26,4)
    encrypted = [valMap[ord(char) - 97] for char in inputString]
    return encrypted

def decryptText1(inputString,key):
    valMap = logisticEqWithRounding(key[0],key[1],26,4)
    decrypted = [chr(valMap.index(char)+97) for char in inputString]
    return ''.join(decrypted)


testKey = (3.7,0.1)
testKey2 = (3.699,0.1)
testKey3 = (3.703,0.09)

# These keys are pretty similar numerically. If you use one to 
# decrypt an encrypted string that used another key, they'll give something
# totally different than the correct
'''
# Testing method 1
test_input1 = input("Enter a lowercase string (no spaces) to encrypt: ")

outTest1 = encryptText1(test_input1,testKey)
print("Your string, encrypted by method 1: " + str(outTest1))
print("Decrypting... ")
print("Decrypted string: " + decryptText1(outTest1,testKey))
'''

def encryptText2(inputString,key):
    # a slightly more advanced version that works for all
    # 255 ASCII characters.
    # This method sends every character to its logistic mapped value, then encodes
    # to a base64 string.
    valMap = logisticEqWithRounding(key[0],key[1],255,6)
    encrypted = [(base64.b64encode((str(valMap[ord(char)]).encode("ascii")))).decode("ascii") for char in inputString]
    return " ".join(encrypted)

def decryptText2(inputString,key):
    valMap = logisticEqWithRounding(key[0],key[1],255,6)
    decrypted = [chr(valMap.index(float(base64.b64decode(x).decode()))) for x in inputString.split()]
    return "".join(decrypted)


# Testing method 2

'''
test_input2 = input("Enter a string of ASCII characters to encrypt: ")
outTest2 = encryptText2(test_input2,testKey)
print("Your string encrypted by method 2: " + str(outTest2))
print("Decrypting...")
print("Your string decrypted by method 2: " + str(decryptText2(outTest2,testKey)))
'''

def encryptText3(inputString,key):
    # Method 3: also works on ASCII, but instead of worrying about the values
    # produced by the logistic map themselves, I sort the values in order
    # and use the mapping (original -> ordinate position) to change ASCII
    # values into new ones. 
    rankMap = logisticRankedMap(key[0],key[1],255)
    encrypted = [chr(rankMap[ord(char)]) for char in inputString]
    return ''.join(encrypted)

def decryptText3(inputString,key):
    rankMap = logisticRankedMap(key[0],key[1],255)
    decrypted = [chr(rankMap.index(ord(char))) for char in inputString]
    return ''.join(decrypted)

'''
test_input3 = input("Enter a string of ASCII characters to encrypt: ")
outTest3 = encryptText3(test_input3,testKey)
print("Your string encrypted by method 3: " + str(outTest3))
print("Decrypting...")
print("Your string decrypted by method 3 with the key: " + str(decryptText3(outTest3,testKey)))
print("Your string decrypted by method 3 with a bad key: " + str(decryptText3(outTest3,testKey2)))
print("Your string decrypted by method 3 with another bad key: " + str(decryptText3(outTest3,testKey3)))
'''

def oneTimePadEncrypt(inputString,key):
    # generates a logistic one-time pad of the length of the input 
    # then adds the OTP to the input character-wise, and encodes
    # as hex.
    pad = logisticRankedMap(key[0],key[1],len(inputString))
    combined = [hex(ord(char) + x)  for char,x in zip(inputString,pad)]
    return ' '.join(combined)

def oneTimePadDecrypt(inputString,key):
    # decrypts text encrypted by the OTP method above
    # by obtaining the duplicate one-time pad from the key.
    split = inputString.split()
    pad = logisticRankedMap(key[0],key[1],len(split))
    decrypted = [chr(int(hex,16) - x) for hex,x in zip(split,pad)]
    return ''.join(decrypted)

# eventual image encoding, useless for now - just a code snippet that
# imports a binary image and encodes it in base64.
'''
image = open('deer.gif', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
'''
 # Sample text
loremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum pharetra, dui ac cursus elementum, lorem lacus faucibus risus, vel fermentum massa diam et ipsum. Nam tincidunt enim eu erat maximus viverra. Sed id felis id orci malesuada viverra. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec tincidunt aliquam rhoncus. Sed sagittis, elit mollis vestibulum efficitur, risus libero fringilla leo, sit amet ullamcorper purus erat nec lorem. Cras cursus in nibh hendrerit commodo. Praesent eget feugiat diam. Sed placerat a sapien eget pharetra. Etiam congue enim nec neque mattis dignissim. \n Integer sit amet est id dolor mattis lacinia ac eget nisi. Sed diam urna, venenatis sed egestas vitae, gravida at purus. Nulla ac posuere nibh, et aliquam justo. Pellentesque elit odio, pharetra nec orci sed, volutpat egestas nisi. Integer et nisi vel orci eleifend mattis at in libero. Mauris iaculis id tellus tristique luctus. Etiam arcu eros, hendrerit ut placerat ac, cursus vitae urna. Nulla non nisl at leo ornare consequat in vitae augue. Donec vehicula massa tempus venenatis consectetur. Etiam fringilla purus vel ultricies rutrum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere euismod ante, a fringilla purus faucibus in. "

lorem_OTP = oneTimePadEncrypt(loremIpsum,testKey2)
print(lorem_OTP)
print(oneTimePadDecrypt(lorem_OTP,testKey2))