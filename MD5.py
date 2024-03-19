import math

T = [int(2**32 * abs(math.sin(i+1))) & 0xFFFFFFFF for i in range (64)]

def F (X,Y,Z):
    return (X&Y)|(~X&Z)

def G (X,Y,Z):
    return (X&Z)|(Y&~Z)

def H (X,Y,Z):
    return (X^Y^Z)

def I (X,Y,Z):
    return Y ^ (X | ~ Z)



def left_rotate(x, n):
    return ((x<<n)|(x>>(32-n)))

def md5_padding(message):
    original_length = len(message)*8
    message = message + b'\x80'
    message = message + b'\x00' * ((56-len(message)%64)%64)
    message = original_length.to_bytes(8, byteorder='little')
    return message

def md5(message):
    message = md5_padding(message)
    
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    chunks = [message[i:i+64] for i in range (0, len(message), 64)]

    for chunk in chunks:
        a,b,c,d = a0, b0, c0, d0
        X=[int.from_bytes(chunk[i:i+4], byteorder='little') for i in range (0,64,4)]
        for i in range (64):
            if 0<=i<16:
                g = i
                F_result = F(b,c,d)
            elif 16<=i<32:
                g = (5*i+1)%16
                F_result=G(b,c,d)
            elif 32<=i<48:
                g = (3*i+5)%16
                F_result = H(b,c,d)
            else:
                g = (7*i)%16
                F_result = I(b,c,d)
            
            d_temp = d
            d = c
            c = b
            b = (b + left_rotate((a + F_result + T[i] + X[g]) & 0xFFFFFFFF , (i%32) )) & 0xFFFFFFFF
            a = d_temp
        a0 = (a0+a) & 0xFFFFFFFF
        b0 = (b0+b) & 0xFFFFFFFF
        c0 = (c0+c) & 0xFFFFFFFF
        d0 = (d0+d) & 0xFFFFFFFF

    return sum((a0, b0<<32, c0<<64, d0<<96))
    

    



message = b'Hello, this is a 1000 bit message for hashing purposes. This message is designed to be exactly 1000 bits long.'

hashed_message = md5(message)
print("MD5 Hash:", hex(hashed_message))
