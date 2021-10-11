ma = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ",": "----",
    " ": "/"
}

inverseMorseAlphabet = dict((v, k) for (k, v) in ma.items())


def decodeMorse(code, positionInString=0):
    if positionInString < len(code):
        morseLetter = ""
        for key, char in enumerate(code[positionInString:]):
            if char == "+":
                positionInString = key + positionInString + 1
                letter = inverseMorseAlphabet[morseLetter]
                return letter + decodeMorse(code, positionInString)

            else:
                morseLetter += char
    else:
        return ""


def encodeToMorse(message):
    encodedMessage = ""
    for char in message[:]:
        encodedMessage += ma[char.upper()] + "+"
    return encodedMessage

def morse():
    txt = input("encode e/ decode d :")

    if txt == "e":
        enc = encodeToMorse(input("message to encode : "))
        print(enc)

    elif txt == "d":
        f = input("code to decode : ") + "+"
        decoded = decodeMorse(f)
        print(decoded)

    else:
        quit()

while True:
    morse()
