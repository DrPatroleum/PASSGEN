from tkinter import *
from tkinter import messagebox
import string
import secrets
import time

all_characters_dict = {8: '8 hours',
                       9: '3 weeks',
                       10: '5 years',
                       11: '400 years',
                       12: '34k years',
                       13: '2m years',
                       14: '200m years',
                       15: '15bn years',
                       16: '1tn years',
                       17: '93tn years',
                       18: '7qd years'}

letters_num_dict = {8: '1 hour',
                    9: '3 days',
                    10: '7 months',
                    11: '41 years',
                    12: '2k years',
                    13: '100k years',
                    14: '9m years',
                    15: '600m years',
                    16: '37bn years',
                    17: '2tn years',
                    18: '100tn years'}

num_spec_dict = {8: '8 hours',
                 9: '3 weeks',
                 10: '5 years',
                 11: '400 years',
                 12: '34k years',
                 13: '2m years',
                 14: '200m years',
                 15: '15bn years',
                 16: '1tn years',
                 17: '93tn years',
                 18: '7qd years'}

letters_spec_dict = {8: '8 hours',
                     9: '3 weeks',
                     10: '5 years',
                     11: '400 years',
                     12: '34k years',
                     13: '2m years',
                     14: '200m years',
                     15: '15bn years',
                     16: '1tn years',
                     17: '93tn years',
                     18: '7qd years'}

numbers_dict = {8: 'no time',
                9: 'no time',
                10: 'no time',
                11: '2 secs',
                12: '25 secs',
                13: '4 mins',
                14: '41 mins',
                15: '6 hours',
                16: '2 days',
                17: '4 weeks',
                18: '9 months'}

letters_dict = {8: '22 mins',
                9: '19 hours',
                10: '1 month',
                11: '5 years',
                12: '300 years',
                13: '16k years',
                14: '800k years',
                15: '43m years',
                16: '2bn years',
                17: '100bn years',
                18: '6tn years'}

special_dict = {8: '8 hours',
                9: '3 weeks',
                10: '5 years',
                11: '400 years',
                12: '34k years',
                13: '2m years',
                14: '200m years',
                15: '15bn years',
                16: '1tn years',
                17: '93tn years',
                   18: '7qd years'}


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


def create_result(password):
    window.clipboard_clear()
    window.clipboard_append(password)


def check_passwd_power(self, password):
    pwr_result = self[pass_len.get()]
    power = 'Hacker need ' + pwr_result + ' to crack this password by brute force'
    msgbox = 'Your password is:\n ' + str(password) + '\n\n' + str(
        power) + '\n\n' + 'The password has been copied to clipboard!'
    messagebox.showinfo('Generated password', msgbox)


def generate_full():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(full_alphabet))
    create_result(password)
    check_passwd_power(all_characters_dict, password)


def generate_letters_num():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(letters_num))
    create_result(password)
    check_passwd_power(letters_num_dict, password)


def generate_num_spec():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(num_spec))
    create_result(password)
    check_passwd_power(num_spec_dict, password)


def generate_letters_spec():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(letters_spec))
    create_result(password)
    check_passwd_power(letters_spec_dict, password)


def generate_numbers_only():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(digits))
    create_result(password)
    check_passwd_power(numbers_dict, password)


def generate_letters_only():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(letters))
    create_result(password)
    check_passwd_power(letters_dict, password)


def generate_spec_only():
    password = ''
    for _ in range(pass_len.get()):
        password += ''.join(secrets.choice(special_chars))
    create_result(password)
    check_passwd_power(special_dict, password)


letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

full_alphabet = letters + digits + special_chars
letters_num = letters + digits
num_spec = digits + special_chars
letters_spec = letters + special_chars

window = Tk()
window.title("PASSGEN")
window.geometry("300x200")
window.resizable(False, False)

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

label2 = Label(window)
label2.pack()

label3 = Label(window)
label3.pack()

window.mainloop()