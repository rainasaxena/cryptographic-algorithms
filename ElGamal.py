import random
import math

#q->prime
#alpha->primitive root of q
#Xa->Secret key of Alice
#Xb->Secret key of Bob
#Ya->Public key of Alice
#Yb->Public key of Bob
#k->random integer relatively prime to q
#Sa->Shared secret of Alice
#Sb->Shared secret of Bob
#Sa=Sb=S(Secret key)
#c1, c2 -> cipher text

def diffie_hellman(q, alpha, Xa, Xb):
    Ya = pow(alpha, Xa, q)
    Yb = pow(alpha, Xb, q)
    Sa = pow(Yb, Xa, q) 
    Sb = pow(Ya, Xb, q) 
    return Ya, Yb, Sa, Sb

def find_coprime(q):
    while True:
        k = random.randint(2, q-1)
        if math.gcd(k,q)==1:
            return k

def elgamal(q, alpha, Xa, Xb, message):
    Ya, Yb, Sa, Sb = diffie_hellman(q,alpha,Xa,Xb)
    k = find_coprime(q)

    #Encryption done by shared secret of Alice
    c1 = pow(alpha, k , q)
    c2 = pow(message*Sa, 1, q)
    print("Cipher text: ", c1, c2)

    #Decryption done by shared secret of Bob
    decrypted = pow(c2*(pow(Sb, -1, q)), 1, q)
    print("Decrypted Text: ", decrypted)


#Driver Function
elgamal(1229, 12, 150, 250, 100)
