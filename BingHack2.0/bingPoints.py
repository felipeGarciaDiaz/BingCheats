import tkinter as tk
import random
import webbrowser
import os
import time
import winsound
from PIL import ImageTk, Image

gui = tk.Tk()
gui.resizable(width=False, height=False)
gui.iconbitmap(os.path.dirname(__file__) + "\\Media\\Pylot.ico")
gui.configure(background="#fcfaf9")
gui.title("Searcher")
gui.geometry("600x300")
logo = ImageTk.PhotoImage(Image.open(os.path.dirname(__file__) + "\\Media\\mountainLogo.png"))
slot = tk.Label(gui, image=logo)
slot.pack(side="top", fill="none", expand="yes")
greeting = tk.Label(gui, text="Press ENTER to proceed", background="#fcfaf9")
greeting.place(x=230, y=273)


def start_program(event):
    slot.destroy()
    greeting.destroy()
    main = tk.Label(gui, text="Searcher", background="#fcfaf9", font = ("IMPACT", 30), fg = "#a3d3bd")
    main.place(x=220, y=10)
    searchamount = tk.Text(width=30, height=1, background="#ded0c2", relief="flat")
    searchamount.place(x=180, y=70)
    searchamount.insert("1.0", "Insert Search amount here")
    searchspeed = tk.Text(width=30, height=1, background="#ded0c2", relief="flat")
    searchspeed.place(x=180, y=95)
    searchspeed.insert("1.0", "Insert Search speed here")
    multiamt = tk.Text(width=30, height=1, background="#ded0c2", relief="flat")
    multiamt.place(x=180, y=120)
    multiamt.insert("1.0", "Insert amount of words")

    def choose_engine(name, ux, uy):

        def change_engine():
            global url
            if name is "Bing":
                url = "https://www.bing.com/search?q="
            if name is "Google":
                url = "https://www.google.com/search?q="
            if name is "Yahoo":
                url = "https://search.yahoo.com/search?p="
            if name is "DuckDuckGo":
                url = "https://duckduckgo.com/?q="
        urlbutton = tk.Button(gui, text=name, width=20, command=change_engine, relief="flat", bg="#699882", fg="#fff")
        urlbutton.place(x=ux, y=uy)

    choose_engine("Bing", 100, 150)
    choose_engine("Google", 350, 150)
    choose_engine("Yahoo", 100, 185)
    choose_engine("DuckDuckGo", 350, 185)

    def read_list():
        datalist = open(os.path.dirname(__file__) + "\\Words\\words.txt").readlines()
        amtlines = len(datalist)
        for i in range(amtlines):
            lines = datalist[random.randrange(1, amtlines)]
        return lines

    def scavange_web():

        def multi_obfuscation(amt):
            search = []
            for i in range(amt):
                search.append(read_list())
            return " ".join(search)
        try:
            for i in range(int(searchamount.get("1.0", "end"))):
                time.sleep(int(searchspeed.get("1.0", "end")))
                webbrowser.open(url + multi_obfuscation(int(multiamt.get("1.0", "end"))), new=2)
        except ValueError:
            winsound.Beep(400, 250)
            print(ValueError)
    scavange = tk.Button(gui, text="SEARCH", command=scavange_web, width=50, height=2, relief="flat", bg="#547968", fg="#fff")
    scavange.place(x=120, y=240)


gui.bind("<Return>", start_program)
gui.mainloop()
