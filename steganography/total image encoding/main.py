from PIL import Image
import math
import string

with open("total image encoding\wiki.txt") as f:
    message = f.read()

global alphabet
alphabet = []

for letter in string.printable:
    alphabet.append(letter)

image = Image.new("RGB", (math.ceil(math.sqrt(len(message))), math.ceil(math.sqrt(len(message)))))
pixels = image.load()


def encode(message):
    posInString = 0
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if posInString < len(message):
                if message[posInString] in string.printable:
                    pixels[x, y] = ((alphabet.index(message[posInString]) + 1),
                                    (alphabet.index(message[posInString]) + 1),
                                    (alphabet.index(message[posInString]) + 1))
            posInString += 1
    image.save("image.png")


def decode():
    encoded_image = Image.open("total image encoding\image.png")
    encoded_pixels = encoded_image.load()

    message = ""

    for y in range(encoded_image.size[1]):
        for x in range(encoded_image.size[0]):
            if encoded_pixels[x, y] != (0, 0, 0):
                message += alphabet[(encoded_pixels[x, y][0]) - 1]

    return message


# encode(message)
print(decode())