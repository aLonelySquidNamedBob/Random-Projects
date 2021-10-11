from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as Keyboard, Key
import time
import requests
from bs4 import BeautifulSoup

artist = input('Artist: ')
song = input("Song: ")

artist_n = ""
song_n = ""


def format_text(text):
    return text.strip().lower().replace(' ', '').replace("'", "").replace('.', '')\
        .replace('é', 'e').replace('è', 'e').replace('ç', 'c').replace('à', 'a')


artist_f = format_text(artist)
song_f = format_text(song)

URL = f"https://www.azlyrics.com/lyrics/{artist_f}/{song_f}.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find(class_='col-xs-12 col-lg-8 text-center')
container = content.find_all('div', _class=None)
lyrics = container[5].text.strip()

for word in artist.split(' '):
    artist_n += word.capitalize()
    artist_n += ' '

for word in song.split(' '):
    song_n += word.capitalize()
    song_n += ' '

file = open('lyrics.txt', 'w')
file.write(song_n.strip() + ' - ' + artist_n.strip() + '\n')
file.write(lyrics)
file.close()
file.close()

file = open('lyrics.txt', 'r')

mouse = Controller()
keyboard = Keyboard()

mouse.position = (361, 1050)
mouse.click(Button.left, 1)

time.sleep(1)

mouse.position = (1000, 1000)
mouse.click(Button.left, 1)

for line in file.readlines():
    keyboard.type(line)
    keyboard.press(Key.enter)
    time.sleep(0.2)

file.close()
