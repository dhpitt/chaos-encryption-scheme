# chaos-based-encryption
A proposed scheme for encrypting image data using chaotic systems.

![The Logistic Equation](https://github.com/dhpitt/chaos-encryption-scheme/blob/main/images/bifurcation_diagram_2.png)
### A bifurcation diagram of the logistic equation

# What is this?
I've always been curious how cryptography works so I thought I'd try my hand at making my own encryption scheme. This project includes several encryption schemes that use a chaotic system to encode and decode data. A few similar implementations exist in literature, but I wanted to see if I could figure it out on my own.

# What's in the repository?
logMap.py contains some implementations of the logistic equation, the mathematical backbone of the encryption scheme. logMapDemo.py shows the logistic equation at work under several different conditions, and demonstrates the minimal testing I've performed thus far to check if my cryptographic hash has collisions. logisticEnc.py contains the actual encryption scheme and allows the user to encrypt and decrypt ASCII data of their choice using my encryption scheme. conceptArt.py contains the code I used to generate the neat pattern I use as the background of the GitHub page (still in development). 

# How does it work?
The scheme uses a [logistic map](https://en.wikipedia.org/wiki/Logistic_map) to create nonrepeating outputs. A demo of the logistic map equation can be found in the file logMapDemo.py. The values that I encrypt are mapped to their new logistic values, which cannot be re-mapped to their original values without the key (knowledge of the initial conditions of the logistic map). Since small perturbations in the initial conditions create large variation in the final system, the system will take much longer to crack through brute force than to decode with the key. 

# Future directions
I want to encode images in this format. I also want to increase the complexity of the hash and make decoding more efficient. Right now my best algorithm runs in polynomial time, but I wonder if I can get it linear or better. 

# Acknowledgments
Thanks to Prof. Spencer for helping me find resources on LTSpice and chaotic encryption. 
