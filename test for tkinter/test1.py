import tkinter as tk
from tkinter import ttk
from Profile import Post,Profile

window=tk.Tk()
window.title("first GUI")
window.geometry("720x480")

menu_bar=tk.Menu(window)
window.config(menu=menu_bar)
menu_file=tk.Menu(menu_bar)
menu_bar.add_cascade(menu=menu_file,label="File")
menu_file.add_command(label="New")

window.update()
window.minsize(window.winfo_width(),window.winfo_height())


window.mainloop()
