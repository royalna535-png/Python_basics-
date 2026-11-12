import random
import string

# How long you want password
length = 8

# All characters allowed
characters = string.ascii_letters + string.digits + "!@#$%"

# Generate password
password = "".join(random.choice(characters) for i in range(length))

print("Your strong password is:", password)