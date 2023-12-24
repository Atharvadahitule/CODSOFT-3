
("PASSWORD GENERATOR APP BY ATHARVA DAHITULE")

from tkinter import *
import string
import random

def generate(min_length, numbers = True, special_charachters=True):
    letters =string.ascii_letters
    digits=string.digits
    special= string.punctuation

    charachters = letters
    if numbers:
        charachters +=digits
    if special_charachters:
        charachters+=special

    password = ""
    meet_criteria = False
    has_number= False
    has_special = False

    while not meet_criteria or len(password) < min_length:
        new_charachter = random.choice(charachters)
        password+= new_charachter

        if new_charachter in digits:
            has_number= True
        elif new_charachter in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_charachters:
            meet_criteria = meet_criteria and has_special
    return password

min_length = int(input("Enter Minimum Length:"))

password = generate(min_length)
print("The generated password is :", password)
