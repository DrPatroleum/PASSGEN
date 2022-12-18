from tkinter import *
import string
import secrets


def click():
    if (check_numbers.get() == 1) and (check_letters.get() == 1) and (check_special_characters.get() == 1):
        generate_full()
    if (check_numbers.get() == 1) and (check_letters.get() == 1) and (check_special_characters.get() == 0):
        generate_letters_num()
    if (check_numbers.get() == 1) and (check_letters.get() == 0) and (check_special_characters.get() == 1):
        generate_num_spec()
    if (check_numbers.get() == 0) and (check_letters.get() == 1) and (check_special_characters.get() == 1):
        generate_letters_spec()
    if (check_numbers.get() == 1) and (check_letters.get() == 0) and (check_special_characters.get() == 0):
        generate_numbers_only()
    if (check_numbers.get() == 0) and (check_letters.get() == 1) and (check_special_characters.get() == 0):
        generate_letters_only()
    if (check_numbers.get() == 0) and (check_letters.get() == 0) and (check_special_characters.get() == 1):
        generate_spec_only()
    label4 = Label(window,
                   text="The password has been copied to clipboard!")
    label4.pack()


def copy_option(password):
    window.clipboard_clear()
    window.clipboard_append(password)


def create_result(password):
    label3.config(text=password)
    copy_option(password)


def generate_full():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(full_alphabet))
    create_result(password)


def generate_letters_num():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(letters_num))
    create_result(password)


def generate_num_spec():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(num_spec))
    create_result(password)


def generate_letters_spec():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(letters_spec))
    create_result(password)


def generate_numbers_only():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(digits))
    create_result(password)


def generate_letters_only():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(letters))
    create_result(password)


def generate_spec_only():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(special_chars))
    create_result(password)


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

full_alphabet = letters + digits + special_chars
letters_num = letters + digits
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

check_numbers = IntVar()
check_button_numbers = Checkbutton(window,
                                   text="Numbers",
                                   variable=check_numbers)
check_button_numbers.pack()

check_letters = IntVar()
check_button_letters = Checkbutton(window,
                                   text="Letters",
                                   variable=check_letters)
check_button_letters.pack()

check_special_characters = IntVar()
check_button_special = Checkbutton(window,
                                   text="Special Characters",
                                   variable=check_special_characters)
check_button_special.pack()

pass_len = IntVar()
scale = Scale(window,
              from_=8,
              to=24,
              length=250,
              orient=HORIZONTAL,
              tickinterval=4,
              showvalue=1,
              resolution=1,
              variable=pass_len)
scale.pack()

gen_button = Button(window,
                    text="GENERATE",
                    command=click,
                    state=ACTIVE,
                    compound="center")
gen_button.pack()

label2 = Label(window,
               text="Generated password is:")
label2.pack()

label3 = Label(window)
label3.pack()

window.mainloop()
