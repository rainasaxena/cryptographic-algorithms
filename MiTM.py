import math
import random

q = 227
alpha = 14
 
 
Xa = random.randint(1, q) #alice secret
Xb = random.randint(1, q) #Bob secret
Ya = pow(alpha, Xa, q) #alice public
Yb = pow(alpha, Xb, q) #bob public
Sa = pow(Yb, Xa, q) #alice shared secret actual
Sb = pow(Ya, Xb, q) #alice shared secret actual
 
print("Actual Shared Secret:", Sa, Sb)
 
Xc = random.randint(1, q) #eve alice secret
Xd = random.randint(1, q) #eve bob secret
Yc = pow(alpha, Xc, q) #
Yd = pow(alpha, Xd, q)
 
# If Alice uses Sa_fake as a key to encrypt a later message to Bob, Malory can decrypt it, re-encrypt it using Sb_fake, and send it to Bob. Bob and Alice won’t notice any problem and may assume their communication is encrypted, but in reality, Malory can decrypt, read, modify, and then re-encrypt all their conversations.
Sa_fake = pow(Yd, Xa, q)
Sb_fake = pow(Yc, Xb, q)
print("Compromised Shared Secret:", Sa_fake, Sb_fake)
