#main

import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
NUMBER = string.ascii_digits
Symbol = string.puncuation

all = lower + upper + NUMBER + Symbol
length = 9

password = ''.join(random.sample(all,length))

print(password)

# варик в 3 строки:

import secrets

length = 9
password = secrets.token_urlsafe(length)

print(password)

# варик в 1 строку:

import random

print("".join([chr(random.randint(ord("0"),ord("z"))) for i in range(9)]))