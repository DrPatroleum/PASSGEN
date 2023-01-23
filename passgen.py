from tkinter import *
import string
import secrets
import time


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
    label5 = Label(window,
                   text="The password has been copied to clipboard!")
    label5.pack()


def clear():
    label1.after(1000, label1.destroy())
    label2.after(1000, label2.destroy())
    label3.after(1000, label3.destroy())
    #label4.after(1000, label4.destroy())
    #label5.after(1000, label5.destroy())

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
    if pass_len.get() == 8:
        txt = "Hacker need 8 hours to crack this password"
    if pass_len.get() == 9:
        txt = "Hacker need 3 weeks to crack this password"
    if pass_len.get() == 10:
        txt = "Hacker need 5 years to crack this password"
    if pass_len.get() == 11:
        txt = "Hacker need 400 years to crack this password"
    if pass_len.get() == 12:
        txt = "Hacker need 34k years to crack this password"
    if pass_len.get() == 13:
        txt = "Hacker need 2m years to crack this password"
    if pass_len.get() == 14:
        txt = "Hacker need 200m years to crack this password"
    if pass_len.get() == 15:
        txt = "Hacker need 15bn years to crack this password"
    if pass_len.get() == 16:
        txt = "Hacker need 1tn years to crack this password"
    if pass_len.get() == 17:
        txt = "Hacker need 93tn years to crack this password"
    if pass_len.get() == 18:
        txt = "Hacker need 7qd years to crack this password"
        #moze warto ogarnac to jakims slownikiem
    label4 = Label(window,
                   text=txt)
    label4.pack()


def generate_letters_num():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(letters_num))
    create_result(password)
    if pass_len.get() == 8:
        txt = "Hacker need 1 hour to crack this password"
    if pass_len.get() == 9:
        txt = "Hacker need 3 days to crack this password"
    if pass_len.get() == 10:
        txt = "Hacker need 7 months to crack this password"
    if pass_len.get() == 11:
        txt = "Hacker need 41 years to crack this password"
    if pass_len.get() == 12:
        txt = "Hacker need 2k years to crack this password"
    if pass_len.get() == 13:
        txt = "Hacker need 100k years to crack this password"
    if pass_len.get() == 14:
        txt = "Hacker need 9m years to crack this password"
    if pass_len.get() == 15:
        txt = "Hacker need 600m years to crack this password"
    if pass_len.get() == 16:
        txt = "Hacker need 37bn years to crack this password"
    if pass_len.get() == 17:
        txt = "Hacker need 2tn years to crack this password"
    if pass_len.get() == 18:
        txt = "Hacker need 100tn years to crack this password"
    label4 = Label(window,
                   text=txt)
    label4.pack()

def generate_num_spec():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(num_spec))
    create_result(password)
    if pass_len.get() == 8:
        txt = "Hacker need 8 hours to crack this password"
    if pass_len.get() == 9:
        txt = "Hacker need 3 weeks to crack this password"
    if pass_len.get() == 10:
        txt = "Hacker need 5 years to crack this password"
    if pass_len.get() == 11:
        txt = "Hacker need 400 years to crack this password"
    if pass_len.get() == 12:
        txt = "Hacker need 34k years to crack this password"
    if pass_len.get() == 13:
        txt = "Hacker need 2m years to crack this password"
    if pass_len.get() == 14:
        txt = "Hacker need 200m years to crack this password"
    if pass_len.get() == 15:
        txt = "Hacker need 15bn years to crack this password"
    if pass_len.get() == 16:
        txt = "Hacker need 1tn years to crack this password"
    if pass_len.get() == 17:
        txt = "Hacker need 93tn years to crack this password"
    if pass_len.get() == 18:
        txt = "Hacker need 7qd years to crack this password"
    label4 = Label(window,
                   text=txt)
    label4.pack()

def generate_letters_spec():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(letters_spec))
    create_result(password)
    if pass_len.get() == 8:
        txt = "Hacker need 8 hours to crack this password"
    if pass_len.get() == 9:
        txt = "Hacker need 3 weeks to crack this password"
    if pass_len.get() == 10:
        txt = "Hacker need 5 years to crack this password"
    if pass_len.get() == 11:
        txt = "Hacker need 400 years to crack this password"
    if pass_len.get() == 12:
        txt = "Hacker need 34k years to crack this password"
    if pass_len.get() == 13:
        txt = "Hacker need 2m years to crack this password"
    if pass_len.get() == 14:
        txt = "Hacker need 200m years to crack this password"
    if pass_len.get() == 15:
        txt = "Hacker need 15bn years to crack this password"
    if pass_len.get() == 16:
        txt = "Hacker need 1tn years to crack this password"
    if pass_len.get() == 17:
        txt = "Hacker need 93tn years to crack this password"
    if pass_len.get() == 18:
        txt = "Hacker need 7qd years to crack this password"
    label4 = Label(window,
                   text=txt)
    label4.pack()

def generate_numbers_only():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(digits))
    create_result(password)
    if pass_len.get() == 8:
        txt = "Hacker need no time to crack this password"
    if pass_len.get() == 9:
        txt = "Hacker need no time to crack this password"
    if pass_len.get() == 10:
        txt = "Hacker need no time to crack this password"
    if pass_len.get() == 11:
        txt = "Hacker need 2 secs to crack this password"
    if pass_len.get() == 12:
        txt = "Hacker need 25 secs to crack this password"
    if pass_len.get() == 13:
        txt = "Hacker need 4 mins to crack this password"
    if pass_len.get() == 14:
        txt = "Hacker need 41 mins to crack this password"
    if pass_len.get() == 15:
        txt = "Hacker need 6 hours to crack this password"
    if pass_len.get() == 16:
        txt = "Hacker need 2 days to crack this password"
    if pass_len.get() == 17:
        txt = "Hacker need 4 weeks to crack this password"
    if pass_len.get() == 18:
        txt = "Hacker need 9 months to crack this password"
    label4 = Label(window,
                   text=txt)
    label4.pack()

def generate_letters_only():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(letters))
    create_result(password)
    if pass_len.get() == 8:
        txt = "Hacker need 22 mins to crack this password"
    if pass_len.get() == 9:
        txt = "Hacker need 19 hours to crack this password"
    if pass_len.get() == 10:
        txt = "Hacker need 1 month to crack this password"
    if pass_len.get() == 11:
        txt = "Hacker need 5 years to crack this password"
    if pass_len.get() == 12:
        txt = "Hacker need 300 years to crack this password"
    if pass_len.get() == 13:
        txt = "Hacker need 16k years to crack this password"
    if pass_len.get() == 14:
        txt = "Hacker need 800k years to crack this password"
    if pass_len.get() == 15:
        txt = "Hacker need 43m years to crack this password"
    if pass_len.get() == 16:
        txt = "Hacker need 2bn years to crack this password"
    if pass_len.get() == 17:
        txt = "Hacker need 100bn years to crack this password"
    if pass_len.get() == 18:
        txt = "Hacker need 6tn years to crack this password"
    label4 = Label(window,
                   text=txt)
    label4.pack()

def generate_spec_only():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(special_chars))
    create_result(password)
    if pass_len.get() == 8:
        txt = "Hacker need 8 hours to crack this password"
    if pass_len.get() == 9:
        txt = "Hacker need 3 weeks to crack this password"
    if pass_len.get() == 10:
        txt = "Hacker need 5 years to crack this password"
    if pass_len.get() == 11:
        txt = "Hacker need 400 years to crack this password"
    if pass_len.get() == 12:
        txt = "Hacker need 34k years to crack this password"
    if pass_len.get() == 13:
        txt = "Hacker need 2m years to crack this password"
    if pass_len.get() == 14:
        txt = "Hacker need 200m years to crack this password"
    if pass_len.get() == 15:
        txt = "Hacker need 15bn years to crack this password"
    if pass_len.get() == 16:
        txt = "Hacker need 1tn years to crack this password"
    if pass_len.get() == 17:
        txt = "Hacker need 93tn years to crack this password"
    if pass_len.get() == 18:
        txt = "Hacker need 7qd years to crack this password"
    label4 = Label(window,
                   text=txt)
    label4.pack()

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
              to=18,
              length=250,
              orient=HORIZONTAL,
              tickinterval=2,
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
