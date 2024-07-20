'''TASK 3
PASSWORD GENERATOR   '''


import random
import string

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Define the character sets for the password
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

# Combine all the character sets
all_characters = lowercase + uppercase + digits + special_characters

# Generate a random password of the specified length
password = ''.join(random.choice(all_characters) for _ in range(length))

# Display the generated password
print(f"Generated password: {password}")
