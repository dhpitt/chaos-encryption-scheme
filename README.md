# chaos-based-encryption
A proposed scheme for encrypting image data using chaotic systems.

# What is this?
I've always been curious how cryptography works so I thought I'd try my hand at making my own encryption scheme. This project includes several encryption schemes that use a chaotic system to encode and decode data. A few similar implementations exist in literature, but I wanted to see if I could figure it out on my own. 

# How does it work?
The schemes use a logistic map <https://en.wikipedia.org/wiki/Logistic_map> to create nonrepeating outputs. A demo of the logistic map equation can be found in the file logMapDemo.py. The values that I encode are mapped to their new logistic values, which cannot be re-mapped to their original values without the key (knowledge of the initial conditions of the logistic map). Since small perturbations in the initial conditions create large variation in the final system, it will take much longer to guess through brute force than to decode with the key. 

# Future directions
I want to encode images in this format. I also want to increase the complexity of the hash and make decoding more efficient. Right now my best algorithm runs in polynomial time, but I wonder if I can get it linear or better. 

