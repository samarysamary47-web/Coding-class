import tkinter as tk

root = tk.Tk()
root.geometry("625x500")

def convert():
    global Farenheit

    Farenheit = (float(celcius) * 9/5) + 32
    Farenheit_Label.config(text="")
    Farenheit_Label.config(text="Farenheit: {}".format(Farenheit))

Title = tk.Label(text="Temperature Converter",
                 font=("Times",45,"bold"),
                 background=("orange"))

Title.pack(pady=6)

tip = tk.Label(font=("Times",25,"bold"),
               foreground="grey",
               text="Celcius -> Farenheit")

tip.pack(pady=25)

Celcius_text = tk.Label(font=("Times",25,"bold"),
               text="Enter the Celcius:")

Celcius_text.pack()

Celcius_box = tk.Entry(root,
                       font=("Times",25,"bold"))

Celcius_box.pack()

Celcius_box.insert(tk.INSERT,"0")

celcius = Celcius_box.get()
Farenheit = (int(celcius) * 9/5) + 32

Farenheit_Label = tk.Label(root,
                           font=("Times",25,"bold"),
                           text="Farenheit:")

Farenheit_Label.pack(pady=25)

Converter = tk.Button(root,
                      text="convert",
                      font=("Times",25,"bold"),
                      background="lightgreen",
                      command=convert)

Converter.pack(pady=25)

root.mainloop()
