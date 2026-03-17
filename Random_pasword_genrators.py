import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

while True:
    length = int(input("Enter password length: "))
    
    password = generate_password(length)
    print("Generated Password:", password)

    choice = input("Generate again? (y/n): ")
    if choice.lower() != 'y':
        break