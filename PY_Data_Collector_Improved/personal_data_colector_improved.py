import re  # regular expressions module needed to validate the input fields

#PY_Data_Collector_Improved: clear data and string type output
# New subtracted menu


# ------------------------------- Data Clean function --------------------------------
def clean_data(data):
    data = data.strip()
    data = re.sub(r'\s+', ' ', data)  # Replace multiple spaces with a single space
    return ' '.join(word.capitalize() for word in data.split())  # Capitalize each word


# ------------------------------- Data collection functions --------------------------------


# Function to collect and validate the full name
def get_full_name():
    while True:
        # Prompt the user to enter their full name
        # .strip() method - clears white space before and after input
        full_name = input("Please enter the name: ").strip()

        # Check if the name is empty
        if not full_name:
            print("Error: The name cannot be empty. Please enter the name.")
            continue

        # Clean and validate the name field
        full_name = clean_data(full_name)

        # Regular expression to match valid characters (letters, spaces, apostrophes, hyphens)
        # raw string used to treat characters just like normal ones and not like special \n \t
        # \s whitespace | + more of the same character  |  $ the end of the string
        if not re.match(r"^[A-Za-zäöüÄÖÜß\s'-]+$", full_name):
            print("Error: The name can only contain letters, spaces, apostrophes, or hyphens. Please enter a valid name.")
        else:
            # If valid input, return the full name and provide feed-back
            print(f"Thank you! The name '{full_name}' has been successfully captured.")
            return full_name


# Function to collect and validate the address
def get_address():
    while True:
        address = input("Please enter the address: ").strip()

        if not address:
            print("Error: The address cannot be empty. Please enter a valid address.")
            continue

        # Clean and validate the name field
        address = clean_data(address)

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

        # Clean and validate the name field, making all lower
        email = email.lower()

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

        # Clean and validate the name field
        telephone_number = clean_data(telephone_number)

        # Clean and validate telephone number, remove extra spaces
        telephone_number = re.sub(r"\s+", "", telephone_number)

        if not re.match(r"^[0-9\s'-`]+$", telephone_number):
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

        # Regular expression to match a valid date format (DD/MM/YYYY)
        # Allows: two digits for day, two digits for month, four digits for year
        # ^\d{2}/\d{2}/\d{4}$ old pattern
        if not re.match(r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$", date_of_birth):
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

    # Output data into a single string
    visitor_data = f"Name: {full_name}, Date of Birth: {date_of_birth}, Address: {address}, Email: {email}, Telephone: {telephone_number}, Type: Visitor"
    visitors.append(visitor_data)
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

    # Output data into a single string
    employee_data = f"Name: {full_name}, Date of Birth: {date_of_birth}, Address: {address}, Email: {email}, Telephone: {telephone_number}, Employee ID: {employee_id}, Type: Employee"
    employees.append(employee_data)
    print("New Employee successfully added!")


# ----------------------------- Show All Functions ------------------------------

# Function to display all Visitors
def show_all_visitors(visitors):
    if not visitors:
        print("No Visitors have been added yet.")
    else:
        print("------------- All Visitors ---------------")
        for visitor in visitors:
            print(visitor)
            print("-------------------------------------------------------")



# Function to display all Employees
def show_all_employees(employees):
    if not employees:
        print("No employees have been added yet.")
    else:
        print("------------- All Employees ---------------")
        for employee in employees:
            print(employee)
            print("-------------------------------------------------------")


# ------------------------------- Main Program ------------------------------

def main():
    # List to store visitor data
    visitors = []
    # List to store employee data
    employees = []

    while True:
        # Display the simplified Menu
        print("-------------------------------------------------------")
        print("Welcome to the Personal Data Collection Program!")
        print("1. Add new")
        print("2. Show all")
        print("3. Exit")

        choice = input("Please select an option (1-3): ").strip()

        if choice == '1':
            print("1. Add new Visitor")
            print("2. Add new Employee")

            sub_choice = input("Please select Visitor or Employee to add (1-2): ").strip()

            if sub_choice == '1':
                add_new_visitor(visitors)
            elif sub_choice == '2':
                add_new_employee(employees)
            else:
                print("Invalid choice. Please choose either 1 or 2.")


        elif choice == '2':
            print("1. Show all Visitors")
            print("2. Show all Employees")

            sub_choice = input("Please select Visitors or Employees to display (1-2): ").strip()

            if sub_choice == '1':
                show_all_visitors(visitors)

            elif sub_choice == '2':
                show_all_employees(employees)
            else:
                print("Invalid choice. Please choose either 1 or 2.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("-------------------------------------------------------")
            print("Invalid choice. Please select an option (1-3):")

# Run the main function
main()