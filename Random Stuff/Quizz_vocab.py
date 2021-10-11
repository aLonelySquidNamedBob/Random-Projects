import random
import os

f = open("vocab.txt", "r")

lines = f.readlines()
dest = "foreign"

foreign = []
translated = []
frequence = []

praise = ["très bien", "génial", "fantastique", "parfait", "top", "excellent", "formidable"]
insults = ["TU ES NUL", "TU NE SERS A RIEN", "MON CHAT POURRAIT FAIRE MIEUX", "C'EST PAS COMME ÇA QUE T'AURA TON BAC", "NON MAIS HO"]

num = 0


def format_text(text, index):
    global num, dest
    text = text.removesuffix("\n")
    text = text.removeprefix(str(index + 1 - num) + ".")
    text = text.removeprefix("\t")

    text = text.replace("Ã¤", "ä")
    text = text.replace("ïƒ\xa0", "->")
    text = text.replace("â‰\xa0", "!=")
    text = text.replace("Ã¶", "ö")
    text = text.replace("Ã¼", "ü")
    text = text.replace("Â°", "°")
    text = text.replace("Ã\xa0", "à")
    text = text.replace("Ã©", "é")
    text = text.replace("Ã‰", "É")
    text = text.replace("Ã¨", "è")
    text = text.replace("Ãª", "ê")
    text = text.replace("â€™", "'")

    text = text.split('->')
    text = text[0]
    text = text.split("+")
    text = text[0]

    if text == '':
        dest = "translated"
        num = index + 1
    elif dest == "foreign":
        foreign.append(text)
    else:
        translated.append(text)


def used(a_question, l_question, index, counter):
    global frequence, translated
    if counter > 30:
        print("Fini")
        quit()
    if frequence[index] > 1 or a_question == l_question:
        print("NON, pas " + a_question.lower())
        a_question = random.choice(translated)
        a_question = used(a_question, l_question, translated.index(a_question), counter + 1)
    return a_question


for index, line in enumerate(lines):
    format_text(line, index)

frequence = [0] * len(translated)
last_question = None

while True:

    question = random.choice(translated)
    question = used(question, last_question, translated.index(question), 0)

    correct_answer = foreign[translated.index(question)]
    answer = input(question + " : ")

    if answer.lower().strip() == correct_answer.lower().strip():
        print(random.choice(praise).capitalize() + "!")
    else:
        print(correct_answer)
        print(random.choice(insults) + " " + "!" * random.randint(0, 4))

    frequence[translated.index(question)] += 1
    print(frequence[translated.index(question)])
    print(frequence)
    print()
    last_question = question
