import random

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890,<>.?:;{[}]-_+=!@#$%^&*()"
while True:
    password_len = int(input("How much charachters?"))
    password_count = int(input("how much count?"))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print(password)