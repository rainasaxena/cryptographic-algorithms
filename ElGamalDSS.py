import random
import math
from sympy import isprime, primitive_root, mod_inverse

def elgamal_sign(m, q, a, Xa):
    k = random.randint(2, q - 1)
    while math.gcd(q - 1, k) != 1:
        k = random.randint(2, q - 1)
    S1 = pow(a, k, q)
    k_inv = mod_inverse(k, q - 1)
    S2 = (k_inv * (m - Xa * S1)) % (q - 1)
    return (S1, S2)

def elgamal_verify(m, q, a, Ya, S1, S2):
    V1 = pow(a, m, q)
    V2 = (pow(Ya, S1, q) * pow(S1, S2, q)) % q
    return V1 == V2

if __name__ == "__main__":
    q = 19
    if not isprime(q):
        print("q is not prime")
        exit()

    a = primitive_root(q)
    print("Primitive root:", a)

    m = 14
    Xa = 16

    S1, S2 = elgamal_sign(m, q, a, Xa)
    print("Signature pair (S1, S2):", (S1, S2))

    # Verification
    Ya = pow(a, Xa, q)
    if elgamal_verify(m, q, a, Ya, S1, S2):
        print("Valid Signature")
    else:
        print("Invalid Signature")
