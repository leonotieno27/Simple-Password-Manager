import base64
import os
import sys

filename = 'passwords.txt'

def main():
    """Encode and decode user input for a simple password manager."""
    while True:
        os.system('clear')
        print("\t\t\t*** Simple Password Manager ***")
        print("Choose an option (1/2/3):")
        print("1. Encode Password")
        print("2. Show Passwords")
        print("3. Exit")

        choice = input("\nEnter your choice: ")
        if choice == '1':
            os.system('clear')
            password_name = input("Enter the password site/program: ")
            password = input("Enter the password to encode: ")

            # Encode the password using Base64
            encoded_password = base64.b64encode(password.encode()).decode()

            # Write to file
            with open(filename, 'a') as file:
                file.write(f"{password_name}:{encoded_password}\n")
            
            print("\nPassword saved successfully!")
            input("\nPress Enter to continue...")

        elif choice == '2':
            os.system('clear')

            # Check if the file exists and is not empty
            if not os.path.exists(filename) or os.path.getsize(filename) == 0:
                print("No passwords found!")
            else:
                print("\t\t\t*** Saved Passwords ***\n")
                with open(filename, 'r') as file:
                    for line in file:
                        # Parse and decode each saved password
                        password_name, encoded_password = line.strip().split(':')
                        decoded_password = base64.b64decode(encoded_password).decode()
                        print(f"{password_name}: {decoded_password}")
            
            input("\nPress Enter to continue...")

        elif choice == '3':
            print("Exiting Password Manager. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice! Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
