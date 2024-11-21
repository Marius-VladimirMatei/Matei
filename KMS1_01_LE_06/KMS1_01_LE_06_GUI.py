from tkinter import *
from tkinter import messagebox
import re
import os

# Create root window
root = Tk()

# Root window title and dimension
root.title("Data Collector")

# Set geometry (width x height)
root.geometry('700x500')

# Set the dark theme colors
root.configure(bg='#2e2e2e')  # Dark background for the root window
label_bg = '#2e2e2e'  # Background color for labels
label_fg = '#dcdcdc'  # Light text color for labels
entry_bg = '#3c3f41'  # Dark background for entry fields
entry_fg = '#ffffff'  # Light text color for entry fields

# File paths for the data files
VISITOR_FILE = "visitors.txt"
EMPLOYEE_FILE = "employees.txt"

# ------------------------------ Validation ________________________________________
name_pattern = r"^[A-Za-zäöüÄÖÜß\s'-]+$"
address_pattern = r"^[A-Za-z0-9äöüÄÖÜß,\s'-]+$"
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
telephone_pattern = r"^[0-9\s'+-`]+$"
date_of_birth_pattern = r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$"
id_pattern = r"^\d+$"


def validate_name():
    name = txt_name.get().strip()
    if not re.match(name_pattern, name):
        messagebox.showerror("Invalid Name", "Please enter a valid name.")
        return False
    return True


def validate_address():
    address = txt_address.get().strip()
    if not re.match(address_pattern, address):
        messagebox.showerror("Invalid Address", "Please enter a valid address.")
        return False
    return True


def validate_email():
    email = txt_email.get().strip()
    if not re.match(email_pattern, email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return False
    return True


def validate_telephone():
    telephone = txt_telephone.get().strip()
    if not re.match(telephone_pattern, telephone):
        messagebox.showerror("Invalid Telephone", "Please enter a valid telephone number.")
        return False
    return True


def validate_date_of_birth():
    dob = txt_date_of_birth.get().strip()
    if not re.match(date_of_birth_pattern, dob):
        messagebox.showerror("Invalid Date of Birth", "Please enter a valid date of birth (DD/MM/YYYY).")
        return False
    return True


def validate_employee_id():
    emp_id = txt_employee_id.get().strip()
    if not re.match(id_pattern, emp_id):
        messagebox.showerror("Invalid Employee ID", "Please enter a valid employee ID (numeric).")
        return False
    return True


def validate():
    # Validate each field
    if (validate_name() and validate_address() and validate_email() and
            validate_telephone() and validate_date_of_birth() and validate_employee_id()):
        save_data()  # If all fields are valid, save the data
    else:
        messagebox.showerror("Error", "Please correct the errors in the form.")


# ----------------------------- Save Data Function --------------------------------

def save_data():
    name = txt_name.get().strip()
    address = txt_address.get().strip()
    email = txt_email.get().strip()
    telephone = txt_telephone.get().strip()
    date_of_birth = txt_date_of_birth.get().strip()
    employee_id = txt_employee_id.get().strip()

    # Create a person dictionary to store the data
    person_data = {
        "name": name,
        "address": address,
        "email": email,
        "telephone": telephone,
        "date_of_birth": date_of_birth,
        "employee_id": employee_id
    }

    # Check if the person is an employee or a visitor
    if employee_id:
        # Employee: Add to employee list
        employee_list.append(person_data)
        save_to_file(EMPLOYEE_FILE, employee_list)  # Save updated data to file
        messagebox.showinfo("Success", "Employee data saved successfully!")
    else:
        # Visitor: Add to visitor list
        visitor_list.append(person_data)
        save_to_file(VISITOR_FILE, visitor_list)  # Save updated data to file
        messagebox.showinfo("Success", "Visitor data saved successfully!")

    # Optionally, clear the fields after saving the data
    clear_fields()


# ----------------------------- Clear Fields Function --------------------------------
def clear_fields():
    txt_name.delete(0, END)
    txt_address.delete(0, END)
    txt_email.delete(0, END)
    txt_telephone.delete(0, END)
    txt_date_of_birth.delete(0, END)
    txt_employee_id.delete(0, END)


# ----------------------------- Display All Visitors/Employees --------------------
def display_all_visitors():
    display_data(VISITOR_FILE, "Visitors")


def display_all_employees():
    display_data(EMPLOYEE_FILE, "Employees")


def display_data(file_path, title):
    # Create a new window to display the data
    display_window = Toplevel(root)
    display_window.title(f"All {title}")
    display_window.geometry("500x300")

    # Add a scrollbar
    scrollbar = Scrollbar(display_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(display_window, width=80, height=15, yscrollcommand=scrollbar.set)
    listbox.pack(padx=10, pady=10)
    scrollbar.config(command=listbox.yview)

    # Read data from file and add to listbox
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                listbox.insert(END, line.strip())  # Add each line from file to the listbox


# ----------------------------- File Handling Functions ---------------------------
def load_from_file(file_path):
    # Load data from the file (if it exists)
    data_list = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                # Split each line by commas and create a dictionary
                fields = line.strip().split(',')
                if len(fields) == 6:
                    person_data = {
                        "name": fields[0],
                        "address": fields[1],
                        "email": fields[2],
                        "telephone": fields[3],
                        "date_of_birth": fields[4],
                        "employee_id": fields[5]
                    }
                    data_list.append(person_data)
    return data_list


def save_to_file(file_path, data):
    # Save data to the file
    with open(file_path, "w") as file:
        for person in data:
            # Write each person as a comma-separated line
            file.write(
                f"{person['name']},{person['address']},{person['email']},{person['telephone']},{person['date_of_birth']},{person['employee_id']}\n")


# ---------------------------------------------------------------------------------
# Visitor and Employee Lists
visitor_list = load_from_file(VISITOR_FILE)  # Load existing visitors from file
employee_list = load_from_file(EMPLOYEE_FILE)  # Load existing employees from file

# ---------------------------- input fields -----------------------------------------

# Adding labels and input fields to the root window
lbl_title = Label(root, text="Add new person", bg=label_bg, fg=label_fg, font=('Arial', 16, 'bold'))
lbl_title.grid(column=0, row=0, padx=10, pady=5, sticky='w')

lbl_name = Label(root, text="Enter full name: ", bg=label_bg, fg=label_fg)
lbl_name.grid(column=0, row=1, padx=10, pady=5, sticky='w')
txt_name = Entry(root, width=30, bg=entry_bg, fg=entry_fg)
txt_name.grid(column=1, row=1, padx=10, pady=5)

lbl_address = Label(root, text="Enter address: ", bg=label_bg, fg=label_fg)
lbl_address.grid(column=0, row=2, padx=10, pady=5, sticky='w')
txt_address = Entry(root, width=30, bg=entry_bg, fg=entry_fg)
txt_address.grid(column=1, row=2, padx=10, pady=5)

lbl_email = Label(root, text="Enter e-mail address: ", bg=label_bg, fg=label_fg)
lbl_email.grid(column=0, row=3, padx=10, pady=5, sticky='w')
txt_email = Entry(root, width=30, bg=entry_bg, fg=entry_fg)
txt_email.grid(column=1, row=3, padx=10, pady=5)

lbl_telephone = Label(root, text="Enter telephone number: ", bg=label_bg, fg=label_fg)
lbl_telephone.grid(column=0, row=4, padx=10, pady=5, sticky='w')
txt_telephone = Entry(root, width=30, bg=entry_bg, fg=entry_fg)
txt_telephone.grid(column=1, row=4, padx=10, pady=5)

lbl_date_of_birth = Label(root, text="Enter date of birth (DD/MM/YYYY): ", bg=label_bg, fg=label_fg)
lbl_date_of_birth.grid(column=0, row=5, padx=10, pady=5, sticky='w')
txt_date_of_birth = Entry(root, width=30, bg=entry_bg, fg=entry_fg)
txt_date_of_birth.grid(column=1, row=5, padx=10, pady=5)

lbl_employee_id = Label(root, text="Enter employee ID (if applicable): ", bg=label_bg, fg=label_fg)
lbl_employee_id.grid(column=0, row=6, padx=10, pady=5, sticky='w')
txt_employee_id = Entry(root, width=30, bg=entry_bg, fg=entry_fg)
txt_employee_id.grid(column=1, row=6, padx=10, pady=5)

# Save button to save data
btn_save = Button(root, text="Save", command=validate, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))
btn_save.grid(column=1, row=7, pady=20)

# Button to show all visitors
btn_show_visitors = Button(root, text="Show Visitors", command=display_all_visitors, bg="#4CAF50", fg="white",
                           font=("Arial", 12))
btn_show_visitors.grid(column=0, row=8, padx=10, pady=5)

# Button to show all employees
btn_show_employees = Button(root, text="Show Employees", command=display_all_employees, bg="#4CAF50", fg="white",
                            font=("Arial", 12))
btn_show_employees.grid(column=1, row=8, padx=10, pady=5)

# Run the main loop
root.mainloop()
