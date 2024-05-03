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
        employee = Employee(name, empID, department, jobTitle, basicSalary, age, dob, passportID, passportExpiry,
                            managerID)
        if empID not in employee:
            employee[empID] = employee
            with open("employee.pkl", "ab") as file:
                pickle.dump(employee, file)
            self.table.insert('', 'end', values=(
            employee.name, employee.empID, employee.department, employee.jobTitle, employee.basicSalary, employee.age, employee.dob, employee.passportID, employee.passportExpiry, employee.managerID))

            self.clearBoxes()
            print("Employee added successfully. Employee ID:", empID)
        else:
            print("Employee with Employee ID", empID, "already exists.")


