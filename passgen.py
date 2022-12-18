
from tkinter import messagebox
from tkinter import *
import string
import secrets


def click():
    if (numerki.get() == 1) and (literki.get() == 1) and (spec_znaki.get() == 1):
        generate_full()
    if (numerki.get() == 1) and (literki.get() == 1) and (spec_znaki.get() == 0):
        generate_leters_num()
    if (numerki.get() == 1) and (literki.get() == 0) and (spec_znaki.get() == 1):
        generate_num_spec()
    if (numerki.get() == 0) and (literki.get() == 1) and (spec_znaki.get() == 1):
        generate_letters_spec()
    if (numerki.get() == 1) and (literki.get() == 0) and (spec_znaki.get() == 0):
        generate_numbers_only()
    if (numerki.get() == 0) and (literki.get() == 1) and (spec_znaki.get() == 0):
        generate_letters_only()
    if (numerki.get() == 0) and (literki.get() == 0) and (spec_znaki.get() == 1):
        generate_spec_only()
    label4 = Label(window,
                   text="Your password has been copied to clipboard!")
    label4.pack()
    # generate password


def copy_option(password):
    window.clipboard_clear()
    window.clipboard_append(password)


def generate_full():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(full_alphabet))
    label3.config(text=password)
    copy_option(password)


def generate_leters_num():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(leters_num))
    label3.config(text=password)
    copy_option(password)


def generate_num_spec():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(num_spec))
    label3.config(text=password)
    copy_option(password)


def generate_letters_spec():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(letters_spec))
    label3.config(text=password)
    copy_option(password)


def generate_numbers_only():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(digits))
    label3.config(text=password)
    copy_option(password)


def generate_letters_only():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(letters))
    label3.config(text=password)
    copy_option(password)


def generate_spec_only():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(special_chars))
    label3.config(text=password)
    copy_option(password)


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

full_alphabet = letters + digits + special_chars
leters_num = letters + digits
num_spec = digits + special_chars
letters_spec = letters + special_chars

window = Tk()
window.title("PASSGEN")
window.geometry("300x300")
window.resizable(False, False)
icon = PhotoImage(file='/Users/defcon/Documents/passgen/set.png')
window.iconphoto(True, icon)

label1 = Label(window,
               text="What the password should consist of?")
label1.pack()

numerki = IntVar()
check_button_numbers = Checkbutton(window,
                                   text="Numbers",
                                   variable=numerki)
check_button_numbers.pack()

literki = IntVar()
check_button_letters = Checkbutton(window,
                                   text="Letters",
                                   variable=literki)
check_button_letters.pack()

spec_znaki = IntVar()
check_button_special = Checkbutton(window,
                                   text="Special Characters",
                                   variable=spec_znaki)
check_button_special.pack()

pass_len = IntVar()
scale = Scale(window,
              from_=8,
              to=24,
              length=250,
              orient=HORIZONTAL,
              font=("Arial", 20),
              tickinterval=4,
              showvalue=1,
              resolution=1,
              variable=pass_len)
scale.pack()

gen_button = Button(window,
                    text="GENERATE",
                    command=click,
                    font=("Arial", 24),
                    fg="orange",
                    bg="black",
                    activeforeground="orange",
                    activebackground="black",
                    state=ACTIVE,
                    compound="center")
gen_button.pack()

label2 = Label(window,
               text="Generated password is:")
label2.pack()

label3 = Label(window)
label3.pack()

window.mainloop()
