from tkinter import messagebox,simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    facts = {"Bob":"is very smart", "Joe":"is very kind", "Jack":"is very strong"}
    name = simpledialog.askstring("Enter a name", "Enter one of the following names to find out something remarkable about that person. (Bob, Joe, or Jack)").lower()
    fact = ""
    fail = 0
    maximum = 3
    for keys, remark in facts.items():
        if name == keys.lower():
            fact = remark
            name = keys
        else:
            fail += 1
    if fail == maximum:
        messagebox.showinfo("Failed", "Input does not match names")
    else:
        messagebox.showinfo(f"{name}", f"{name} {fact}")
