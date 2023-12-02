from tkinter import *
from random import *
from tkinter import messagebox
from tkinter import filedialog

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()`~-_=+[{]}|;:,<.>/?"
amount = 8

def open_settings():
    def check_mode():
        if mode.get() == 1:
            window.config(bg="#d9d9d9")
            try:
                window2.config(bg="#d9d9d9")
            except NameError:
                pass
            window3.config(bg="#d9d9d9")
            space_label.config(bg="#d9d9d9")
            space_label2.config(bg="#d9d9d9")
            space_label3.config(bg="#d9d9d9")
            space_label4.config(bg="#d9d9d9")
            try:
                space_label5.config(bg="#d9d9d9")
                space_label6.config(bg="#d9d9d9")
            except NameError:
                pass
            space_label7.config(bg="#d9d9d9")

            settings_title.config(fg="blue")
            mode_label.config(fg="blue")
            dark_mode.config(fg="blue")
            light_mode.config(fg="blue")
            try:
                second_window_title.config(fg="blue")
                about_button_window2.config(fg="blue")
                open_file_button.config(fg="blue")
                file_read_label.config(fg="blue")
                copy_password_window2.config(fg="blue")
                paste_label.config(fg="blue")
                password_text.config(fg="blue")
                password_text_button.config(fg="blue")
                submit_password_text.config(fg="blue")
            except NameError:
                pass
            title.config(fg="blue")
            amount_label.config(fg="blue")
            amount_entry.config(fg="blue")
            amount_button.config(fg="blue")
            show_symbols.config(fg="blue")
            hide_symbols.config(fg="blue")
            start.config(fg="blue")
            password.config(fg="blue")
            copy.config(fg="blue")
            next_tab_button.config(fg="blue")
            settings_button.config(fg="blue")
        elif mode.get() == 2:
            window.config(bg="black")
            try:
                window2.config(bg="black")
            except NameError:
                pass
            window3.config(bg="black")
            space_label.config(bg="black")
            space_label2.config(bg="black")
            space_label3.config(bg="black")
            space_label4.config(bg="black")
            try:
                space_label5.config(bg="black")
                space_label6.config(bg="black")
            except NameError:
                pass
            space_label7.config(bg="black")

            settings_title.config(fg="black")
            mode_label.config(fg="black")
            dark_mode.config(fg="black")
            light_mode.config(fg="black")
            try:
                second_window_title.config(fg="black")
                about_button_window2.config(fg="black")
                open_file_button.config(fg="black")
                file_read_label.config(fg="black")
                copy_password_window2.config(fg="black")
                paste_label.config(fg="black")
                password_text.config(fg="black")
                password_text_button.config(fg="black")
                submit_password_text.config(fg="black")
            except NameError:
                pass
            title.config(fg="black")
            amount_label.config(fg="black")
            amount_entry.config(fg="black")
            amount_button.config(fg="black")
            show_symbols.config(fg="black")
            hide_symbols.config(fg="black")
            start.config(fg="black")
            password.config(fg="black")
            copy.config(fg="black")
            next_tab_button.config(fg="black")
            settings_button.config(fg="black")

    global window3
    global settings_title
    global mode_label
    global dark_mode
    global light_mode

    window3 = Toplevel()
    window3.geometry("300x130")
    window3.resizable(False, False)
    window.title("Password Generator Settings")

    settings_title = Label(window3, text="Welcome to Settings")
    settings_title.pack()

    space_label7 = Label(window3)
    space_label7.pack()

    mode_label = Label(window3, text="Select Color Customization")
    mode_label.pack()

    mode = IntVar()

    light_mode = Radiobutton(window3, text="Light Mode (Default Option)", variable=mode, value=1, command=check_mode)
    light_mode.pack()
    dark_mode = Radiobutton(window3, text="Dark Mode", variable=mode, value=2, command=check_mode)
    dark_mode.pack()

    settings_title.config(fg="blue", font=("Helvetica 15 underline"))
    mode_label.config(fg="blue")
    dark_mode.config(fg="blue")
    light_mode.config(fg="blue")

    window3.mainloop()

def submit_symbols():
    global symbols

    if symbols_or_not.get() == 1:
        symbols = "!@#$%^&*()`~-_=+[{]}|;:,<.>/?"
    elif symbols_or_not.get() == 2:
        symbols = "abcdefghijklmnopqrstuvwxyz"

def submit_amount(*args):
    global amount

    try:
        amount = int(amount_entry.get())
        if amount > 20:
            amount = 20
        elif amount < 0:
            amount = 1
            messagebox.showerror(title="Amount Error", message="Please do not use negative numbers for the amount.")
        
        amount_entry.delete(0, END)
        amount_label.config(text="How long would you like your password to be? (Max is 20, current amount is " + str(amount) + ")")
    except ValueError:
        amount_entry.delete(0, END)
        messagebox.showerror(title="Amount Error", message="Please use numbers only for the amount.")

def scramble():
    global character

    random_character = randint(1,4)

    if random_character == 1:
        character = lowers
    elif random_character == 2:
        character = uppers
    elif random_character == 3:
        character = numbers
    elif random_character == 4:
        character = symbols

def create_password():
    scramble()
    one = character[randint(0,len(character)-1)]
    scramble()
    two = character[randint(0,len(character)-1)]
    scramble()
    three = character[randint(0,len(character)-1)]
    scramble()
    four = character[randint(0,len(character)-1)]
    scramble()
    five = character[randint(0,len(character)-1)]
    scramble()
    six = character[randint(0,len(character)-1)]
    scramble()
    seven = character[randint(0,len(character)-1)]
    scramble()
    eight = character[randint(0,len(character)-1)]
    scramble()
    nine = character[randint(0,len(character)-1)]
    scramble()
    ten = character[randint(0,len(character)-1)]
    scramble()
    eleven = character[randint(0,len(character)-1)]
    scramble()
    twelve = character[randint(0,len(character)-1)]
    scramble()
    thirteen = character[randint(0,len(character)-1)]
    scramble()
    fourteen = character[randint(0,len(character)-1)]
    scramble()
    fifteen = character[randint(0,len(character)-1)]
    scramble()
    sixteen = character[randint(0,len(character)-1)]
    scramble()
    seventeen = character[randint(0,len(character)-1)]
    scramble()
    eighteen = character[randint(0,len(character)-1)]
    scramble()
    nineteen = character[randint(0,len(character)-1)]
    scramble()
    twenty = character[randint(0,len(character)-1)]
    scramble()

    random_string = one + two + three + four + five + six + seven + eight + nine + ten + eleven + twelve + thirteen + fourteen + fifteen + sixteen + seventeen + eighteen + nineteen + twenty

    password.config(text=random_string[0:amount])

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password.cget("text"))
    window.update()

def second_tab():
    global space_label5
    global space_label6

    global second_window_title
    global about_button_window2
    global open_file_button
    global file_read_label
    global copy_password_window2
    global paste_label
    global password_text
    global password_text_button
    global submit_password_text

    def encrypt(string):
        return "lkfg87%" + (string[::-1])+"6343cR1y&)$*"

    def decrypt(string):
        return (string[7:-12])[::-1]

    def ask_for_file():
        filepath = filedialog.askopenfilename(initialdir="/home/zbos/Password Generator", title="Find Password File", filetypes=(("Text Files","*.txt"), ("All Files", "*.*")))
        file = open(filepath, "r")
        file_read_label.config(text=decrypt(file.read()))
        file.close()
        messagebox.showwarning(title="File Password Success", message="Congradulations! File has been successfully decrypted!")

    def encrypt_and_save():
        global encrypted_filetext
        file = filedialog.asksaveasfile(initialdir="/home/zbos/Password Generator", defaultextension=".txt", filetypes=[("Text Files",".txt")])
        filetext = str(password_text.get())
        encrypted_filetext = encrypt(filetext)
        file.write(encrypted_filetext)
        file.close()
        messagebox.showwarning(title="File Password Success", message="Congradulations! File has been successfully encrypted and saved! Encrypted version is '" + encrypted_filetext + "'")

    def hide_pass():
        password_text.config(show="*")
    
    def info_window2():
        messagebox.showinfo(title="About File Passwords", message="The point of this part of the program is to save your password safely through a .txt file, in case you forget them.")

    def copy_second_password():
        window2.clipboard_clear()
        window2.clipboard_append(file_read_label.cget("text"))
        window2.update()

    global window2

    window2 = Toplevel()
    window2.title("Password Files")
    window2.geometry("800x400")
    window2.resizable(False, False)

    second_window_title = Label(window2, text="Save, Open, Encrypt, and Decrypt Your Password Files Here")
    second_window_title.pack()

    about_button_window2 = Button(window2, text="About Password File Encryptor and Decryptor", command=info_window2, image=about, compound="right")
    about_button_window2.pack()

    space_label5 = Label(window2)
    space_label5.pack()

    open_file_button = Button(window2, text="Open and Decrypt a File", command=ask_for_file, image=open_symbol, compound="right")
    open_file_button.pack()

    file_read_label = Label(window2, text="the content of the file will appear here...")
    file_read_label.pack()

    copy_password_window2 = Button(window2, text="Copy Password", command=copy_second_password, image=copy_symbol, compound="right")
    copy_password_window2.pack()

    space_label6 = Label(window2)
    space_label6.pack()

    paste_label = Label(window2, text="Paste in the password you would like to encrypt and save below.")
    paste_label.pack()

    password_text = Entry(window2)
    password_text.pack()

    password_text_button = Button(window2, text="Hide Password", command=hide_pass, image=hide, compound="right")
    password_text_button.pack()

    submit_password_text = Button(window2, text="Submit Your Password to Save and Encrpyt File", command=encrypt_and_save, image=submit, compound="right")
    submit_password_text.pack()

    second_window_title.config(fg="blue", font=("Helvetica 15 underline"))
    about_button_window2.config(fg="blue")
    open_file_button.config(fg="blue")
    file_read_label.config(fg="blue")
    copy_password_window2.config(fg="blue")
    paste_label.config(fg="blue")
    password_text.config(fg="blue")
    password_text_button.config(fg="blue")
    submit_password_text.config(fg="blue")

    window2.mainloop()

window = Tk()
window.geometry("700x500")
window.resizable(False, False)
window.title("Password Generator")

about = PhotoImage(file="about.png").subsample(6, 6)
arrow = PhotoImage(file="arrow.png").subsample(100, 100)
copy_symbol = PhotoImage(file="copy.png").subsample(15, 15)
hide = PhotoImage(file="hide.png").subsample(90, 90)
lock = PhotoImage(file="lock.png").subsample(15, 15)
new = PhotoImage(file="new.png").subsample(80, 80)
open_symbol = PhotoImage(file="open.png").subsample(12, 12)
submit = PhotoImage(file="submit.png").subsample(20, 20)
settings = PhotoImage(file="settings.png").subsample(15, 15)

title = Label(window, text="Generate Safe and Secure Passwords")
title.pack()

space_label = Label(window)
space_label.pack()

amount_label = Label(window, text="How long would you like your password to be? (Max is 20, current amount is " + str(amount) + ")")
amount_label.pack()

amount_entry = Entry(window)
amount_entry.pack()

amount_button = Button(window, text="Submit Amount", command=submit_amount, image=arrow, compound="right")
amount_button.pack()

space_label2 = Label(window)
space_label2.pack()

symbols_or_not = IntVar()

show_symbols = Radiobutton(window, text="Use Symbols (Default Option)", variable=symbols_or_not, value=1, command=submit_symbols)
show_symbols.pack()

hide_symbols = Radiobutton(window, text="No Symbols (Just Letters and Numbers)", variable=symbols_or_not, value=2, command=submit_symbols)
hide_symbols.pack()

space_label3 = Label(window)
space_label3.pack()

start = Button(window, text="Click to Start", command=create_password, image=lock, compound="right")
start.pack()

password = Label(window, text="password will appear here...")
password.pack()

copy = Button(window, text="Copy Password", command=copy_password, image=copy_symbol, compound="right")
copy.pack()

space_label4 = Label(window)
space_label4.pack()

next_tab_button = Button(window, text="Encrypt and Save Password", command=second_tab, image=new, compound="right")
next_tab_button.pack()

settings_button = Button(window, text="Settings", command=open_settings, image=settings, compound="right")
settings_button.pack()

title.config(fg="blue", font=("Helvetica 15 underline"))
amount_label.config(fg="blue")
amount_entry.config(fg="blue")
amount_button.config(fg="blue")
show_symbols.config(fg="blue")
hide_symbols.config(fg="blue")
start.config(fg="blue")
password.config(fg="blue")
copy.config(fg="blue")
next_tab_button.config(fg="blue")
settings_button.config(fg="blue")

window.bind("<Return>", submit_amount)

window.mainloop()