import random
import string

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ''
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation
    
    if not characters:
        print("Please select at least one character set.")
        return None
    
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        digits = input("Include digits? (yes/no): ").lower() == 'yes'
        special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
        
        password = generate_password(length, uppercase, lowercase, digits, special_chars)
        
        if password:
            print(f"Generated Password: {password}")
        
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
