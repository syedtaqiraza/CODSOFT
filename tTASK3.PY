import random
import string

def generate_password(length):
    # Here we define the characters we'll use to create your password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Now, we'll randomly pick characters from this pool to generate your password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Let's start by asking how long you'd like your password to be
    length = int(input("How long would you like your password to be? "))
    
    # Great! Now we'll generate your password for you
    password = generate_password(length)
    
    # Here's your randomly generated password, ready for use:
    print("Your password is:", password)

# Time to run the main function and get your password!
main()