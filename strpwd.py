import string
from random import *
characters = string.ascii_letters+string.punctuation+string.digits
password = "".join(choice(characters) for x in range(randint(13, 23)))
print('This is your generated password')
print(password)
