# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import tkinter as tk
from tkinter import ttk

# class PwnRfApp(tk.Frame):
#
#
#
# def main():
#     window = tkinter.Tk()
#     window.title("Welcome title")
#     window.mainloop()
#
#
# if __name__ == '__main__':
#     main()

# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")
#
#         self.label = tk.Label(master, text="This is our first GUI!")
#         self.label.pack()
#
#         self.greet_button = tk.Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()
#
#         self.close_button = tk.Button(master, text="Close", command=master.quit)
#         self.close_button.pack()
#
#     def greet(self):
#         print("Greetings!")
#
#
# def main():
#     root = tk.Tk()
#     my_gui = MyFirstGUI(root)
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.style = ttk.Style()
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Quit button")
        self.style.theme_use("default")

        self.pack(fill=tk.BOTH, expand=1)

        quitButton = ttk.Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)


def main():
    root = tk.Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    # root.mainloop()


    app.mainloop()


if __name__ == '__main__':
    main()