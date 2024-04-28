import math
import sympy
import random 

def elgamal_dss(a, m , q, Xa):
    k = random.randint(2, q-1)

    while(math.gcd(q-1, k )!=1):
        k = random.randint(2, q-1)

    k_inv = sympy.mod_inverse(k, q-1)

    S1 = pow(a, k, q)
    S2 = (k_inv * (m-Xa*S1))%(q-1)

    return S1, S2

def elgamal_verify(a, m , q, Xa, S1, S2):
    V1 = pow(a, m , q)
    Ya = pow(a, Xa, q)

    V2 = (pow(Ya,S1, q) * pow(S1, S2,q))%q

    return V1==V2


q = sympy.randprime(1, 20)
print("q = ", q)

a = sympy.primitive_root(q)
print("Primitive Root (a) : ",a)

m = 14
Xa = 16

S1, S2 = elgamal_dss(a, m, q, Xa)

print(elgamal_verify(a, m, q, Xa, S1, S2))
