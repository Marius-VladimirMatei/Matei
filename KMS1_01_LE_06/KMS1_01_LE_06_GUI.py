import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import re
import os

# ---------------------------------- Patterns for validation --------------------------------
name_pattern = r"^[A-Za-zäöüÄÖÜß\s'-]+$"
address_pattern = r"^[A-Za-z0-9äöüÄÖÜß,\s'-]+$"
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
telephone_pattern = r"^[0-9\s'+-`]+$"
date_of_birth_pattern = r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$"
id_pattern = r"^\d+$"


# ------------------------------- Data Clean function --------------------------------
def clean_data(data):
    data = data.strip()
    data = re.sub(r'\s+', ' ', data)
    return ' '.join(word.capitalize() for word in data.split())


# method to capitalize every word
def capitalize_words(data):
    data = data.strip()
    data = re.sub(r'\s+', ' ', data)  # Remove extra spaces
    return ' '.join([word.capitalize() for word in data.split()])


# ------------------------------- File Save / Load Functions --------------------------------
def load_data(filename):
    data = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = [line.strip() for line in file.readlines()]
    return data


def save_data(filename, data):
    with open(filename, 'w') as file:
        for entry in data:
            file.write(entry + '\n')


# ------------------------ Main Program Functions -----------------------

def get_validated_input(prompt, pattern):
    while True:
        value = simpledialog.askstring("Input", prompt)
        if value is None:  # User cancelled
            return None
        if re.match(pattern, value):
            return value
        else:
            messagebox.showerror("Invalid Input", "The input does not match the required format. Please try again.")


# ------------------------ Add new Visitor / Employee functions --------------------
def add_new_visitor():
    name = get_validated_input("Enter full name:", name_pattern)
    if not name:
        return
    address = get_validated_input("Enter address:", address_pattern)
    if not address:
        return
    email = get_validated_input("Enter email:", email_pattern)
    if not email:
        return
    telephone = get_validated_input("Enter telephone number:", telephone_pattern)
    if not telephone:
        return
    dob = get_validated_input("Enter date of birth (DD/MM/YYYY):", date_of_birth_pattern)
    if not dob:
        return

    visitor_data = f"Name: {capitalize_words(name)}, Date of Birth: {dob}, Address: {capitalize_words(address)}, Email: {email}, Telephone: {telephone}, Type: Visitor"
    visitors.append(visitor_data)
    save_data('visitors.txt', visitors)
    messagebox.showinfo("Success", "New visitor added successfully!")


def add_new_employee():
    name = get_validated_input("Enter full name:", name_pattern)
    if not name:
        return
    address = get_validated_input("Enter address:", address_pattern)
    if not address:
        return
    email = get_validated_input("Enter email:", email_pattern)
    if not email:
        return
    telephone = get_validated_input("Enter telephone number:", telephone_pattern)
    if not telephone:
        return
    dob = get_validated_input("Enter date of birth (DD/MM/YYYY):", date_of_birth_pattern)
    if not dob:
        return
    employee_id = get_validated_input("Enter Employee ID:", id_pattern)
    if not employee_id:
        return

    employee_data = f"Name: {capitalize_words(name)}, Date of Birth: {dob}, Address: {capitalize_words(address)}, Email: {email}, Telephone: {telephone}, Employee ID: {employee_id}, Type: Employee"
    employees.append(employee_data)
    save_data('employees.txt', employees)
    messagebox.showinfo("Success", "New employee added successfully!")


# ----------------------------- Show All Functions ------------------------------
def show_all_visitors():
    result_text.delete(1.0, tk.END)
    if not visitors:
        result_text.insert(tk.END, "No visitors have been added yet.")
    else:
        for index, visitor in enumerate(visitors, start=1):
            result_text.insert(tk.END, f"{index}. {visitor}\n\n")


def show_all_employees():
    result_text.delete(1.0, tk.END)
    if not employees:
        result_text.insert(tk.END, "No employees have been added yet.")
    else:
        for index, employee in enumerate(employees, start=1):
            result_text.insert(tk.END, f"{index}. {employee}\n\n")


# ----------------------------- Search Function ------------------------------
def search():
    choice = simpledialog.askstring("Search", "Enter 1 for Visitors or 2 for Employees:")
    if choice == '1':
        search_visitors()
    elif choice == '2':
        search_employees()
    else:
        messagebox.showerror("Error", "Invalid choice")


def search_visitors():
    search_term = simpledialog.askstring("Search Visitors", "Enter search term:")
    if search_term:
        results = [v for v in visitors if search_term.lower() in v.lower()]
        display_search_results(results)


def search_employees():
    search_term = simpledialog.askstring("Search Employees", "Enter search term:")
    if search_term:
        results = [e for e in employees if search_term.lower() in e.lower()]
        display_search_results(results)


def display_search_results(results):
    result_text.delete(1.0, tk.END)
    if not results:
        result_text.insert(tk.END, "No matching results found.")
    else:
        for index, result in enumerate(results, start=1):
            result_text.insert(tk.END, f"{index}. {result}\n\n")


# ----------------------------- Update Functions ------------------------------
def update():
    choice = simpledialog.askstring("Update", "Enter 1 for Visitors or 2 for Employees:")
    if choice == '1':
        update_visitor()
    elif choice == '2':
        update_employee()
    else:
        messagebox.showerror("Error", "Invalid choice")


def update_visitor():
    search_term = simpledialog.askstring("Update Visitor", "Enter search term for visitor:")
    if search_term:
        matching_visitors = [v for v in visitors if search_term.lower() in v.lower()]
        if not matching_visitors:
            messagebox.showinfo("No Results", "No matching visitors found.")
            return

        result_text.delete(1.0, tk.END)
        for i, visitor in enumerate(matching_visitors, 1):
            result_text.insert(tk.END, f"{i}. {visitor}\n\n")

        index = simpledialog.askinteger("Select Visitor", "Enter the number of the visitor to update:", minvalue=1,
                                        maxvalue=len(matching_visitors))
        if index is None:
            return

        visitor = matching_visitors[index - 1]
        visitor_details = visitor.split(", ")

        field = simpledialog.askstring("Update Field",
                                       "Enter field to update (Name, Date of Birth, Address, Email, Telephone):")
        if field:
            new_value = simpledialog.askstring("New Value", f"Enter new value for {field}:")
            if new_value:
                for i, detail in enumerate(visitor_details):
                    if detail.lower().startswith(field.lower()):
                        visitor_details[i] = f"{field}: {capitalize_words(new_value)}"
                        break
                else:
                    messagebox.showerror("Error", f"Field '{field}' not found.")
                    return

        updated_visitor = ", ".join(visitor_details)
        index_in_main_list = visitors.index(visitor)
        visitors[index_in_main_list] = updated_visitor
        save_data('visitors.txt', visitors)
        messagebox.showinfo("Success", "Visitor updated successfully!")
        show_all_visitors()


def update_employee():
    search_term = simpledialog.askstring("Update Employee", "Enter search term for employee:")
    if search_term:
        matching_employees = [e for e in employees if search_term.lower() in e.lower()]
        if not matching_employees:
            messagebox.showinfo("No Results", "No matching employees found.")
            return

        result_text.delete(1.0, tk.END)
        for i, employee in enumerate(matching_employees, 1):
            result_text.insert(tk.END, f"{i}. {employee}\n\n")

        index = simpledialog.askinteger("Select Employee", "Enter the number of the employee to update:", minvalue=1,
                                        maxvalue=len(matching_employees))
        if index is None:
            return

        employee = matching_employees[index - 1]
        employee_details = employee.split(", ")

        field = simpledialog.askstring("Update Field",
                                       "Enter field to update (Name, Date of Birth, Address, Email, Telephone, Employee ID):")
        if field:
            new_value = simpledialog.askstring("New Value", f"Enter new value for {field}:")
            if new_value:
                for i, detail in enumerate(employee_details):
                    if detail.lower().startswith(field.lower()):
                        employee_details[i] = f"{field}: {capitalize_words(new_value)}"
                        break
                else:
                    messagebox.showerror("Error", f"Field '{field}' not found.")
                    return

        updated_employee = ", ".join(employee_details)
        index_in_main_list = employees.index(employee)
        employees[index_in_main_list] = updated_employee
        save_data('employees.txt', employees)
        messagebox.showinfo("Success", "Employee updated successfully!")
        show_all_employees()


# ----------------------------- Tkinter UI Setup ------------------------------
def main():
    global visitors, employees, result_text

    visitors = load_data('visitors.txt')
    employees = load_data('employees.txt')

    root = tk.Tk()
    root.title("Personal Data Collection Program")
    root.geometry("900x600")

    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Create buttons for main menu functions
    ttk.Button(main_frame, text="Add New Visitor", command=add_new_visitor).pack(fill=tk.X, pady=5)
    ttk.Button(main_frame, text="Add New Employee", command=add_new_employee).pack(fill=tk.X, pady=5)
    ttk.Button(main_frame, text="Show All Visitors", command=show_all_visitors).pack(fill=tk.X, pady=5)
    ttk.Button(main_frame, text="Show All Employees", command=show_all_employees).pack(fill=tk.X, pady=5)
    ttk.Button(main_frame, text="Search", command=search).pack(fill=tk.X, pady=5)
    ttk.Button(main_frame, text="Update", command=update).pack(fill=tk.X, pady=5)
    ttk.Button(main_frame, text="Exit", command=root.quit).pack(fill=tk.X, pady=5)

    # Text widget to show results
    result_text = tk.Text(main_frame, height=20, width=100, font=("Arial", 10))
    result_text.pack(pady=10)

    root.mainloop()


main()
