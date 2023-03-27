import pandas as pd
import random
import requests

# Access remote dictionary

word_list = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_list)
WORDS = response.content.splitlines()

# Create function to generate a password containing a word > len(7), a 4 digit number, and a special character

def gen_pw(name: str): # input will ask user to input their name
    for word in WORDS:
        if len(str(random.choice(WORDS).decode('UTF8'))) >= 7: #decode word as byte and convert to str
            rand_word = str(random.choice(WORDS).decode('UTF8')) 
    
    symbol_list = ["!", "@", "#", "$", "%", "^", "*"]
    rand_symbol = str(random.choice(symbol_list)) # choose random symbol from list
    rand_num = str(random.randrange(1000,9999)) # generate random 4 digit number
    rand_pw = rand_word + rand_num + rand_symbol
    return rand_pw

# Generate password for you
gen_pw("Michael")

# Functionalize whole process
def user_password():
    user = input("Hello, please type your name to have a password generated for you: ")
    print(f"Hello {user} your password is {gen_pw(user)}")

# FULL USE FUNCTION - Asks user for their name and generates them a password
user_password()