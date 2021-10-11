a = "10100"
b = "01110"
c = 14
d = [1,2,1,2,[1,1,2,4,],1,1,1,[1,1,2,522,5,2,6]]
e = "1234567, hey"
f = [2,2]
for i in f :
    f.clear()
print(f)

 step1 = (int(chunk_block[0],2) * int(subkey["k1"],2)) % 17 
            step2 = (int(chunk_block[1],2) + int(subkey["k2"],2)) % 16
            step3 = (int(chunk_block[2],2) + int(subkey["k3"],2)) % 16
            step4 = (int(chunk_block[3],2) * int(subkey["k4"],2)) % 17
            step5 = step1 ^ step3
            step6 = step2 ^ step4
            step7 = (step5 * int(subkey["k5"],2)) % 17
            step8 = (step6 + step7) % 16
            step9 = (step8 * int(subkey["k6"],2)) % 17
            step10 = (step7 + step9) % 16
            step11 = step1 ^ step9
            step12 = step3 ^ step9
            step13 = step2 ^ step10
            step14 = step9 ^ step10
            chunk_block[0] = zbinstrip(step11)
            chunk_block[1] = binstrip(step13)
            chunk_block[2] = binstrip(step12)
            chunk_block[3] = binstrip(step14)
            Key_rotation_template = ""
            for keys in subkey:
                Key_rotation_template = Key_rotation_template + subkey[keys]
            Key_rotation_template = Key_rotation_template[6:] + Key_rotation_template[0:6]
            subkey = key_split(Key_rotation_template)
        #last round somme differences
        step1 = (int(chunk_block[0],2) * int(subkey["k1"],2)) % 17 
        step2 = (int(chunk_block[1],2) + int(subkey["k2"],2)) % 16
        step3 = (int(chunk_block[2],2) + int(subkey["k3"],2)) % 16
        step4 = (int(chunk_block[3],2) * int(subkey["k4"],2)) % 17
        step5 = step1 ^ step3
        step6 = step2 ^ step4
        step7 = (step5 * int(subkey["k5"],2)) % 17
        step8 = (step6 + step7) % 16
        step9 = (step8 * int(subkey["k6"],2)) % 17
        step10 = (step7 + step9) % 16
        step11 = step1 ^ step9
        step12 = step3 ^ step9
        step13 = step2 ^ step10
        step14 = step9 ^ step10
        chunk_block[0] = binstrip(step11)
        chunk_block[1] = binstrip(step12)
        chunk_block[2] = binstrip(step13)
        chunk_block[3] = binstrip(step14)
        step1 = (int(chunk_block[0],2) * int(subkey["k1"],2)) % 17 
        step2 = (int(chunk_block[1],2) + int(subkey["k2"],2)) % 16
        step3 = (int(chunk_block[2],2) + int(subkey["k3"],2)) % 16
        step4 = (int(chunk_block[3],2) * int(subkey["k4"],2)) % 17
        chunk_block[0] = zbinstrip(step11,4)
        chunk_block[1] = zbinstrip(step12,4)
        chunk_block[2] = zbinstrip(step13,4)
        chunk_block[3] = zbinstrip(step14,4)

#step4 = x * k % 17
3 = x *2 % 17
3/x=2%17

(x*15) % 17 = 8
(x*15) % 17 = 8

10*3=1


