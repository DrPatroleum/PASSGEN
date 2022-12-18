import secrets
import string
from tkinter import *
from tkinter import messagebox

result = ""

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
    #generowanie hasła

"""def sel():
    selection = "Długość hasła wyniesie: " + str(pass_len.get())
    label.config(text=selection)"""

def generate_full():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(full_alphabet))
    label3.config(text=password)
    
def generate_leters_num():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(leters_num))
    label3.config(text=password)
    
def generate_num_spec():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(num_spec))
    label3.config(text=password)
    
def generate_letters_spec():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(letters_spec))
    label3.config(text=password)
    
def generate_numbers_only():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(digits))
    label3.config(text=password)
    
def generate_letters_only():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(letters))
    label3.config(text=password)
    
def generate_spec_only():
    password = ''
    for i in range(pass_len.get()):
        password += ''.join(secrets.choice(special_chars))
    label3.config(text=password)
       
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

full_alphabet = letters + digits + special_chars
leters_num = letters + digits
num_spec = digits + special_chars
letters_spec = letters + special_chars

window = Tk()
window.title("Generator Haseł 1.0")
window.geometry("300x300")
window.resizable(False, False)
icon = PhotoImage(file='/Users/defcon/Documents/passgen/set.png')
window.iconphoto(True, icon)

label1 = Label(window,
              text="Co ma zawierać hasło?")
label1.pack()

numerki = IntVar()
check_button_numbers = Checkbutton(window,
                           text="numerki",
                           variable=numerki)
check_button_numbers.pack()

literki = IntVar()
check_button_letters = Checkbutton(window,
                           text="literki",
                           variable= literki)
check_button_letters.pack()

spec_znaki = IntVar()
check_button_special = Checkbutton(window,
                           text="znaki spec",
                           variable=spec_znaki)
check_button_special.pack()

pass_len = IntVar()
scale = Scale(window, 
              from_ = 8, 
              to=24,
              length=250,
              orient=HORIZONTAL,
              font = ("Consolas", 20),
              tickinterval= 4,
              showvalue= 1,
              resolution=1,
              variable=pass_len)
scale.pack()

gen_button = Button(window,
                text = "GENERUJ HASŁO",
                command = click,
                font = ("Arial", 24),
                fg = "#00FF00",
                bg = "black",
                activeforeground = "#00FF00",
                activebackground = "black",
                state=ACTIVE,
                compound = "center")
gen_button.pack()

label2 = Label(window,
               text="Wygenerowane haslo to:")
label2.pack()

label3 = Label(window)
label3.pack()

"""copy_button = Button(window,
                     text="COPY PASSWORD",
                     command=copy_option,
                     fg="orange",
                     bg="black",
                     activeforeground="orange",
                     activebackground="black",
                     state=ACTIVE,
                     compound="center")
copy_button.pack()"""

"""menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open") #command="")
fileMenu.add_command(label="save") #command="")
fileMenu.add_separator()
fileMenu.add_command(label="exit") #command="")
editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="edit")

window.mainloop()

print("Generator Haseł 1.0")

"""while decision != 0:
    decision = input("Wybierz 'k' by kontynować lub 'w' by wyjść z programu ")
    if decision == "k":
        while True:
            try:
                pass_len = int(input("Jak długie ma być hasło? (wpisz liczbę znaków) "))
                if pass_len != 0:    
                    break
            except ValueError:
                continue
        letters = input("Czy mam uzyc liter w haśle? y/n ")
        numbers = input("Czy mam uzyc cyfr w haśle? y/n ")
        special_characters = input("Czy uzyc znakow specjalnych? y/n ")
        if letters == 'y' and digits == 'y' and special_characters == 'y':
            generate_full()
        if letters == 'y' and digits == 'y':
            generate_leters_num()
        if digits == 'y' and special_characters == 'y':
            generate_num_spec()
        if letters == 'y' and special_characters == 'y':
            generate_letters_spec()
    if decision == "w":
        break
    if decision != "k" and decision != "w":
        print("Błąd, spróbuj wybrać ponownie.")
        continue"""