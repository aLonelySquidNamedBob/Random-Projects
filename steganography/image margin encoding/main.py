from PIL import Image
import string


# determines the number of margins needed to fit the message
def margin_size(image_size, message):
    message_length = len(message)
    margin_capacity = 0
    x = image_size[0]
    y = image_size[1]
    marginSize = 0
    while message_length >  margin_capacity:
        margin_capacity += (x * 2) + (y * 2) - 4
        x -= 2
        y -= 2
        marginSize += 1
    return marginSize


# creating the letter encoding dictionary
def dictionary():
    alphabet = {}
    color_value_a = [0, 0, 0]
    color_derivation = 4
    test_list = []
    for letters in string.printable:
        alphabet[letters] = list(color_value_a)
        # determines next RGB value
        color_value_a[0] += 1
        for i in range(3):
            if color_value_a[i] > color_derivation:
                color_value_a[i] = 0
                # catches error of too small color range
                if color_value_a[-1] >= color_derivation:
                    print("too many elements for the given color range")
                    color_value_a = [0, 0, 0]
                else:
                    color_value_a[i + 1] += 1
    # converting the list rgb values in tuppel values
    rgb_alphabet = {}
    for i in alphabet:
        rgb_alphabet[i] = tuple(alphabet[i])
    return rgb_alphabet


# encoding the message
def encode(image_name, message):
    # opening image create empty canvas to proces
    input_image = Image.open(image_name)
    output_image = Image.open(image_name)
    output_image = output_image.convert("RGB")
    output_pixels = output_image.load()
    # establishing the color match table
    letter_color_matching = dictionary()
    #adding end comand to the message
    message += "\end"
    # determining the margin size
    margin = margin_size(input_image.size, message)
    # making the margin
    for y in range(input_image.size[1]):
        for x in range(input_image.size[0]):
            # cheking if in margin boundries
            if y <= margin:
                output_pixels[x, y] = (0, 0, 0)
            elif y >= input_image.size[1] - margin - 1:
                output_pixels[x, y] = (0, 0, 0)
            elif x <= margin:
                output_pixels[x, y] = (0, 0, 0)
            elif x >= input_image.size[0] - margin - 1:
                output_pixels[x, y] = (0, 0, 0)
    # making the encoded margins
    message_index = 0
    for y in range(input_image.size[1]):
        for x in range(input_image.size[0]):
            if message_index < len(message):
                if message[message_index] in string.printable:
                    # cheking if in margin boundries
                    if y <= margin:
                        output_pixels[x, y] = tuple(letter_color_matching[message[message_index]])
                        message_index += 1
                    elif y >= input_image.size[1] - margin - 1:
                        output_pixels[x, y] = tuple(letter_color_matching[message[message_index]])
                        message_index += 1
                    elif x <= margin:
                        output_pixels[x, y] = tuple(letter_color_matching[message[message_index]])
                        message_index += 1
                    elif x >= input_image.size[0] - margin - 1:
                        output_pixels[x, y] = tuple(letter_color_matching[message[message_index]])
                        message_index += 1
                else:
                    message_index += 1
    # svaing the outputteg image
    output_image.save("image margin encoding\output_image.png")


def decode(image_name):
    # preparing the image for process
    color_deviation = 4
    input_image = Image.open(image_name)
    input_image = input_image.convert("RGB")
    input_pixels = input_image.load()
    # finding the margin width
    max_rgb_value = 0
    xy_ofset = -1
    while max_rgb_value <= 4:
        xy_ofset += 1
        for i in input_pixels[input_image.size[0] // 2, xy_ofset]:
            if i > max_rgb_value:
                max_rgb_value = i
    margin = xy_ofset
    # generating the reverse collor matching dictionary
    char_to_rgb = dictionary()
    rgb_to_char = {}
    for i in char_to_rgb:
        rgb_to_char[char_to_rgb[i]] = i
    # decoding the margins
    message = ""
    end_comand = False
    for y in range(input_image.size[1]):
        for x in range(input_image.size[0]):
            if input_pixels[x, y] in rgb_to_char:
                # cheking if the message is finished
                if end_comand == False:
                    # cheking if in margin boundries
                    if y <= margin:
                        message += rgb_to_char[input_pixels[x, y]]
                    elif y >= input_image.size[1] - margin - 1:
                        message += rgb_to_char[input_pixels[x, y]]
                    elif x <= margin:
                        message += rgb_to_char[input_pixels[x, y]]
                    elif x >= input_image.size[0] - margin -1 :
                        message += rgb_to_char[input_pixels[x, y]]
                    # detecting \end command
                    if len(message) > 4:
                        end_segment = ""
                        for i in range(len(message)-4,len(message)):
                            end_segment += message[i]
                        if end_segment == "\end":
                            end_comand = True
    message.replace("\end","")
    return message


my_message = """hey ca va bien"""
encode("image margin encoding\image1.png", my_message)
print(decode("image margin encoding\output_image.png"))
