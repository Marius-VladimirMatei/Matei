from tkinter import *

# Data collector program with tkinter GUI

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


# Adding labels to the root window
lbl_title = Label(root, text = "Add new person", bg=label_bg, fg=label_fg, font=('Arial', 16, 'bold'))
lbl_title.grid(column = 0, row = 0, padx = 10, pady = 5, sticky = 'w')

lbl_name = Label(root, text = "Enter full name: ", bg=label_bg, fg=label_fg)
lbl_name.grid(column = 0, row = 1, padx = 10, pady = 5, sticky = 'w')

lbl_address = Label(root, text = "Enter address: ", bg=label_bg, fg=label_fg)
lbl_address.grid(column = 0, row = 2, padx = 10, pady = 5, sticky = 'w')

lbl_email = Label(root, text ="Enter e-mail address: ", bg=label_bg, fg=label_fg)
lbl_email.grid(column = 0, row = 3, padx = 10, pady = 5, sticky = 'w')

lbl_telephone = Label(root, text ="Enter telephone number: ", bg=label_bg, fg=label_fg)
lbl_telephone.grid(column = 0, row = 4, padx = 10, pady = 5, sticky = 'w')

lbl_date_of_birth = Label(root, text ="Enter date of birth (DD/MM/YY): ", bg=label_bg, fg=label_fg)
lbl_date_of_birth.grid(column = 0, row = 5, padx = 10, pady = 5, sticky = 'w')

lbl_employee_id = Label(root, text ="Enter employee ID: ", bg=label_bg, fg=label_fg)
lbl_employee_id.grid(column = 0, row = 6, padx = 10, pady = 5, sticky = 'w')

# Input fields
txt_name = Entry(root, width = 30, bg=entry_bg, fg=entry_fg)
txt_name.grid(column = 1, row = 1, padx = 10, pady = 5)

txt_address = Entry(root, width = 30, bg=entry_bg, fg=entry_fg)
txt_address.grid(column = 1, row = 2, padx = 10, pady = 5)

txt_email = Entry(root, width = 30, bg=entry_bg, fg=entry_fg)
txt_email.grid(column = 1, row = 3, padx = 10, pady = 5)

txt_telephone = Entry(root, width = 30, bg=entry_bg, fg=entry_fg)
txt_telephone.grid(column = 1, row = 4, padx = 10, pady = 5)

txt_date_of_birth = Entry(root, width = 30, bg=entry_bg, fg=entry_fg)
txt_date_of_birth.grid(column = 1, row = 5, padx = 10, pady = 5)

txt_employee_id = Entry(root, width = 30, bg=entry_bg, fg=entry_fg)
txt_employee_id.grid(column = 1, row = 6, padx = 10, pady = 5)

# Executes the main loop
root.mainloop()