import random


def printmatrix(matrix):
    for row in matrix:
        print(row)


class Key:
    def __init__(self, numOfRots=3, length=32, subkeyLength=4):
        self.rots = numOfRots
        self.length = length
        self.subkeyLength = subkeyLength
        self.key = []

        self.keyRot = []
        self.keyRound = []

    def AddToRot(self, key):
        self.keyRot.append(key)

    def Generate(self):
        self.key = []
        for bit in range(self.length):
            if bit % self.subkeyLength == 0:
                self.key.append("")
            self.key[bit // self.subkeyLength] += str(random.choice((0, 1)))
        self.AddToRot(self.key)

    def RotateKey(self, key, num=6):
        stringKey = ""
        for subkey in key:
            stringKey += subkey
        newStringKey = stringKey[num:] + stringKey[:num]
        newKey = []
        for bit in range(len(newStringKey)):
            if bit % self.subkeyLength == 0:
                newKey.append("")
            newKey[bit // self.subkeyLength] += newStringKey[bit]
        self.AddToRot(newKey)

    def OrganiseKeyRounds(self, rounds=6):
        roundIndex = 0
        self.keyRound.append([])
        for key in self.keyRot:
            for subkey in key:
                self.keyRound[roundIndex].append(subkey)
                if len(self.keyRound[roundIndex]) == rounds:
                    roundIndex += 1
                    self.keyRound.append([])
        if len(self.keyRound[-1]) != rounds:
            self.keyRound.pop(-1)


def StringToBin(string):  # Converts a string to a list containing each character devided into 4 chunks of 4 bits
    binaryString = []
    for char in range(len(string)):
        binaryString.append([])
        code = ord(string[char])
        binaryLetter = bin(code)[2:]
        binaryLetter = FillBin(binaryLetter, 16)
        for i in range(0, len(binaryLetter), 4):
            binaryString[char].append(str(binaryLetter[i:i + 4]))
    return binaryString


def StripBin(binary):
    if 'b' in binary:
        return binary[2:]
    else:
        return binary


def FillBin(binary, length):
    binary = StripBin(binary)
    if len(binary) < length:
        binary = (length - len(binary)) * '0' + binary
    elif len(binary) > length:
        binary = binary[-4:]
    return binary

### OPERATIONS ###
def Mul(bin1, bin2):  # Multiplication modulo 17
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    result = bin((num1 * num2) % 17)
    return FillBin(result, 4)


def Add(bin1, bin2):  # Addition modulo 16
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    result = bin((num1 + num2) % 16)
    return FillBin(result, 4)


def XOR(bin1, bin2):  # Bitwise XOR
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    result = bin(num1 ^ num2)
    return FillBin(result, 4)


### Encryption algorithm ###
def Encrypt(chunks, key, rounds=4):
    for i in range(rounds):
        step1 = Mul(chunks[0], key.keyRound[i][0])
        step2 = Add(chunks[1], key.keyRound[i][1])
        step3 = Add(chunks[2], key.keyRound[i][2])
        step4 = Mul(chunks[3], key.keyRound[i][3])
        step5 = XOR(step1, step3)
        step6 = XOR(step2, step4)
        step7 = Mul(step5, key.keyRound[i][4])
        step8 = Add(step6, step7)
        step9 = Mul(step8, key.keyRound[i][5])
        step10 = Add(step7, step9)
        step11 = XOR(step1, step9)
        step12 = XOR(step3, step9)
        step13 = XOR(step2, step10)
        step14 = XOR(step4, step10)
        if i == 0:
            chunks = [step11, step13, step12, step14]
        else:
            chunks = [step11, step12, step13, step14]
    step1 = Mul(chunks[0], key.keyRound[-1][0])
    step2 = Add(chunks[1], key.keyRound[-1][1])
    step3 = Add(chunks[2], key.keyRound[-1][2])
    step4 = Mul(chunks[3], key.keyRound[-1][3])
    chunks = [step1, step2, step3, step4]
    return chunks


### MAIN ###
def main():
    # key = Key(length=128, subkeyLength=16)
    key = Key()
    # key.Generate()
    key.keyRot = [['1101', '1100', '0110', '1111', '0011', '1111', '0101', '1001']]
    for i in range(3):
        key.RotateKey(key.keyRot[i])
    key.OrganiseKeyRounds()
    printmatrix(key.keyRound)
    print("")

    
    # binaryPlaintext = StringToBin('h')
    binaryPlaintext = [['1001', '1100', '1010', '1100']]
    print(binaryPlaintext)
    cypherText = []
    for index, char in enumerate(binaryPlaintext):
        cypherText.append([])
        cypherText[index] = Encrypt(char, key)
    print(cypherText)


if __name__ == '__main__':
    main()
