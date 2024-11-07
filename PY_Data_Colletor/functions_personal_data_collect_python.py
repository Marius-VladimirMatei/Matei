# Personal Data Collect System in Python


"""
class Person:
    def __init__(self,full_name, address):
        self.full_name = full_name
        self.address = address
"""


# regular expressions module needed to validate the input fields
import re

# ------------------------- Data collection functions --------------------------------
# Function to collect and validate the full name
def get_full_name():
    while True:
        # Prompt the user to enter their full name
        full_name = input("Please enter your name: ").strip()

        # Check if the name is empty
        if not full_name:
            print("Error: The name cannot be empty. Please enter your name.")
            continue

        # Regular expression to match valid characters (letters, spaces, apostrophes, hyphens)
        # raw string used to treat characters just like normal ones and not like special \n \t
        if not re.match(r"^[A-Za-zß\s'-]+$", full_name):
            print("Error: The name can only contain letters, spaces, apostrophes, or hyphens. Please enter a valid name.")
        else:
            # If valid input, return the full name
            return full_name



# Function to collect and validate the address
def get_address():
    while True:
        # Prompt the user to enter address
        address = input("Please enter your address: ").strip()

        # Check if the name is empty
        if not address:
            print("Error: The address cannot be empty. Please enter a valid address.")
            continue

        # Regular expression to match valid characters (letters, spaces, apostrophes, hyphens)
        # raw string used to treat characters just like normal ones and not like special \n \t
        # \s whitespace | + more of the same character  |  $ the end of the string
        if not re.match(r"^[A-Za-z0-9ß,\s'-]+$", address):
            print("Error: The address can only contain letters, spaces, apostrophes, or hyphens. Please enter a valid address.")
        else:
            # If valid input, return the full name
            return address


# Function to collect and validate the address
def get_email():
    while True:
        # Prompt the user to enter address
        email = input("Please enter your email: ").strip()

        # Check if the name is empty
        if not email:
            print("Error: The email cannot be empty. Please enter your email.")
            continue

        # Regular expression to match valid characters (letters, spaces, apostrophes, hyphens)
        # raw string used to treat characters just like normal ones and not like special \n \t
        # \s whitespace | + more of the same character  |  $ the end of the string
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            print("Invalid email. Please enter a valid email.")
        else:
            return email



def get_telephone_number():
    while True:
        # Prompt the user to enter their full name
        telephone_number = input("Please enter your telephone number: ").strip()

        # Check if the name is empty
        if not telephone_number:
            print("Error: The telephone number cannot be empty. Please enter a valid telephone number name.")
            continue

        # Regular expression to match valid characters (letters, spaces, apostrophes, hyphens)
        # raw string used to treat characters just like normal ones and not like special \n \t
        if not re.match(r"^[0-9\s'-]+$", telephone_number):
            print("Error: The telephone number cannot be empty. Please enter a valid telephone number name.")
        else:
            # If valid input, return the full name
            return telephone_number



def get_date_of_birth():
    while True:
        # Prompt the user to enter their date of birth
        date_of_birth = input("Please enter your date of birth (DD/MM/YYYY): ").strip()

        # Check if the input is empty
        if not date_of_birth:
            print("Error: The date of birth cannot be empty. Please enter a valid date of birth.")
            continue

        # Regular expression to match a valid date format (DD/MM/YYYY)
        # Allows: two digits for day, two digits for month, four digits for year
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", date_of_birth):
            print("Error: The date of birth must be in the format DD/MM/YYYY. Please enter a valid date.")
        else:
            # If valid input, return the date of birth
            return date_of_birth


# ------------------------- Feed back  functions --------------------------------

# Function to provide feedback to the user after successful data capture
def provide_feedback_name(full_name):
    print(f"Thank you! Your full name '{full_name}' has been successfully captured.")

# Function to provide feedback to the user after successful data capture
def provide_feedback_address(address):
    print(f"Thank you! Your address '{address}' has been successfully captured.")

# Function to provide feedback to the user after successful data capture
def provide_feedback_email(email):
    print(f"Thank you! Your email '{email}' has been successfully captured.")

# Function to provide feedback to the user after successful data capture
def provide_feedback_telephone_number(telephone_number):
    print(f"Thank you! Your telephone number '{telephone_number}' has been successfully captured.")

# Function to provide feedback to the user after successful data capture
def provide_feedback_date_of_birth(date_of_birth):
    print(f"Thank you! Your date of birth '{date_of_birth}' has been successfully captured.")



# -------------------------  Main function --------------------------------


# Main function to run the program
def main():

    #The main function runs the collection of the data, makes the input checks and provides feedback.

    print("Welcome to the Personal Data Collection Program!")


    # Step 1: Collect the user's full name
    full_name = get_full_name()
    address = get_address()
    email = get_email()
    telephone_number = get_telephone_number()
    date_of_birth = get_date_of_birth()


    # Step 2: Provide feedback that the data was successfully captured
    provide_feedback_name(full_name)
    provide_feedback_address(address)
    provide_feedback_email(email)
    provide_feedback_telephone_number(telephone_number)
    provide_feedback_date_of_birth(date_of_birth)


main()