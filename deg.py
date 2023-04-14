import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font

from effects import random_char, update

class TextEditor:

    def __init__(self, root):
        custom_font = font.Font(family="Comic Sans MS", size=10)
        self.root = root
        self.root.title("deg")
        self.root.geometry("600x400")
        root.option_add("*Font", custom_font)

        self.filename = None
        self.textarea = ScrolledText(self.root, undo=True,)
        self.textarea.bind("<Key>", random_char)
        self.textarea.bind("<KeyRelease>", update)
        self.textarea.configure(font=("Comic Sans MS", 10))
        self.textarea.tag_config("highlight", foreground="blue")
        self.textarea.configure(font=custom_font)
        self.textarea.pack(fill="both", expand=True)

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)

        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_command(label="Save As", command=self.save_file_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit_application)

        self.editmenu.add_command(label="Undo", command=self.undo)
        self.editmenu.add_command(label="Redo", command=self.redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        self.editmenu.add_command(label="Paste", command=self.paste)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="deg", command=self.banwords)

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.root.config(menu=self.menubar)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.filename = None

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("Text Files", "*.txt"),
                                                               ("All Files", "*.*")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(tk.INSERT, f.read())

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.textarea.get(1.0, tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text Files", "*.txt"),
                                                                 ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.textarea.get(1.0, tk.END))
            messagebox.showinfo("File Saved", f"{self.filename} has been saved successfully.")

    def exit_application(self):
        self.root.quit()

    def undo(self):
        self.textarea.edit_undo()

    def redo(self):
        self.textarea.edit_redo()

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")
    
    def banwords(self):
        print(self.bannedWords)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
