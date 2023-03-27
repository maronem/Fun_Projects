# Fun Projects
My repo for fun projects and challenges.


### Random password Generator

To create a password generator I wanted 3 components: 

1. A string of letters that form a word
2. A 4-digit number 
3. A special character

To get a word as a string I accessed a remote dictionary of 10,000 word from [MIT](https://www.mit.edu/~ecprice/wordlist.10000). I first converted the output into an array using `.split_lines()` on the content from the get() request and saved this array to the variable WORDS. Then I created a loop to loop through the array and used `random.choice()` to pull a random word from the list, but as each word comes back as a byte datatype (ie. b'word') I used `.decode(UTF8)` to convert it to a string.  

```    
for word in WORDS:
        if len(str(random.choice(WORDS).decode('UTF8'))) >= 7: #decode word as byte and convert to str
            rand_word = str(random.choice(WORDS).decode('UTF8')) 
```

I also needed a random 4-digit number and a special character. For the special characters, I created a self-made list of characters from the 1-8 keys on a keyboard. For the random number, I once again used the `random` module and used the `randrange()` function to generate a number between 1000-9999.

```
    symbol_list = ["!", "@", "#", "$", "%", "^", "*"]
    rand_symbol = str(random.choice(symbol_list)) # choose random symbol from list
    rand_num = str(random.randrange(1000,9999)) # generate random 4 digit number
```

To put it all together I concatonated all my outputs to form a single password and functionlized the process:

```
def gen_pw(name: str): #user input their name
    for word in WORDS:
        if len(str(random.choice(WORDS).decode('UTF8'))) >= 7: #decode word as byte and convert to str
            rand_word = str(random.choice(WORDS).decode('UTF8')) 
    
    symbol_list = ["!", "@", "#", "$", "%", "^", "*"]
    rand_symbol = str(random.choice(symbol_list)) # choose random symbol from list
    rand_num = str(random.randrange(1000,9999)) # generate random 4 digit number
    rand_pw = rand_word + rand_num + rand_symbol
    return rand_pw
```
An example output can be seen here:

<img width="148" alt="Screen Shot 2023-03-27 at 12 32 45 PM" src="https://user-images.githubusercontent.com/108199140/228005691-2757db42-6213-4d09-a807-e9716a0dfeb1.png">

Lastly, to make the process interactive, I created a function that asks the user their name and takes their name as an argument to greet them and tell them their password:

```
# Functionalize whole process
def user_password():
    user = input("Hello, please type your name to have a password generated for you: ")
    print(f"Hello {user} your password is {gen_pw(user)}")

# FULL USE FUNCTION - Asks user for their name and generates them a password
user_password()
```

For example:

<img width="529" alt="Screen Shot 2023-03-27 at 12 35 16 PM" src="https://user-images.githubusercontent.com/108199140/228006608-504bcff7-fe95-40f5-977c-34407ebf00e1.png">

And there you have your very own password! :) 



