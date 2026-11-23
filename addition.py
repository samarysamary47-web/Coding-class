import tkinter as tk

root = tk.Tk()
root.title("Mini Adder")
root.geometry("280x200")

heading = tk.Label(
    root,
    text="Enter two numbers:",
    font=("Arial", 10)
)
heading.pack(pady=(20, 8))

num1_entry = tk.Entry(root, width=19, font=("Arial", 10))
num1_entry.pack()
num1_entry.insert(0, "")

num2_entry = tk.Entry(root, width=19, font=("Arial", 10))
num2_entry.pack(pady=3)
num2_entry.insert(0, "")

def add_numbers():

    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())

    result_label.config(
        text=f"Result: {num1 + num2:g}"
    )

add_button = tk.Button(
    root,
    text="Add",
    command=add_numbers,
    bg="lightgreen",
    font=("Arial", 10),
)
add_button.pack(pady=12)

result_label = tk.Label(
    root,
    text="Result: 10",
    font=("Arial", 12, "bold")
)
result_label.pack()

root.mainloop()
