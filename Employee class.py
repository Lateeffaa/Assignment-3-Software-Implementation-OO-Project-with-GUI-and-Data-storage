import pickle
import tkinter as tk
from tkinter import ttk

class Employee:
    """Class to represent the employee information"""

    def __init__(self, name, empID, department, jobTitle, basicSalary, age, dateOfBirth, passportID, passportExpiry,
                 managerID):
        self.name = name
        self.empID = int(empID)
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = float(basicSalary)
        self.age = int(age)
        self.dateOfBirth = dateOfBirth
        self.passportID = passportID
        self.passportExpiry = passportExpiry
        self.managerID = int(managerID)

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setempID(self, empID):
        self.empID = empID
    def getEmpID(self):
        return self.empID

    def setDepartment(self, department):
        self.department = department

class EmployeeGUI:
    """Class to represent the employee GUI system that the employee fills in"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x250")
        self.root.title("Employee Management System")

        self.name_lbl = tk.Label(self.root, text="Name:")
        self.name_lbl.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.nameEntry = tk.Entry(self.root)
        self.nameEntry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        self.empID_lbl = tk.Label(self.root, text="Employee ID:")
        self.empID_lbl.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.empID_entry = tk.Entry(self.root)
        self.empID_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.department_lbl = tk.Label(self.root, text="Department:")
        self.department_lbl.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.departmentEntry = tk.Entry(self.root)
        self.departmentEntry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.jobTitle_lbl = tk.Label(self.root, text="Job Title:")
        self.jobTitle_lbl.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.jobTitle_entry = tk.Entry(self.root)
        self.jobTitle_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.basicSalary_lbl = tk.Label(self.root, text="Basic Salary:")
        self.basicSalary_lbl.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.basicSalary_entry = tk.Entry(self.root)
        self.basicSalary_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.age_lbl = tk.Label(self.root, text="Age:")
        self.age_lbl.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.ageEntry = tk.Entry(self.root)
        self.ageEntry.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        self.dateOfBirth_lbl = tk.Label(self.root, text="Date of Birth:")
        self.dateOfBirth_lbl.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
        self.dateOfBirth_entry = tk.Entry(self.root)
        self.dateOfBirth_entry.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

        self.passportID_lbl = tk.Label(self.root, text="Passport ID:")
        self.passportID_lbl.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        self.passportID_entry = tk.Entry(self.root)
        self.passportID_entry.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)

        self.passportExpiry_lbl = tk.Label(self.root, text="Passport Expiry Date:")
        self.passportExpiry_lbl.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
        self.passportExpiry_entry = tk.Entry(self.root)
        self.passportExpiry_entry.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)

        self.managerID_lbl = tk.Label(self.root, text="Manager ID:")
        self.managerID_lbl.grid(column=0, row=9, sticky=tk.W, padx=5, pady=5)
        self.managerID_entry = tk.Entry(self.root)
        self.managerID_entry.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(column=1, row=10, padx=5, pady=5)
        self.root.mainloop()

    def clearBoxes(self):
        # Clear all entry boxes
        for entry in (self.nameEntry, self.empID_entry, self.departmentEntry, self.jobTitle_entry,
                      self.basicSalary_entry, self.ageEntry, self.dateOfBirth_entry, self.passportID_entry,
                      self.passportExpiry_entry, self.managerID_entry):
            entry.delete(0, tk.END)

    def submit(self):
        name = self.nameEntry.get()
        empID = self.empID_entry.get()
        department = self.departmentEntry.get()
        jobTitle = self.jobTitle_entry.get()
        basicSalary = self.basicSalary_entry.get()
        age = self.ageEntry.get()
        dob = self.dateOfBirth_entry.get()
        passportID = self.passportID_entry.get()
        passportExpiry = self.passportExpiry_entry.get()
        managerID = self.managerID_entry.get()

        # Check if employee ID already exists
        if empID in allEmployees:
            print("Employee with Employee ID", empID, "already exists.")
        else:
            employee = Employee(name, empID, department, jobTitle, basicSalary, age, dob, passportID, passportExpiry,
                                managerID)
            allEmployees[empID] = employee
            with open("employee.pkl", "ab") as file:
                pickle.dump(employee, file)
            self.table.insert('', 'end', values=(
                employee.name, employee.empID, employee.department, employee.jobTitle, employee.basicSalary,
                employee.age, employee.dob, employee.passportID, employee.passportExpiry, employee.managerID))

            self.clearBoxes()
            print("Employee added successfully. Employee ID:", empID)


class EmployeeList:
    """Class to represent the employees list in the GUI"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Employee Information List")

        self.table = ttk.Treeview(self.root, columns=(
        'Name', 'Employee ID', 'Department', 'Job Title', 'Basic Salary', 'Age', 'Date of Birth', 'Passport ID',
        'Passport Expiry Date', 'Manager ID'), show='headings')
        self.table.heading('Name', text='Name')
        self.table.heading('Employee ID', text='Employee ID')
        self.table.heading('Department', text='Department')
        self.table.heading('Job Title', text='Job Title')
        self.table.heading('Basic Salary', text='Basic Salary')
        self.table.heading('Age', text='Age')
        self.table.heading('Date of Birth', text='Date of Birth')
        self.table.heading('Passport ID', text='Passport ID')
        self.table.heading('Passport Expiry Date', text='Passport Expiry Date')
        self.table.heading('Manager ID', text='Manager ID')
        self.table.pack(pady=20)

        self.search_lbl = tk.Label(self.root, text="Search by Employee ID:")
        self.search_lbl.pack(pady=5)
        self.searchEntry = tk.Entry(self.root)
        self.searchEntry.pack(pady=5)
        self.search_btn = tk.Button(self.root, text="Search", command=self.searchEmp)
        self.search_btn.pack(pady=5)

        self.edit_btn = tk.Button(self.root, text="Edit", command=self.editEmp)
        self.edit_btn.pack(pady=10)

        self.delete_btn = tk.Button(self.root, text="Delete", command=self.deleteEmp)
        self.delete_btn.pack(pady=10)

        self.loadEmployees()  # Load employees when initializing the GUI

        self.root.mainloop()
        try:
            with open('employees.pkl', 'rb') as file:
                while True:
                    employee = pickle.load(file)
                    if isinstance(employee, Employee):
                        self.table.insert('', 'end', values=(employee.name, employee.empID, employee.department, employee.jobTitle, employee.basicSalary, employee.age, employee.dob, employee.passportID, employee.passportExpiry, employee.managerID))
        except FileNotFoundError:
            pass
        except EOFError:
            pass

        self.root.mainloop()
    def searchEmp(self):
        empID = self.searchEntry.get()
        if empID in allEmployees:
            employee = allEmployees[empID]
            self.table.delete(*self.table.get_children())  # Clear table
            self.table.insert('', 'end', values=(
            employee.name, employee.empID, employee.department, employee.jobTitle, employee.basicSalary, employee.age,
            employee.dob, employee.passportID, employee.passportExpiry, employee.managerID))
        else:
            print("Employee with Employee ID", empID, " not found.")

    def editEmp(self):
        item = self.table.selection()
        if len(item) == 0:
            return

        # Retrieve the values associated with the selected item
        values = self.table.item(item, 'values')

        # Check if values exist and if the item is a tuple
        if values and isinstance(values, tuple):
            # Retrieve the employee ID from the values tuple
            empID = values[1]

            with open("employees.pkl", "rb") as file:
                employees = []
                while True:
                    try:
                        employee = pickle.load(file)
                        if isinstance(employee, Employee) and employee.empID == empID:
                            employees.append(employee)
                    except EOFError:
                        break

            if employees:
                # Open a new window or dialog box for editing employee details
                editWindow = tk.Toplevel()
                editWindow.title("Edit Employee Details")
                editWindow.geometry("300x250")

                tk.Label(editWindow, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
                tk.Label(editWindow, text="Employee ID:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
                tk.Label(editWindow, text="Manager ID:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
                tk.Label(editWindow, text="Department:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
                tk.Label(editWindow, text="Job Title:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
                tk.Label(editWindow, text="Basic Salary:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)

                nameVar = tk.StringVar(value=employees[0].name)
                tk.Entry(editWindow, textvariable=nameVar).grid(row=0, column=1, padx=5, pady=5)
                empID_var = tk.StringVar(value=str(employees[0].empID))
                tk.Entry(editWindow, textvariable=empID_var, state='disabled').grid(row=1, column=1, padx=5, pady=5)
                managerID_var = tk.StringVar(value=str(employees[0].managerID))
                tk.Entry(editWindow, textvariable=managerID_var).grid(row=2, column=1, padx=5, pady=5)
                departmentVar = tk.StringVar(value=employees[0].department)
                tk.Entry(editWindow, textvariable=departmentVar).grid(row=3, column=1, padx=5, pady=5)
                jobTitle_var = tk.StringVar(value=employees[0].jobTitle)
                tk.Entry(editWindow, textvariable=jobTitle_var).grid(row=4, column=1, padx=5, pady=5)
                basicSalary_var = tk.StringVar(value=str(employees[0].basicSalary))
                tk.Entry(editWindow, textvariable=basicSalary_var).grid(row=5, column=1, padx=5, pady=5)

            # Function to save the edited details
            def edited():
                # Update the employee object with the edited details
                employees[0].name = nameVar.get()
                employees[0].managerID = managerID_var.get()
                employees[0].department = departmentVar.get()
                employees[0].jobTitle = jobTitle_var.get()
                employees[0].basicSalary = basicSalary_var.get()

                # Rewrite the entire employees list to the file with the updated employee details
                with open("employees.pkl", "wb") as file:
                    for emp in employees:
                        pickle.dump(emp, file)

                # Update the table with the edited details
                self.table.item(item, values=(
                employees[0].name, employees[0].empID, employees[0].managerID, employees[0].department,
                employees[0].jobTitle, employees[0].basicSalary))

                editWindow.destroy()  # Close the edit window

            # Button to save the edited details
            tk.Button(editWindow, text="Save", command=edited).grid(row=6, column=1, padx=5, pady=10, sticky=tk.E)

    def deleteEmp(self):
        item = self.table.selection()
        if len(item) == 0:
            return
        empID = self.table.item(item)['values'][1]

        with open("employees.pkl", "rb") as file:
            employees = []
            while True:
                try:
                    employee = pickle.load(file)
                    if isinstance(employee, Employee) and employee.empID != empID:
                        employees.append(employee)
                except EOFError:
                    break

        with open("employees.pkl", "wb") as file:
            for employee in employees:
                pickle.dump(employee, file)

        self.table.delete(item)

    def loadEmployees(self):
        try:
            with open('employees.pkl', 'rb') as f:
                while True:
                    employee = pickle.load(f)
                    if isinstance(employee, Employee):
                        self.table.insert('', 'end', values=(
                            employee.name, employee.empID, employee.managerID, employee.department,
                            employee.jobTitle,
                            employee.basicSalary))
        except FileNotFoundError:
            pass
        except EOFError:
            pass

# List to save employee details
allEmployees = {}


def saveEmployeeInfo(employee):
    with open('employees.pkl', 'ab') as f:
        pickle.dump(employee, f)


if __name__ == "__main__":
    # Create Object of the List Employee Form
    displayEmployee = EmployeeList()

