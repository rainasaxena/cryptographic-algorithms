#preprocessing
plaintext = [0, 2, 4, 6, 8, 'A', 'C', 'E', 1, 3, 5, 7, 9, 'B', 'D', 'F', 0, 2, 4, 6, 8, 'A', 'C', 'E', 1, 3, 5, 7, 9, 'B', 'D', 'F']
plaintext = ''.join(str(item) for item in plaintext)
# print(plaintext)
plaintext = bytearray.fromhex(plaintext)
# print(plaintext)


key = ['F', 'E', 'D', 'C', 'B', 'A', 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 'F', 'E', 'D', 'C', 'B', 'A', 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
key = ''.join(str(item) for item in key)
# print(plaintext)
key = bytearray.fromhex(key)
# print(key)

Sbox = [
    99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118,
    202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114,
    192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49,
    21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117,
    9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83,
    209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239,
    170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64,
    143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19,
    236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220,
    34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6,
    36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213,
    78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180,
    198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14,
    97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148,
    155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104,
    65, 153, 45, 15, 176, 84, 187, 22
]
sbox_hex = [hex(value)[2:].zfill(2) for value in Sbox]
# print(sbox_hex)
sbox_hex_string = ''.join(sbox_hex)
# print(sbox_hex_string)
s_box = bytearray.fromhex(sbox_hex_string)
# print(s_box)


#################################
def state_from_bytes(data):
    state = [data[i*4:(i+1)*4] for i in range(len(data) // 4)]
    return state
    
def sub_bytes(state):
    for r in range(len(state)):
        state[r] = [s_box[state[r][c]] for c in range(len(state[0]))]
    return state
    
def shift_rows(state):
    # [00, 10, 20, 30]     [00, 10, 20, 30]
    # [01, 11, 21, 31] --> [11, 21, 31, 01]
    # [02, 12, 22, 32]     [22, 32, 02, 12]
    # [03, 13, 23, 33]     [33, 03, 13, 23]
    state[0][1], state[1][1], state[2][1], state[3][1] = state[1][1], state[2][1], state[3][1], state[0][1]
    state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
    state[0][3], state[1][3], state[2][3], state[3][3] = state[3][3], state[0][3], state[1][3], state[2][3]
    return state
    
def xor_key(state, key):
  new_state = []
  for row in state:
    new_row = []
    for i in range(len(row)):
      # Ensure key byte is within its valid range (0 to 255)
      key_byte = key[i % len(key)]  # Wrap around for key length
      new_row.append(row[i] ^ key_byte)
    new_state.append(new_row)
  return new_state
  
  
 
def bytes_from_state(state):
    return bytes(state[0] + state[1] + state[2] + state[3])


def aes_encryption(data, key):
    nr = 10
    
    #make state matrix
    state = state_from_bytes(data)
    
    for round in range(1, nr):
        state=sub_bytes(state)
        state=shift_rows(state)
        state=xor_key(state, key)
        
    
    cipher = bytes_from_state(state)
    print(cipher)
    # return cipher
    
    
    
    
aes_encryption(plaintext, key)
 
