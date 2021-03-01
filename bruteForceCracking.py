from logisticEnc import ascii_mapping, ascii_mapping_reverse, oneTimePadEncrypt, oneTimePadDecrypt

loremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum pharetra, dui ac cursus elementum, lorem lacus faucibus risus, vel fermentum massa diam et ipsum. Nam tincidunt enim eu erat maximus viverra. Sed id felis id orci malesuada viverra. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec tincidunt aliquam rhoncus. Sed sagittis, elit mollis vestibulum efficitur, risus libero fringilla leo, sit amet ullamcorper purus erat nec lorem. Cras cursus in nibh hendrerit commodo. Praesent eget feugiat diam. Sed placerat a sapien eget pharetra. Etiam congue enim nec neque mattis dignissim. \n Integer sit amet est id dolor mattis lacinia ac eget nisi. Sed diam urna, venenatis sed egestas vitae, gravida at purus. Nulla ac posuere nibh, et aliquam justo. Pellentesque elit odio, pharetra nec orci sed, volutpat egestas nisi. Integer et nisi vel orci eleifend mattis at in libero. Mauris iaculis id tellus tristique luctus. Etiam arcu eros, hendrerit ut placerat ac, cursus vitae urna. Nulla non nisl at leo ornare consequat in vitae augue. Donec vehicula massa tempus venenatis consectetur. Etiam fringilla purus vel ultricies rutrum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere euismod ante, a fringilla purus faucibus in. "

sampleKey = (3.695202,0.710539)
encrypted = oneTimePadEncrypt(loremIpsum,sampleKey)

def bruteForceCracker(inputString):
    # Kind of cheating. Knows the code is a logistic
    # one time pad and also knows the original message. 
    # Goal is to prove that given this knowledge you can eventually 
    # crack a logistic OTP with brute force.
    cracked = False
    r = 3.56995 # r > 3.56995 generates chaotic outputs
    x0 = 0
    for i in range(10000):
        for j in range (10000):
            output = oneTimePadDecrypt(inputString,(r+0.00001*i,x0+0.00001*j))
            if output == loremIpsum:
                cracked = True
                break

bruteForceCracker(encrypted)

            
    
