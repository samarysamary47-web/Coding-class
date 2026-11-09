import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

root.config(background="green",relief="solid",cursor="hand2")

name = tk.Label(text="Miguel",font=("Times",25,"bold"))
name.pack()

root.mainloop()