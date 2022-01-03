from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pw_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pw_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pw = pw_letters + pw_symbols + pw_numbers

    random.shuffle(pw)
    result = ''.join(pw)
    password_txt.insert(0, result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_txt.get()
    user = username_txt.get()
    password = password_txt.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details Entered:\n\tUser: {user}\n\tPassword:{password}"
                                                              f"\n\nIs this ok to save?")
        if is_ok:
            with open("./data.txt", "a") as file:
                file.write(f"{website} | {user} | {password}\n")
            website_txt.delete(0, END)
            username_txt.delete(0, END)
            password_txt.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(height=200, width=200, highlightthickness=0)
img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)
website_txt = Entry(width=54)
website_txt.focus()
website_txt.grid(column=1, row=1, columnspan=2)

username_lbl = Label(text="Email/Username:")
username_lbl.grid(column=0, row=2)
username_txt = Entry(width=54)
username_txt.insert(0, "example@gmail.com")
username_txt.grid(column=1, row=2, columnspan=2)

password_lbl = Label(text="Password:")
password_lbl.grid(column=0, row=3)
password_txt = Entry(width=35)
password_txt.grid(column=1, row=3)

generate_pass_btn = Button(text="Generate Password", command=generate_pass)
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=46, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

# All code before exit
window.mainloop()
