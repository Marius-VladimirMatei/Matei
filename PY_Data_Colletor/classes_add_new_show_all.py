# Personal Data Collect System in Python

import re  # regular expressions module needed to validate the input fields

# Parent Class definition
class Person:
    # init function is executed always when the class is being initiated
    #and assigns values to object properties
    # self parameter - reference to the current instance of the class - accesses the methods that belong to the class
    def __init__(self, full_name, address, email, telephone_number, date_of_birth):
        self.full_name = full_name
        self.address = address
        self.email = email
        self.telephone_number = telephone_number
        self.date_of_birth = date_of_birth


    # str func controls what should be returned
    def __str__(self):
        # f" - formatted string literals - allows expressions to be embedded and sets the output format
        return (f"Name: {self.full_name} \n"
                f"Address: {self.address} \n"
                f"Email: {self.email} \n"
                f"Telephone number: {self.telephone_number} \n"
                f"Date of Birth: {self.date_of_birth}")

# Child Classes definition
class Visitor(Person):
    # def init defines the Child its own set of parameters
    def __init__(self, full_name, address, email, telephone_number, date_of_birth):
        # super(). function inherits all the parameters from the parent class
        super().__init__(full_name, address, email, telephone_number, date_of_birth)
        # defining the child class instance as type Visitor
        self.type = "Visitor"

    def __str__(self):
        return (f"{super().__str__()} \n"
                f"Type: {self.type} \n")

class Employee(Person):
    def __init__(self, full_name, address, email, telephone_number, date_of_birth, employee_id):
        super().__init__(full_name, address, email, telephone_number, date_of_birth)
        self.employee_id = employee_id
        self.type = "Employee"


    def __str__(self):
        return (f"{super().__str__()} \n"
                f"Employee ID: {self.employee_id} \n"
                f"Type: {self.type} \n")

# ------------------------------- Data collection functions --------------------------------

# Function to collect and validate the full name
def get_full_name():
    while True:
        # Prompt the user to enter their full name
        full_name = input("Please enter the name: ").strip()

        # Check if the name is empty
        if not full_name:
            print("Error: The name cannot be empty. Please enter the name.")
            continue

        # Regular expression to match valid characters (letters, spaces, apostrophes, hyphens)
        # raw string used to treat characters just like normal ones and not like special \n \t
        # \s whitespace | + more of the same character  |  $ the end of the string
        if not re.match(r"^[A-Za-zäöüÄÖÜß\s'-]+$", full_name):
            print("Error: The name can only contain letters, spaces, apostrophes, or hyphens. Please enter a valid name.")
        else:
            # If valid input, return the full name
            print(f"Thank you! The name '{full_name}' has been successfully captured.")
            return full_name


# Function to collect and validate the address
def get_address():
    while True:
        # Prompt the user to enter address
        address = input("Please enter the address: ").strip()

        # Check if the name is empty
        if not address:
            print("Error: The address cannot be empty. Please enter a valid address.")
            continue

        # Regular expression to match valid characters (letters, spaces, apostrophes, hyphens)
        # raw string used to treat characters just like normal ones and not like special \n \t
        # \s whitespace | + more of the same character  |  $ the end of the string
        if not re.match(r"^[A-Za-z0-9äöüÄÖÜß,\s'-]+$", address):
            print("Error: The address can only contain letters, spaces, apostrophes, or hyphens. Please enter a valid address.")
        else:
            # If valid input, return the address
            print(f"Thank you! The address '{address}' has been successfully captured.")
            return address


# Function to collect and validate the address
def get_email():
    while True:
        # Prompt the user to enter email
        email = input("Please enter the email: ").strip()

        # Check if the name is empty
        if not email:
            print("Error: The email cannot be empty. Please enter a valid email.")
            continue

        # Regular expression to match valid characters (letters, spaces, apostrophes, hyphens)
        # raw string used to treat characters just like normal ones and not like special \n \t
        # \s whitespace | + more of the same character | ^ the start of the string |  $ the end of the string
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            print("Invalid email. Please enter a valid email.")
        else:
            # If valid input, return the email
            print(f"Thank you! The email '{email}' has been successfully captured.")
            return email

# Function to collect and validate the telephone number
def get_telephone_number():
    while True:
        # Prompt the user to enter their full name
        telephone_number = input("Please enter the telephone number: ").strip()

        # Check if the name is empty
        if not telephone_number:
            print("Error: The telephone number cannot be empty. Please enter a valid telephone number name.")
            continue

        if not re.match(r"^[0-9\s'-]+$", telephone_number):
            print("Error: The telephone number cannot be empty. Please enter a valid telephone number name.")
        else:
            # If valid input, return the telephone number
            print(f"Thank you! The telephone number '{telephone_number}' has been successfully captured.")
            return telephone_number


# Function to collect and validate the date of birth
def get_date_of_birth():
    while True:
        # Prompt the user to enter their date of birth
        date_of_birth = input("Please enter the date of birth (DD/MM/YYYY): ").strip()

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
            print(f"Thank you! The date of birth '{date_of_birth}' has been successfully captured.")
            return date_of_birth


# Function to collect and validate the employee ID
def get_employee_id():
    while True:
        employee_id = input("Please enter the Employee ID: ").strip()
        if not employee_id:
            print("Error: The Employee ID cannot be empty.")
            continue

        # Allows only digits
        if not re.match(r"^\d+$", employee_id):
            print("Error: Employee ID must be numeric.")
        else:
            # If valid input, return the employee ID
            print(f"Thank you! The Employee ID '{employee_id}' has been successfully captured.")
            return employee_id


#------------------------ Add new Visitor / Employee functions--------------------

# Function to add a new visitor
def add_new_visitor():
    print("Start adding a new Visitor")
    full_name = get_full_name()
    address = get_address()
    email = get_email()
    telephone_number = get_telephone_number()
    date_of_birth = get_date_of_birth()

    new_visitor = Visitor(full_name, address, email, telephone_number, date_of_birth)
    visitors.append(new_visitor)
    print("New Visitor successfully added!")

# Function to add new employee
def add_new_employee():
    print("Start adding a new Employee")
    full_name = get_full_name()
    address = get_address()
    email = get_email()
    telephone_number = get_telephone_number()
    date_of_birth = get_date_of_birth()
    employee_id = get_employee_id()

    new_employee = Employee(full_name, address, email, telephone_number, date_of_birth, employee_id)
    employees.append(new_employee)
    print("New Employee successfully added!")


#----------------------------- Show All Functions ------------------------------

# Function to display all Visitors
def show_all_visitors():
    if not visitors:
        print("No Visitors have been added yet.")
    else:
        print("------------- All Visitors ---------------")
        for visitor in visitors:
            print(visitor)
        #print() #prints a new blank line after every object


# Function to display all Employees
def show_all_employees():
    if not employees:
        print("No employees have been added yet.")
    else:
        print("------------- All Employees ---------------")
        for employee in employees:
            print(employee)
        #print()



# Def Main function
def main():
    # define global variables: also in py the variables are accessed across
    # multiple functions and they allow the data to be stored
    global visitors, employees

    #Lists to hold visitors/employees objects
    visitors = []
    employees = []


    while True:
        # Display the Menu
        print("-------------------------------------------------------") # separation for easy reading
        print("Welcome to the Personal Data Collection Program!")
        print("1. Add new Visitor")
        print("2. Add new Employee")
        print("3. Show all Visitors")
        print("4. Show all Employees")
        print("5. Exit")

        choice = input("Please select an option (1-5): ").strip()

        if choice == '1':
            add_new_visitor()
        elif choice == '2':
            add_new_employee()
        elif choice == '3':
            show_all_visitors()
        elif choice == '4':
            show_all_employees()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("-------------------------------------------------------")
            print("Invalid choice. Please select an option (1-5):")



"""
It ensures that the main() function is called when the script is executed directly
preventing it from  running when the script is imported as a module

if __name__ == "__main__":
    main()
"""
# calling the main() function to the program code
main()