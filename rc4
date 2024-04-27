def initialize(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def generate_keystream(S, data_length):
    i = 0
    j = 0
    keystream = []
    for _ in range(data_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream_byte = S[(S[i] + S[j]) % 256]
        keystream.append(keystream_byte)
    return keystream

def rc4_encrypt(data, key):
    S = initialize(key)
    keystream = generate_keystream(S, len(data))
    encrypted_data = [byte ^ keystream_byte for byte, keystream_byte in zip(data, keystream)]
    return bytes(encrypted_data)

def rc4_decrypt(data, key):
    return rc4_encrypt(data, key)  # Decryption is the same as encryption in RC4

# Example usage:
key = b'YourSecretKey'
plaintext = b'Hello, World!'
encrypted = rc4_encrypt(plaintext, key)
decrypted = rc4_decrypt(encrypted, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
