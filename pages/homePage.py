import tkinter as tk

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label1 = tk.Label(self, text="Home Page")
        label2 = tk.Label(self, text='Choose a position and a year')
        label1.pack(pady=10)
        label2.pack()

        button1 = tk.Button(self, text='Go to Page One', command = lambda: controller.show_frame('PageOne'))
        button2 = tk.Button(self, text='Go to Page Two', command = lambda: controller.show_frame('PageTwo'))

        button1.pack()
        button2.pack()