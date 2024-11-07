import re  # regular expressions module needed to validate the input fields

# ------------------------------- Data collection functions --------------------------------


# Function to collect and validate the full name
def get_full_name():
    while True:
        full_name = input("Please enter the name: ").strip()

        if not full_name:
            print("Error: The name cannot be empty. Please enter the name.")
            continue

        if not re.match(r"^[A-Za-zäöüÄÖÜß\s'-]+$", full_name):
            print("Error: The name can only contain letters, spaces, apostrophes, or hyphens. Please enter a valid name.")
        else:
            print(f"Thank you! The name '{full_name}' has been successfully captured.")
            return full_name


# Function to collect and validate the address
def get_address():
    while True:
        address = input("Please enter the address: ").strip()

        if not address:
            print("Error: The address cannot be empty. Please enter a valid address.")
            continue

        if not re.match(r"^[A-Za-z0-9äöüÄÖÜß,\s'-]+$", address):
            print("Error: The address can only contain letters, spaces, apostrophes, or hyphens. Please enter a valid address.")
        else:
            print(f"Thank you! The address '{address}' has been successfully captured.")
            return address


# Function to collect and validate the email
def get_email():
    while True:
        email = input("Please enter the email: ").strip()

        if not email:
            print("Error: The email cannot be empty. Please enter a valid email.")
            continue

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            print("Invalid email. Please enter a valid email.")
        else:
            print(f"Thank you! The email '{email}' has been successfully captured.")
            return email


# Function to collect and validate the telephone number
def get_telephone_number():
    while True:
        telephone_number = input("Please enter the telephone number: ").strip()

        if not telephone_number:
            print("Error: The telephone number cannot be empty. Please enter a valid telephone number.")
            continue

        if not re.match(r"^[0-9\s'-]+$", telephone_number):
            print("Error: The telephone number cannot be empty. Please enter a valid telephone number.")
        else:
            print(f"Thank you! The telephone number '{telephone_number}' has been successfully captured.")
            return telephone_number


# Function to collect and validate the date of birth
def get_date_of_birth():
    while True:
        date_of_birth = input("Please enter the date of birth (DD/MM/YYYY): ").strip()

        if not date_of_birth:
            print("Error: The date of birth cannot be empty. Please enter a valid date of birth.")
            continue

        if not re.match(r"^\d{2}/\d{2}/\d{4}$", date_of_birth):
            print("Error: The date of birth must be in the format DD/MM/YYYY. Please enter a valid date.")
        else:
            print(f"Thank you! The date of birth '{date_of_birth}' has been successfully captured.")
            return date_of_birth


# Function to collect and validate the employee ID
def get_employee_id():
    while True:
        employee_id = input("Please enter the Employee ID: ").strip()

        if not employee_id:
            print("Error: The Employee ID cannot be empty.")
            continue

        if not re.match(r"^\d+$", employee_id):
            print("Error: Employee ID must be numeric.")
        else:
            print(f"Thank you! The Employee ID '{employee_id}' has been successfully captured.")
            return employee_id


# ------------------------ Add new Visitor / Employee functions --------------------

# Function to add a new visitor
def add_new_visitor(visitors):
    print("Start adding a new Visitor")
    full_name = get_full_name()
    address = get_address()
    email = get_email()
    telephone_number = get_telephone_number()
    date_of_birth = get_date_of_birth()

    # Create a dictionary for the new visitor
    new_visitor = {
        'full_name': full_name,
        'address': address,
        'email': email,
        'telephone_number': telephone_number,
        'date_of_birth': date_of_birth,
        'type': 'Visitor'
    }
    visitors.append(new_visitor)
    print("New Visitor successfully added!")


# Function to add a new employee
def add_new_employee(employees):
    print("Start adding a new Employee")
    full_name = get_full_name()
    address = get_address()
    email = get_email()
    telephone_number = get_telephone_number()
    date_of_birth = get_date_of_birth()
    employee_id = get_employee_id()

    # Create a dictionary for the new employee
    new_employee = {
        'full_name': full_name,
        'address': address,
        'email': email,
        'telephone_number': telephone_number,
        'date_of_birth': date_of_birth,
        'employee_id': employee_id,
        'type': 'Employee'
    }
    employees.append(new_employee)
    print("New Employee successfully added!")


# ----------------------------- Show All Functions ------------------------------

# Function to display all Visitors
def show_all_visitors(visitors):
    if not visitors:
        print("No Visitors have been added yet.")
    else:
        print("------------- All Visitors ---------------")
        for visitor in visitors:
            print(f"Name: {visitor['full_name']} \n"
                  f"Address: {visitor['address']} \n"
                  f"Email: {visitor['email']} \n"
                  f"Telephone number: {visitor['telephone_number']} \n"
                  f"Date of Birth: {visitor['date_of_birth']} \n"
                  f"Type: {visitor['type']} \n")


# Function to display all Employees
def show_all_employees(employees):
    if not employees:
        print("No employees have been added yet.")
    else:
        print("------------- All Employees ---------------")
        for employee in employees:
            print(f"Name: {employee['full_name']} \n"
                  f"Address: {employee['address']} \n"
                  f"Email: {employee['email']} \n"
                  f"Telephone number: {employee['telephone_number']} \n"
                  f"Date of Birth: {employee['date_of_birth']} \n"
                  f"Employee ID: {employee['employee_id']} \n"
                  f"Type: {employee['type']} \n")


# ------------------------------- Main Program ------------------------------

def main():
    # List to store visitor data
    visitors = []
    # List to store employee data
    employees = []

    while True:
        # Display the Menu
        print("-------------------------------------------------------")
        print("Welcome to the Personal Data Collection Program!")
        print("1. Add new Visitor")
        print("2. Add new Employee")
        print("3. Show all Visitors")
        print("4. Show all Employees")
        print("5. Exit")

        choice = input("Please select an option (1-5): ").strip()

        if choice == '1':
            add_new_visitor(visitors)
        elif choice == '2':
            add_new_employee(employees)
        elif choice == '3':
            show_all_visitors(visitors)
        elif choice == '4':
            show_all_employees(employees)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("-------------------------------------------------------")
            print("Invalid choice. Please select an option (1-5):")


main()
