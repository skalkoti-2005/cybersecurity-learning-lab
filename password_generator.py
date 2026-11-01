
import secrets
import string

length = int(input("Enter password length (minimum 12): "))

if length < 12:
    print("Please enter at least 12 characters.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))

    print("Generated sample password:", password)
