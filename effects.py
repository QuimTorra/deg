from tkinter import *
from tkinter.scrolledtext import ScrolledText
import random
import string
import re


def random_char(event):
    prob = 0.05
    if random.random() < prob:
        if event.char != " " and event.char != "\r" and event.char != "\x08":
            random_char = random.choice(string.ascii_letters)
            event.widget.insert(INSERT, random_char)
            return "break"

def update(event):
    highlight(event)


def highlight(event):
    event.widget.tag_remove("highlight", "1.0", END)
    start = "1.0"
    words = ["deg", "ref"]
    pattern = "|".join(re.escape(word) for word in words)  # Create a regex pattern
    while True:
        start = event.widget.search(pattern, start, END, regexp=True)
        if not start:
            break
        end = f"{start}+{len('deg')}c"
        event.widget.tag_add("highlight", start, end)
        start = end

def bwords(event):
    bannedWords = {
        "amposta": "Tortosa és millor",
        "terrassa": "Sabadell capital del Vallés Occidental i del món en general",
    }

