#string -> char(2B 16bit) -> x1 x2 x3 x4 & k1 k2 k3 k4 k5 k6 (x,k = 4bit) 
# example key = 1010 1110 1001 0110 0010 0001 1101 0101
import random
import math

def random_key_generator():
    key_bit_lenght = 32
    random_key = ""
    for i in range(32):
        random_key = random_key + str(random.randint(0,1))
    return random_key

def binstrip(binary):
    if type(binary) != str:
        binary = bin(binary)
    if binary[0:2] == "0b":
        binary = binary[2:]
    return binary

def zerofill(number, lenght = 16):
    if len(number) < lenght:
        number = (lenght - len(number)) * "0" + number 
    if len(number) > lenght:
        number = number[-lenght:]
    return number

def zbinstrip(binary,lenght = 16):
    if type(binary) != str:
        binary = bin(binary)
    if binary[0:2] == "0b":
        binary = binary[2:]
    if len(binary) < lenght:
        binary = (lenght - len(binary)) * "0" + binary 
    if len(binary) > lenght:
        binary = binary[-lenght:]
    return binary
    
def key_split(key,output_type = "dict"):
    key_k_index = 1
    if output_type == "dict":
        subkey = {}
        for subkeys_index in range(0,32,4):
            subkey["k"+str(key_k_index)] = key[subkeys_index: subkeys_index + 4] 
            key_k_index += 1
    if output_type == "list":
        subkey = []
        for subkeys_index in range(0,32,4):
            subkey.append(key[subkeys_index: subkeys_index + 4])
    return subkey

def create_subkeys(key):
    #creating an empty round list containig each 8 keys  ===> keys round k1 
    max_round = 5
    keys = []
    for i in range(max_round+1):
        round = {}
        for j in range(6):
            round["k"+str(j+1)] = "" 
        keys.append(dict(round))
    # inserting the different keys in the rounds
    current_round = 1
    current_subkey = "k1"
    for i in range(int(math.ceil(6/8*max_round))):
        for j in key_split(key,"list"):
            keys[current_round - 1][current_subkey] = j
            key_value = int(current_subkey[1:]) + 1
            current_subkey = "k" + str(key_value)
            if int(current_subkey[1:]) >= 7:
                current_round += 1
                current_subkey = "k1"
        #rotating key
        key = key[6:] + key[0:6]
    return keys

def string_to_bit_sequence(astring = "error2    the sender forgot to write a message ..."):
    bit_sequence = []
    for achar in astring:
        unicode_equivalent = ord(achar)
        binary_equivalent = bin(unicode_equivalent)
        bit_sequence.append(binstrip(binary_equivalent))
    #filling the empty binary room to enable spliting 16 bit -> 4 * 4 bit
    correct_lenght_bit_sequence = []
    for bits in bit_sequence:
        if len(bits) != 16 :
            correct_lenght_bit_sequence.append((16 - len(bits)) * "0" + bits)
    bit_sequence = correct_lenght_bit_sequence
    return bit_sequence

def bit_input_to_bit_seqence(abin):
    #1000000000000000 1111111111111111 --> [1000000000000000,1111111111111111]
    bit_sequence = abin.split(" ")
    return bit_sequence


def IDEA_encryption(message,key,binary_output = False,input = "string"):
    # converting input to bit sequence
    if input == 'string':
        binary_code_list = string_to_bit_sequence(message)
    if input == 'binary':
        binary_code_list = bit_input_to_bit_seqence(message)
    #sequencing each binary char code into 4 sub chunk each 4 bit and in an organized list
    chunk_list = []
    chunk_index = 0
    for binary_code in binary_code_list:
        chunk_list.append([])
        for index in range(0,16,4):
            chunk_list[chunk_index].append(binary_code[index:index+4])
        chunk_index += 1
    #key splitting
    key_matrix = create_subkeys(key)
    for chunk_block in chunk_list:
        #the number of rounds is max_round
        max_round = 4.5
        for rounds in range(int(int(max_round-1.5))):
            #calculation part
            step1 = (int(chunk_block[0],2) * int(key_matrix[rounds]["k1"],2)) % 17 
            step2 = (int(chunk_block[1],2) + int(key_matrix[rounds]["k2"],2)) % 16
            step3 = (int(chunk_block[2],2) + int(key_matrix[rounds]["k3"],2)) % 16
            step4 = (int(chunk_block[3],2) * int(key_matrix[rounds]["k4"],2)) % 17
            step5 = step1 ^ step3
            step6 = step2 ^ step4
            step7 = (step5 * int(key_matrix[rounds]["k5"],2)) % 17
            step8 = (step6 + step7) % 16
            step9 = (step8 * int(key_matrix[rounds]["k6"],2)) % 17
            step10 = (step7 + step9) % 16
            step11 = step1 ^ step9
            step12 = step3 ^ step9
            step13 = step2 ^ step10
            step14 = step4 ^ step10
            chunk_block[0] = zbinstrip(step11, 4)
            chunk_block[1] = zbinstrip(step13, 4)
            chunk_block[2] = zbinstrip(step12, 4)
            chunk_block[3] = zbinstrip(step14, 4)
        #last round somme differences
        step1 = (int(chunk_block[0],2) * int(key_matrix[int(max_round-1.5)]["k1"],2)) % 17 
        step2 = (int(chunk_block[1],2) + int(key_matrix[int(max_round-1.5)]["k2"],2)) % 16
        step3 = (int(chunk_block[2],2) + int(key_matrix[int(max_round-1.5)]["k3"],2)) % 16
        step4 = (int(chunk_block[3],2) * int(key_matrix[int(max_round-1.5)]["k4"],2)) % 17
        step5 = step1 ^ step3
        step6 = step2 ^ step4
        step7 = (step5 * int(key_matrix[int(max_round-1.5)]["k5"],2)) % 17
        step8 = (step6 + step7) % 16
        step9 = (step8 * int(key_matrix[int(max_round-1.5)]["k6"],2)) % 17
        step10 = (step7 + step9) % 16
        step11 = step1 ^ step9
        step12 = step3 ^ step9
        step13 = step2 ^ step10
        step14 = step9 ^ step10
        chunk_block[0] = binstrip(step11)
        chunk_block[1] = binstrip(step12)
        chunk_block[2] = binstrip(step13)
        chunk_block[3] = binstrip(step14)
        step1 = (int(chunk_block[0],2) * int(key_matrix[int(max_round-1.5)]["k1"],2)) % 17 
        step2 = (int(chunk_block[1],2) + int(key_matrix[int(max_round-1.5)]["k2"],2)) % 16
        step3 = (int(chunk_block[2],2) + int(key_matrix[int(max_round-1.5)]["k3"],2)) % 16
        step4 = (int(chunk_block[3],2) * int(key_matrix[int(max_round-1.5)]["k4"],2)) % 17
        chunk_block[0] = zbinstrip(step11,4)
        chunk_block[1] = zbinstrip(step12,4)
        chunk_block[2] = zbinstrip(step13,4)
        chunk_block[3] = zbinstrip(step14,4)
        #chunkblock merging into blocks
        final_chunk = ""
        for sub_chunk_blok in chunk_block:
            final_chunk = zbinstrip(final_chunk + sub_chunk_blok)
        chunk_block.clear()
        chunk_block.append(final_chunk)
    final_string = ""
    if binary_output != False:
        for char in chunk_list:
            final_string = final_string + chr(int(char[0],2))
        return final_string
    else: 
        for binaries in chunk_list:
            final_string = final_string + str(binaries[0]) + " "
        return final_string

def decode(encrypted_data,key):
    #type determination (str or bin) could be improuved
    if encrypted_data[1] == "0" or encrypted_data[1] == "1":
        atype = "bin"
    else:
        atype = "str"
    chunk_list = []
    #preping the str input -> converting in bloks/subloks (bin format)
    if atype == "str":
        for char in encrypted_data:
            whole_block = zbinstrip(ord(char),16)
            block = []
            for block_index in range(0,16,4):
                block.append(whole_block[block_index:block_index + 4])
            chunk_list.append(block)
    #preping the bin input -> converting in bloks/subloks (bin format)
    if atype == "bin":
        whole_block_list = encrypted_data.split(" ")
        for binaries in whole_block_list:
            binaries = zbinstrip(binaries)
            block = []  
            for block_index in range(0,16,4):
                block.append(binaries[block_index:block_index + 4])
            chunk_list.append(block)
    #subdividing the key and iterating it to end phase
    subkey = key_split(key)
    for keys in subkey:
        Key_rotation_template = Key_rotation_template + subkey[keys]
    Key_rotation_template = Key_rotation_template[6*3:] + Key_rotation_template[0:6*3]
    subkey = key_split(Key_rotation_template)
    #reverse encrypting
    for chunk in chunk_list:
        step4 = 2


# key = random_key_generator()
key = "11011100011011110011111101011001"
for i in create_subkeys(key):
    print(i)
message = "1001110010101100"
encrypted_message = IDEA_encryption(message,key,False,"binary")
print((encrypted_message))
# decode(encrypted_message,key)

#iiiio