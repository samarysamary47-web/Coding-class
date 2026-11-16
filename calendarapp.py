import tkinter as tk
import calendar

def show_calendar():

    calendar_window = tk.Tk()
    calendar_window.geometry("1000x1000")
    calendar_window.title("Calendar")

    calendar_year = int(input.get())
    the_calendar = calendar.calendar(calendar_year)
    calendar_text = tk.Text(calendar_window,
                             width=450,
                             height=450)
    calendar_text.insert(tk.INSERT,the_calendar)
    calendar_text.pack()

    calendar_window.mainloop()

#Line 22 is checking if the window is the main window

if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("500x500")

    root.config(background="lightblue",relief="solid",cursor="hand2")

    Title = tk.Label(text="Calendar",font=("Times",75,"bold"))
    Title.pack()

    input = tk.Entry(root, font=("Times",25,"bold"))
    input.pack()

    year = tk.Label(text="Enter Year", font=("Times",25,"bold"),background="lightgreen")
    year.pack(pady=25)

    calendar_button = tk.Button(text="Show calendar", font=("Times",25,"bold"),background="lightgreen",command=show_calendar)
    calendar_button.pack()

    Exit = tk.Button(text="Exit", font=("Times",25,"bold"),background="red",command=exit)
    Exit.pack(pady=25)

    root.mainloop()