from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_lbl = Label(text="Website:", bg="white")
website_lbl.grid(column=0, row=1)
website_txt = Entry(width=35)
website_txt.grid(column=1, row=1, columnspan=2)

username_lbl = Label(text="Email/Username:", bg="white")
username_lbl.grid(column=0, row=2)
username_txt = Entry(width=35)
username_txt.grid(column=1, row=2, columnspan=2)

password_lbl = Label(text="Password:", bg="white")
password_lbl.grid(column=0, row=3)
password_txt = Entry(width=17)
password_txt.grid(column=1, row=3)

generate_pass_btn = Button(text="Generate Password")
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36)
add_btn.grid(column=1, row=4, columnspan=2)

# All code before exit
window.mainloop()
