from tkinter import messagebox,simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    day = "01/26"
    birthday = simpledialog.askstring(title="When is Your birthday?",prompt="Enter your birthday(MM/DD)")
    if birthday == day:
        messagebox.showinfo("Happy Birthday", "Happy Birthday!")
    else:
        messagebox.showinfo("Happy Unbirthday", "Happy Unbirthday!")
