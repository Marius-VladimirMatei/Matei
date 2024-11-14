import re  # regular expressions module needed to validate the input fields



# updated show all functions with indexing each entry
# update entry functions



# ------------------------------- Data Clean function --------------------------------
def clean_data(data):
    data = data.strip()
    data = re.sub(r'\s+', ' ', data)  # Replace multiple spaces with a single space
    return ' '.join(word.capitalize() for word in data.split())  # Capitalize each word


# ------------------------------- Data collection functions --------------------------------
def get_full_name():
    while True:
        full_name = input("Please enter the name: ").strip()
        if not full_name:
            print("Error: The name cannot be empty. Please enter the name.")
            continue
        full_name = clean_data(full_name)
        if not re.match(r"^[A-Za-zäöüÄÖÜß\s'-]+$", full_name):
            print("Error: The name can only contain letters, spaces, apostrophes, or hyphens. Please enter a valid name.")
        else:
            print(f"Thank you! The name '{full_name}' has been successfully captured.")
            return full_name


def get_address():
    while True:
        address = input("Please enter the address: ").strip()
        if not address:
            print("Error: The address cannot be empty. Please enter a valid address.")
            continue
        address = clean_data(address)
        if not re.match(r"^[A-Za-z0-9äöüÄÖÜß,\s'-]+$", address):
            print("Error: The address can only contain letters, spaces, apostrophes, or hyphens. Please enter a valid address.")
        else:
            print(f"Thank you! The address '{address}' has been successfully captured.")
            return address


def get_email():
    while True:
        email = input("Please enter the email: ").strip()
        if not email:
            print("Error: The email cannot be empty. Please enter a valid email.")
            continue
        email = email.lower()
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            print("Invalid email. Please enter a valid email.")
        else:
            print(f"Thank you! The email '{email}' has been successfully captured.")
            return email


def get_telephone_number():
    while True:
        telephone_number = input("Please enter the telephone number: ").strip()
        if not telephone_number:
            print("Error: The telephone number cannot be empty. Please enter a valid telephone number.")
            continue
        telephone_number = clean_data(telephone_number)
        telephone_number = re.sub(r"\s+", "", telephone_number)
        if not re.match(r"^[0-9\s'-`]+$", telephone_number):
            print("Error: The telephone number cannot be empty. Please enter a valid telephone number.")
        else:
            print(f"Thank you! The telephone number '{telephone_number}' has been successfully captured.")
            return telephone_number


def get_date_of_birth():
    while True:
        date_of_birth = input("Please enter the date of birth (DD/MM/YYYY): ").strip()
        if not date_of_birth:
            print("Error: The date of birth cannot be empty. Please enter a valid date of birth.")
            continue
        if not re.match(r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$", date_of_birth):
            print("Error: The date of birth must be in the format DD/MM/YYYY. Please enter a valid date.")
        else:
            print(f"Thank you! The date of birth '{date_of_birth}' has been successfully captured.")
            return date_of_birth


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
def add_new_visitor(visitors):
    print("Start adding a new Visitor")
    full_name = get_full_name()
    address = get_address()
    email = get_email()
    telephone_number = get_telephone_number()
    date_of_birth = get_date_of_birth()
    visitor_data = f"Name: {full_name}, Date of Birth: {date_of_birth}, Address: {address}, Email: {email}, Telephone: {telephone_number}, Type: Visitor"
    visitors.append(visitor_data)
    print("New Visitor successfully added!")


def add_new_employee(employees):
    print("Start adding a new Employee")
    full_name = get_full_name()
    address = get_address()
    email = get_email()
    telephone_number = get_telephone_number()
    date_of_birth = get_date_of_birth()
    employee_id = get_employee_id()
    employee_data = f"Name: {full_name}, Date of Birth: {date_of_birth}, Address: {address}, Email: {email}, Telephone: {telephone_number}, Employee ID: {employee_id}, Type: Employee"
    employees.append(employee_data)
    print("New Employee successfully added!")


# ----------------------------- Show All Functions ------------------------------
def show_all_visitors(visitors):
    if not visitors:
        print("No Visitors have been added yet.")
    else:
        print("------------- All Visitors ---------------")
        for index, visitor in enumerate(visitors, start=1):
            print(f"{index}. {visitor}")
            print("-------------------------------------------------------")


def show_all_employees(employees):
    if not employees:
        print("No employees have been added yet.")
    else:
        print("------------- All Employees ---------------")
        for index, employee in enumerate(employees, start=1):
            print(f"{index}. {employee}")
            print("-------------------------------------------------------")



# ----------------------------- Search Function ------------------------------

def search_visitors(visitors):
    if not visitors:
        print("No visitors to search.")
        return []

    search_visitor = input("Enter search term for visitors (Name, Email, or Telephone): ").strip().lower()
    found_visitors = [visitor for visitor in visitors if search_visitor in visitor.lower()]

    if found_visitors:
        print("Search Results for Visitors:")
        for index, visitor in enumerate(found_visitors, start=1):
            print(f"{index}. {visitor}")
            print("-------------------------------------------------------")
        return found_visitors  # Return the list of matching visitors
    else:
        print("No matching visitors found.")
        return []  # Return an empty list if no results


def search_employees(employees):
    if not employees:
        print("No employees to search.")
        return []

    search_employee = input("Enter search term for employees (Name, Email, Employee ID): ").strip().lower()
    found_employees = [employee for employee in employees if search_employee in employee.lower()]

    if found_employees:
        print("Search Results for Employees:")
        for index, employee in enumerate(found_employees, start=1):
            print(f"{index}. {employee}")
            print("-------------------------------------------------------")
        return found_employees  # Return the list of matching employees
    else:
        print("No matching employees found.")
        return []  # Return an empty list if no results


# ----------------------------- Update Functions ------------------------------

def update_visitor(visitors):
    matching_visitors = search_visitors(visitors)  # Get matching visitors
    if not matching_visitors:
        return  # Exit if no matching visitors

    try:
        visitor_index = int(input("Enter the number of the visitor you want to update: ")) - 1
        if 0 <= visitor_index < len(matching_visitors):
            visitor = matching_visitors[visitor_index]
            visitor_details = visitor.split(", ")
            print(f"Current details of the selected visitor:\n{visitor}")

            print("Select the field to update:")
            print("1. Name")
            print("2. Address")
            print("3. Email")
            print("4. Telephone")
            print("5. Date of Birth")
            field_choice = input("Enter the number of the field to update: ")

            if field_choice == '1':
                new_name = get_full_name()
                visitor_details[0] = f"Name: {new_name}"
            elif field_choice == '2':
                new_address = get_address()
                visitor_details[2] = f"Address: {new_address}"
            elif field_choice == '3':
                new_email = get_email()
                visitor_details[3] = f"Email: {new_email}"
            elif field_choice == '4':
                new_telephone = get_telephone_number()
                visitor_details[4] = f"Telephone: {new_telephone}"
            elif field_choice == '5':
                new_dob = get_date_of_birth()
                visitor_details[1] = f"Date of Birth: {new_dob}"
            else:
                print("Invalid choice. No updates made.")
                return

            # Update the visitor record in the full list
            visitor_str = ", ".join(visitor_details)
            visitors[visitors.index(matching_visitors[visitor_index])] = visitor_str
            print("Visitor details updated successfully!")
        else:
            print("Invalid choice. No updates made.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def update_employee(employees):
    matching_employees = search_employees(employees)  # Get matching employees
    if not matching_employees:
        return  # Exit if no matching employees

    try:
        employee_index = int(input("Enter the number of the employee you want to update: ")) - 1
        if 0 <= employee_index < len(matching_employees):
            employee = matching_employees[employee_index]
            employee_details = employee.split(", ")
            print(f"Current details of the selected employee:\n{employee}")

            print("Select the field to update:")
            print("1. Name")
            print("2. Address")
            print("3. Email")
            print("4. Telephone")
            print("5. Date of Birth")
            print("6. Employee ID")
            field_choice = input("Enter the number of the field to update: ")

            if field_choice == '1':
                new_name = get_full_name()
                employee_details[0] = f"Name: {new_name}"
            elif field_choice == '2':
                new_address = get_address()
                employee_details[2] = f"Address: {new_address}"
            elif field_choice == '3':
                new_email = get_email()
                employee_details[3] = f"Email: {new_email}"
            elif field_choice == '4':
                new_telephone = get_telephone_number()
                employee_details[4] = f"Telephone: {new_telephone}"
            elif field_choice == '5':
                new_dob = get_date_of_birth()
                employee_details[1] = f"Date of Birth: {new_dob}"
            elif field_choice == '6':
                new_emp_id = get_employee_id()
                employee_details[5] = f"Employee ID: {new_emp_id}"
            else:
                print("Invalid choice. No updates made.")
                return

            # Update the employee record in the full list
            employee_str = ", ".join(employee_details)
            employees[employees.index(matching_employees[employee_index])] = employee_str
            print("Employee details updated successfully!")
        else:
            print("Invalid choice. No updates made.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# ------------------------------- Main Program ------------------------------
def main():
    visitors = []
    employees = []

    while True:
        print("-------------------------------------------------------")
        print("Welcome to the Personal Data Collection Program!")
        print("1. Add new")
        print("2. Show all")
        print("3. Search")
        print("4. Update")
        print("5. Exit")

        choice = input("Please select an option (1-5): ").strip()

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
            print("1. Search Visitors")
            print("2. Search Employees")
            sub_choice = input("Select 1 or 2 to search: ").strip()
            if sub_choice == '1':
                search_visitors(visitors)
            elif sub_choice == '2':
                search_employees(employees)
            else:
                print("Invalid choice.")
        elif choice == '4':
            print("1. Update Visitor")
            print("2. Update Employee")
            sub_choice = input("Select 1 or 2 to update: ").strip()
            if sub_choice == '1':
                update_visitor(visitors)
            elif sub_choice == '2':
                update_employee(employees)
            else:
                print("Invalid choice.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select an option (1-5):")

# Run the main function
main()
