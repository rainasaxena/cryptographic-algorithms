def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def extended_euclidean(a,b):
    if b==0:
        return a, 1, 0
    else:
        gcd, x, y  = extended_euclidean(b, a%b)
        return gcd, y, x - (a//b) * y
    
def modular_inverse(a, m):
    gcd, x, y = extended_euclidean(a, m)
    if gcd!=1:
        return None
    else:
        return x%m
    

def extended_euclidean(a,b):
    if b==0:
        return a, 1, 0
    else:
        gcd, x, y  = extended_euclidean(b, a%b)
        return gcd, y, x - (a//b) * y
    
def modular_inverse(a, m):
    gcd, x, y = extended_euclidean(a, m)
    if gcd!=1:
        return None
    else:
        return x%m
    
print("Modular inverse is", modular_inverse(7, 101))

# Extended Euclidean algorithm to express GCD as linear sum
gcd, x, y = extended_euclidean(7, 101)
print("GCD of 7 and 101 as a linear sum:", gcd, "=", "7", "*", x, "+", "101", "*", y)
