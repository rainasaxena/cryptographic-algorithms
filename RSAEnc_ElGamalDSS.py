import random 
import math
import sympy


def extended_euclidean(a, b):
    if b==0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean(b, a%b)
        return gcd, y, x - (a//b) *y

def modular_inverse(a, m):
    gcd, x, y = extended_euclidean(a, m)
    if gcd!=1:
        return None
    else:
        return x%m


def find_public(phi_n):
    while True:
        e = random.randint(2, phi_n)
        if math.gcd(e, phi_n) == 1:
            return e


q = sympy.randprime(2**10, 2**16)
p = sympy.randprime(2**10, 2**16)
# p = sympy.randprime(2, 10)


n = p*q
phi_n = (p-1)* (q -1)


e = find_public(phi_n)
d = modular_inverse(e, phi_n)


m = 101
cipher = pow(m, e, n)
decrypt = pow(cipher, d, n)

print(decrypt)


#Sign with elgamal




def elgamal_encrypt(alpha, q, Xa, m):
    k = random.randint(2, q-1)
    while(math.gcd(k, q-1)!=1):
        k = random.randint(2, q-1)

    k_inv = modular_inverse(k, q-1)

    S1 = pow(alpha, k, q)
    S2 = (k_inv * (m-Xa*S1))%(q-1)

    #verufy

    v1 = pow(alpha, m, q)
    Ya = pow(alpha, Xa, q)
    v2 =  (pow(Ya, S1, q) * pow(S1, S2, q))%q

    print(v1==v2)


q = sympy.randprime(2**10, 2**16)
alpha = random.randint(2, q-1)
while(math.gcd(alpha, q)!=1):
    alpha = random.randint(2, q-1)

Xa = 23


elgamal_encrypt(alpha, q, Xa, m )


