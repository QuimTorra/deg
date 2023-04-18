from tkinter import *
from tkinter.scrolledtext import ScrolledText
import random
import string
import re

bannedWords = {
    "amposta": "Tortosa",
    "terrassa": "Sabadell",
}


def random_char(event):
    prob = 0.05
    prob_trole = 0
    if random.random() < prob:
        if random.random() > prob_trole:
            if event.char != " " and event.char != "\r" and event.char != "\x08":
                random_char = random.choice(string.ascii_letters)
                event.widget.insert(INSERT, random_char)
                return "break"

def update(event):
    deglight(event)
    bwords(event)


def deglight(event):
    event.widget.tag_remove("deglight", "1.0", END)
    start = "1.0"
    while True:
        start = event.widget.search("deg", start, END, regexp=True)
        if not start:
            break
        end = f"{start}+{len('deg')}c"
        event.widget.tag_add("deglight", start, end)
        start = end

def bwords(event):
    text = event.widget
    # Get the current cursor position
    cursor_pos = text.index("insert")

    # Get the current text in the text area
    text_content = text.get("1.0", END)

    # Replace the banned words with their replacements using regex
    for banned_word, replacement in bannedWords.items():
        regex = re.compile(rf"{banned_word}", re.IGNORECASE)
        text_content = regex.sub(replacement, text_content)

    # Update the text area with the new content
    text.delete("1.0", END)
    text.insert("1.0", text_content)

    # Set the cursor back to its original position
    text.mark_set("insert", cursor_pos)