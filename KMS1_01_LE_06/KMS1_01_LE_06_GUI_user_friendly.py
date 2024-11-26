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

"""
def get_validated_input(prompt, pattern):
    while True:
        value = simpledialog.askstring("Input", prompt)
        if value is None:  # User cancelled
            return None
        if re.match(pattern, value):
            return value
        else:
            messagebox.showerror("Invalid Input", "The input does not match the required format. Please try again.")
"""

# ------------------------------- File Load / Save in file Functions --------------------------------

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


# ------------------------ Add new Visitor / Employee functions --------------------

def add_new_person(person_type):
    # Create the Toplevel popup window
    popup = tk.Toplevel()
    popup.title(f"Add New {person_type}")
    popup.geometry("400x350")
    popup.config(bg="#333333")  # Dark theme background for the popup


    # Configure style for TButton and TFrame
    #style = ttk.Style()
    #style.configure("TButton", background="#555555", foreground="black", font=("Arial", 12,), padding=10)
    #style.configure("TLabel", background="#333333", foreground="white", font=("Arial", 10))  # Style for labels


    # Variables to hold input data
    name_var = tk.StringVar()
    address_var = tk.StringVar()
    email_var = tk.StringVar()
    telephone_var = tk.StringVar()
    dob_var = tk.StringVar()
    employee_id_var = tk.StringVar()

    # Function to save person data
    def save_person():
        name = name_var.get().strip()
        address = address_var.get().strip()
        email = email_var.get().strip()
        telephone = telephone_var.get().strip()
        dob = dob_var.get().strip()
        employee_id = employee_id_var.get().strip()

        # Input fields
        if not re.match(name_pattern, name):
            messagebox.showerror("Error", "Invalid Name!", parent=popup)
            return
        if not re.match(address_pattern, address):
            messagebox.showerror("Error", "Invalid Address!", parent=popup)
            return
        if not re.match(email_pattern, email):
            messagebox.showerror("Error", "Invalid Email!", parent=popup)
            return
        if not re.match(telephone_pattern, telephone):
            messagebox.showerror("Error", "Invalid Telephone!", parent=popup)
            return
        if not re.match(date_of_birth_pattern, dob):
            messagebox.showerror("Error", "Invalid Date of Birth! Use DD/MM/YYYY format.", parent=popup)
            return
        if person_type == "Employee" and not re.match(id_pattern, employee_id):
            messagebox.showerror("Error", "Invalid Employee ID!", parent=popup)
            return

        # Person data string
        person_data = f"Name: {capitalize_words(name)}, Date of Birth: {dob}, Address: {capitalize_words(address)}, Email: {email}, Telephone: {telephone}"
        if person_type == "Employee":
            person_data += f", Employee ID: {employee_id}, Type: Employee"
            employees.append(person_data)
            save_data('employees.txt', employees)
        else:
            person_data += ", Type: Visitor"
            visitors.append(person_data)
            save_data('visitors.txt', visitors)

        messagebox.showinfo("Success", f"New {person_type.lower()} added successfully!", parent=popup)
        popup.destroy()

    # Frame for widgets
    frame = ttk.Frame(popup, padding="10", style="TFrame")
    frame.pack(fill=tk.BOTH, expand=True)

    # Layout with ttk themed tkinter Widgets
    ttk.Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(frame, textvariable=name_var, width=30).grid(row=0, column=1, padx=10, pady=5)
    ttk.Label(frame, text="Address:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(frame, textvariable=address_var, width=30).grid(row=1, column=1, padx=10, pady=5)
    ttk.Label(frame, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(frame, textvariable=email_var, width=30).grid(row=2, column=1, padx=10, pady=5)
    ttk.Label(frame, text="Telephone:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(frame, textvariable=telephone_var, width=30).grid(row=3, column=1, padx=10, pady=5)
    ttk.Label(frame, text="Date of Birth:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    ttk.Entry(frame, textvariable=dob_var, width=30).grid(row=4, column=1, padx=10, pady=5)

    if person_type == "Employee":
        ttk.Label(frame, text="Employee ID:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        ttk.Entry(frame, textvariable=employee_id_var, width=30).grid(row=5, column=1, padx=10, pady=5)

    ttk.Button(frame, text="Save", command=save_person).grid(row=6, column=1, pady=15)

def add_new_visitor():
    add_new_person("Visitor")

def add_new_employee():
    add_new_person("Employee")

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
    choice = simpledialog.askstring("Search", "Enter 1 for Visitors or 2 for Employees:", parent=root)
    if choice == '1':
        search_visitors()
    elif choice == '2':
        search_employees()
    else:
        messagebox.showerror("Error", "Invalid choice", parent=root)


def search_visitors():
    search_term = simpledialog.askstring("Search Visitors", "Enter search term:", parent=root)
    if search_term:
        results = [v for v in visitors if search_term.lower() in v.lower()]
        display_search_results(results)


def search_employees():
    search_term = simpledialog.askstring("Search Employees", "Enter search term:", parent=root)
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

def update(entry_type, entry_list, filename):
    search_term = simpledialog.askstring(f"Update {entry_type}", f"Enter search term for {entry_type.lower()}:", parent=root)
    if search_term:
        matching_entries = [e for e in entry_list if search_term.lower() in e.lower()]
        if not matching_entries:
            messagebox.showinfo("No Results", f"No matching {entry_type.lower()}s found.")
            return

        # Display results and select entry to update
        result_text.delete(1.0, tk.END)
        for i, entry in enumerate(matching_entries, 1):
            result_text.insert(tk.END, f"{i}. {entry}\n\n")

        index = simpledialog.askinteger(f"Select {entry_type}",
                                        f"Enter the number of the {entry_type.lower()} to update:", minvalue=1,
                                        maxvalue=len(matching_entries), parent=root)
        if index is None:
            return

        # Get selected entry details
        selected_entry = matching_entries[index - 1]
        entry_details = selected_entry.split(", ")

        # Create a popup window for updating
        popup = tk.Toplevel()
        popup.title(f"Update {entry_type}")
        popup.geometry("400x400")
        popup.config(bg="#333333")  # Dark theme background for the popup


        # Variables to hold updated data
        fields = {}

        # Create input fields for each detail
        row_index = 0
        for i, detail in enumerate(entry_details):
            field_name, current_value = detail.split(": ")
            if field_name == "Type":
                ttk.Label(popup, text=f"{field_name}: {current_value}").grid(row=row_index, column=0, columnspan=2, padx=10, pady=5)

            else:
                fields[field_name] = tk.StringVar(value=current_value)

                ttk.Label(popup, text=f"{field_name}:").grid(row=i, column=0, padx=10, pady=5, sticky="e")
                ttk.Entry(popup, textvariable=fields[field_name], width=30).grid(row=i, column=1, padx=10, pady=5)
                row_index += 1

        def save_updated_entry():
            updated_details = [f"{field}: {capitalize_words(var.get())}" for field, var in fields.items()]
            updated_entry = ", ".join(updated_details)

            index_in_main_list = entry_list.index(selected_entry)
            entry_list[index_in_main_list] = updated_entry
            save_data(filename, entry_list)

            messagebox.showinfo("Success", f"{entry_type} updated successfully!")
            popup.destroy()
            #show_all_entries(entry_type)

        ttk.Button(popup, text="Save", command=save_updated_entry).grid(row=len(entry_details), column=1, pady=15)


def update_visitor():
    update("Visitor", visitors, 'visitors.txt')


def update_employee():
    update("Employee", employees, 'employees.txt')



# ----------------------------- Delete Function ------------------------------

def delete():
    choice = simpledialog.askstring("Delete", "Enter 1 for Visitors or 2 for Employees:", parent=root)
    if choice == '1':
        delete_visitor()
    elif choice == '2':
        delete_employee()
    else:
        messagebox.showerror("Error", "Invalid choice")


def delete_visitor():
    search_term = simpledialog.askstring("Delete Visitor", "Enter search term for visitor:", parent=root)
    if search_term:
        matching_visitors = [v for v in visitors if search_term.lower() in v.lower()]
        if not matching_visitors:
            messagebox.showinfo("No Results", "No matching visitors found.")
            return

        result_text.delete(1.0, tk.END)
        for i, visitor in enumerate(matching_visitors, 1):
            result_text.insert(tk.END, f"{i}. {visitor}\n\n")

        index = simpledialog.askinteger("Select Visitor", "Enter the number of the visitor to delete:", minvalue=1,
                                        maxvalue=len(matching_visitors), parent=root)
        if index is None:
            return

        visitor_to_delete = matching_visitors[index - 1]
        visitors.remove(visitor_to_delete)
        save_data('visitors.txt', visitors)

        messagebox.showinfo("Success", "Visitor deleted successfully!")
        show_all_visitors()


def delete_employee():
    search_term = simpledialog.askstring("Delete Employee", "Enter search term for employee:", parent=root)
    if search_term:
        matching_employees = [e for e in employees if search_term.lower() in e.lower()]
        if not matching_employees:
            messagebox.showinfo("No Results", "No matching employees found.")
            return

        result_text.delete(1.0, tk.END)
        for i, employee in enumerate(matching_employees, 1):
            result_text.insert(tk.END, f"{i}. {employee}\n\n")

        index = simpledialog.askinteger("Select Employee", "Enter the number of the employee to delete:", minvalue=1, maxvalue=len(matching_employees), parent=root)
        if index is None:
            return

        employee_to_delete = matching_employees[index - 1]
        employees.remove(employee_to_delete)
        save_data('employees.txt', employees)

        messagebox.showinfo("Success", "Employee deleted successfully!")
        show_all_employees()


# ----------------------------- Tkinter UI Setup ------------------------------

def main():
    global visitors, employees, result_text, root

    visitors = load_data('visitors.txt')
    employees = load_data('employees.txt')

    root = tk.Tk()
    root.title("Personal Data Collection Program")
    root.geometry("800x700")

    # Dark theme colors
    root.config(bg="#333333")

    main_frame = ttk.Frame(root, padding="10", style="Dark.TFrame")
    main_frame.pack(fill=tk.BOTH, expand=True)



    # ------------------------ Dropdown button for ADD NEW Visitor or Employee ------------------------
    dropdown_button = ttk.Menubutton(main_frame, text="Add New", style="TButton")
    #dropdown_button.pack(fill=tk.X, pady=5)
    dropdown_button.pack(anchor="center", pady=5)


    # Create a menu for the dropdown button
    add_menu = tk.Menu(dropdown_button, tearoff=0)
    add_menu.add_command(label="Add New Visitor", command=add_new_visitor)
    add_menu.add_command(label="Add New Employee", command=add_new_employee)

    # Attach the menu to the dropdown button
    dropdown_button["menu"] = add_menu


    #------------------------- Dropdown button for SHOW ALL Visitors or Employees ------------------------
    dropdown_button = ttk.Menubutton(main_frame, text="Show All", style="TButton")
    dropdown_button.pack(anchor="center", pady=5)

    # Create a menu for the dropdown button
    add_menu = tk.Menu(dropdown_button, tearoff=0)
    add_menu.add_command(label="Show all Visitors", command=show_all_visitors)
    add_menu.add_command(label="Show all Employees", command=show_all_employees)

    # Attach the menu to the dropdown button
    dropdown_button["menu"] = add_menu


    # ------------------------- Dropdown button for SEARCH Visitors or Employees ------------------------
    dropdown_button = ttk.Menubutton(main_frame, text="Search", style="TButton")
    dropdown_button.pack(anchor="center", pady=5)

    # Create a menu for the dropdown button
    add_menu = tk.Menu(dropdown_button, tearoff=0)
    add_menu.add_command(label="Search Visitor", command=search_visitors)
    add_menu.add_command(label="Search Employee", command=search_employees)

    # Attach the menu to the dropdown button
    dropdown_button["menu"] = add_menu

    # ------------------------- Dropdown button for UPDATE Visitors or Employees ------------------------
    dropdown_button = ttk.Menubutton(main_frame, text="Update", style="TButton")
    dropdown_button.pack(anchor="center", pady=5)

    # Create a menu for the dropdown button
    add_menu = tk.Menu(dropdown_button, tearoff=0)
    add_menu.add_command(label="Update Visitor", command=update_visitor)
    add_menu.add_command(label="Update Employee", command=update_employee)

    # Attach the menu to the dropdown button
    dropdown_button["menu"] = add_menu

    # ------------------------- Dropdown button for DELETE Visitors or Employees ------------------------
    dropdown_button = ttk.Menubutton(main_frame, text="Delete", style="TButton")
    dropdown_button.pack(anchor="center", pady=5)

    # Create a menu for the dropdown button
    add_menu = tk.Menu(dropdown_button, tearoff=0)
    add_menu.add_command(label="Delete Visitor", command=delete_visitor)
    add_menu.add_command(label="Delete Employee", command=delete_employee)

    # Attach the menu to the dropdown button
    dropdown_button["menu"] = add_menu

    # ------------------------- Buttons for other main menu functions -------------------------------------

    ttk.Button(main_frame, text="Exit", command=root.quit, style="TButton").pack(anchor="center", pady=5)

    # Text widget to show results
    result_text = tk.Text(main_frame, height=20, width=100, font=("Arial", 10))
    result_text.pack(pady=10)

    # Styling for buttons and other widgets
    style = ttk.Style()
    style.configure("TButton", background="#555555", foreground="black", font=("Arial", 12), padding=10)
    style.configure("TFrame", background="#333333")
    style.configure("TLabel", background="#333333", foreground="white", font=("Arial", 10))  # Style for labels
    style.configure("TEntry", padding=5)  # Ensure entries are styled

    root.mainloop()

main()




