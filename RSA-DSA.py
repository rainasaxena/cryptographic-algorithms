import random 
import sympy
import math

def generate_prime():
    return sympy.randprime(2**16, 2**32)

def find_public(phi_n):
    while True:
        e = random.randint(2, phi_n)
        if math.gcd(e,phi_n)==1:
            return e

def find_private(e, phi_n):
    return pow(e, -1, phi_n)


def RSA_encrypt_decrypt(M,e,n):
    return pow(M,e,n)


p=generate_prime()
print("p=",p)
q=generate_prime()
print("q=",q)

n=p*q
print("n=",n)

phi_n = (p-1)*(q-1)
print("phi(n)=", phi_n)

e=find_public(phi_n)
print("e=",e)
d=find_private(e, phi_n)
print("d=",d)

M=2
print("M=",M)


Mbar = RSA_encrypt_decrypt(M, e, n)
print("Encrypted Message = ", Mbar)

print("Decrypted Message = ", RSA_encrypt_decrypt(Mbar,d,n))


S = pow(M, d, n)
print("S=",S)

print("Decrypted Message = ", RSA_encrypt_decrypt(S,e,n))