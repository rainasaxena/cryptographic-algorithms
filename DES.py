#DECRYPTION 
def inverse_permute(text):
    permutation = [0, 4, 1, 5, 2, 6, 3, 7]
    permuted_bits = [None] * len(permutation)
    for i, j in enumerate(permutation):
        permuted_bits[j] = text[i]
    return ''.join(permuted_bits)

def unmap(text):
    for key in binary_sbox.keys():
        if binary_sbox[key] == text:
            return key
        
def right_shift(text):
    return text[-1] + text[:-1]

def decrypt(ciphertext, key):

    #inverse xor operation 
    mod_pt = [(ord(a)^ord(b)) for a,b in zip (ciphertext, key)]
    mod_pt = ''.join(str(i) for i in mod_pt)

    #inverse permutation
    mod_pt, mod_key = inverse_permute(mod_pt), inverse_permute(key)

    #split into 4 bits left and right
    left_pt, right_pt = split(mod_pt)
    left_key, right_key = split(mod_key)

    #unmap from sbox
    left_pt, right_pt = unmap(left_pt), unmap(right_pt)
    print("1st i=unmapped pt:", left_pt, right_pt)
    left_key, right_key = unmap(left_key), unmap(right_key)

    #right shift
    left_pt, right_pt = right_shift(left_pt), right_shift(right_pt)
    left_key, right_key = right_shift(left_key), right_shift(right_key)

    plaintext = left_pt + right_pt
    key = left_key + right_key

    return plaintext, key
        

#ENCRYPTION
def split(text):
    left, right = text[0:4], text[4:]
    return left, right

def left_shift(text):
    return text[1:] + text[0]

sbox = [0, "f", 1, "e", 2, "d" , 3, "c", 4, "b", 5, "a", 6, 9, 7, 8]
binary_sbox = {}
for i in range(16):
    binary_key = format(i, '04b')
    value = sbox[i]
    binary_value = format(int(value, 16), '04b') if isinstance (value, str) else format(value, '04b')
    binary_sbox[binary_key] = binary_value

def permute(text):
    permutation = [0, 2, 4, 6, 1, 3, 5, 7]
    permuted_bits = [None] * len(permutation)
    for i, j in enumerate(permutation):
        permuted_bits[j] = text[i]
    return ''.join(permuted_bits)


def encrypt(plaintext, key):

    #Split pt and key into 4 parts
    left_pt, right_pt = split(plaintext)
    left_key, right_key = split(key)

    #Left shift pt and key bits
    left_pt, right_pt = left_shift(left_pt), left_shift(right_pt)
    left_key, right_key = left_shift(left_key), left_shift(right_key)

    #Map to sBox
    left_pt, right_pt = binary_sbox[left_pt], binary_sbox[right_pt]
    left_key, right_key = binary_sbox[left_key], binary_sbox[right_key]

    #concatenate left and right parts to 8 bits again
    mapped_pt = left_pt+right_pt
    mapped_key = left_key+right_key
    print(mapped_pt, mapped_key)

    #add permutation
    mod_pt, mod_key = permute(mapped_pt), permute(mapped_key)

    #xor the key to get new plain text 
    new_mod_pt = [(ord(a)^ord(b)) for a, b in zip (mod_pt, mod_key)]
    new_mod_pt = ''.join(str(i) for i in new_mod_pt)

    return new_mod_pt, mod_key

#DRIVER CODE
plaintext = "10101010"
key = "11001100"

#encryption
round1_plaintext, round1_key = encrypt(plaintext, key)
print("1:",round1_plaintext, round1_key)
round2_plaintext, round2_key = encrypt(round1_plaintext, round1_key)
print("2:",round2_plaintext, round2_key)

#decryption
ret_round2_plaintext, ret_round2_key = decrypt(round2_plaintext, round2_key)
ret_plaintext, ret_key = decrypt(ret_round2_plaintext, ret_round2_key)
print("decrypted plain text, key", ret_plaintext, ret_key)