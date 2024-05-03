import pickle
import os
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

infoPath = "data"  # The data will be stored here
if not os.path.exists(infoPath):
    os.makedirs(infoPath)

# Functions to save and load the employee information
def saveInfo(employees):
    try:
        with open(os.path.join(infoPath, 'employees.pkl'), 'wb') as dumpf:
            pickle.dump(employees, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadInfo():
    try:
        with open(os.path.join(infoPath, 'employees.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Employee not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load event information
def saveEventInfo(events):
    try:
        with open(os.path.join(infoPath, 'events.pkl'), 'wb') as dumpf:
            pickle.dump(events, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadEventInfo():
    try:
        with open(os.path.join(infoPath, 'events.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Event not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load supplier information
def saveSupplierInfo(supplier):
    try:
        with open(os.path.join(infoPath, 'suppliers.pkl'), 'wb') as dumpf:
            pickle.dump(supplier, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadSupplierInfo():
    try:
        with open(os.path.join(infoPath, 'suppliers.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Supplier not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load guest information
def saveGuestInfo(guests):
    try:
        with open(os.path.join(infoPath, 'guests.pkl'), 'wb') as dumpf:
            pickle.dump(guests, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadGuestInfo():
    try:
        with open(os.path.join(infoPath, 'guests.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Guest not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load client information
def saveClientInfo(clients):
    try:
        with open(os.path.join(infoPath, 'clients.pkl'), 'wb') as dumpf:
            pickle.dump(clients, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadClientInfo():
    try:
        with open(os.path.join(infoPath, 'clients.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Client not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load venue information
def saveVenueInfo(venues):
    try:
        with open(os.path.join(infoPath, 'venues.pkl'), 'wb') as dumpf:
            pickle.dump(venues, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadVenueInfo():
    try:
        with open(os.path.join(infoPath, 'venues.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Venue not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


class Employee:
    """Class to represent the employee information"""

    def __init__(self, name, empID, department, jobTitle, basicSalary, age, dateOfBirth, passportID, passportExpiry,
                 managerID):
        self.name = name
        self.empID = empID
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.age = age
        self.dateOfBirth = dateOfBirth
        self.passportID = passportID
        self.passportExpiry = passportExpiry
        self.managerID = managerID

    def getInfo(self):
        # Return information about the employee
        return (f"Name: {self.name}\nEmployee ID: {self.empID}\nDepartment: {self.department}\nJob Title: {self.jobTitle}\nBasic Salary: {self.basicSalary}\nAge: {self.age}"
                 f"\nDate of Birth: {self.dateOfBirth}\nPassport ID: {self.passportID}\nPassport Expiry Date: {self.passportExpiry}\nManager: {self.managerID}")


class Client:
    """Class to represent the client information"""

    def __init__(self, clientName, clientID, clientAddress, email, phoneNum, clientBudget):
        self.clientName = clientName
        self.clientID = clientID
        self.clientAddress = clientAddress
        self.email = email
        self.phoneNum = phoneNum
        self.clientBudget = clientBudget

    def updateBudget(self, newBudget):
        self.clientBudget = newBudget

    def displayInfo(self):
        # Return details of the client
        return f"Client Name: {self.clientName}\nClient ID: {self.clientID}\nClient Address: {self.clientAddress}\nEmail: {self.email}\n Phone Number: {self.phoneNum}\nBudget: {self.clientBudget}"


class Guest:
    """Class to represent the guest information"""

    def __init__(self, guestName, guestID, guestAddress, email, phoneNum):
        self.guestName = guestName
        self.guestID = guestID
        self.guestAddress = guestAddress
        self.email = email
        self.phoneNum = phoneNum

    def getInfo(self):
        # Return details of the guest
        return f"Guest Name: {self.guestName}\n Guest ID: {self.guestID}\n Guest Address: {self.guestAddress}\n Email: {self.email}\n Phone Number: {self.phoneNum}"


class Supplier:
    """Class to represent the supplier information"""

    def __init__(self, supplierName, supplierID, supplierAddress, email, phoneNum, supplierCompany, minGuests,
                 maxGuests):
        self.supplierName = supplierName
        self.supplierID = supplierID
        self.supplierAddress = supplierAddress
        self.email = email
        self.phoneNum = phoneNum
        self.supplierCompany = supplierCompany
        self.minGuests = minGuests
        self.maxGuests = maxGuests

    def __str__(self):
        return f"Supplier Name: {self.supplierName}\nSupplier ID: {self.supplierID}\n Supplier Address: {self.supplierAddress}\n Email: {self.email}\n Phone Number: {self.phoneNum}\n Supplier Company: {self.supplierCompany}\n Minimum Guests: {self.minGuests}\n Maximum Guests: {self.maxGuests}"


class Venue:
    """Class to represent the venue information"""

    def __init__(self, venueName, venueID, venueAddress, contactNum, minGuests, maxGuests):
        self.venueName = venueName
        self.venueID = venueID
        self.venueAddress = venueAddress
        self.contactNum = contactNum
        self.minGuests = minGuests
        self.maxGuests = maxGuests

    def __str__(self):
        return f"Venue Name: {self.venueName}\n Venue ID: {self.venueID}\n Address: {self.venueAddress}\n Contact Number: {self.contactNum}\n Min Guests: {self.minGuests}\n Max Guests: {self.maxGuests}"


class Event:
    """Class to represent the event information"""

    def __init__(self, eventName, eventID, eventType, eventTheme, date, time, duration, venueAddress, clientID,
                 invoice):
        self.eventName = eventName
        self.eventID = eventID
        self.eventType = eventType
        self.eventTheme = eventTheme
        self.date = date
        self.time = time
        self.duration = duration
        self.venueAddress = venueAddress
        self.clientID = clientID
        self.guestList = []
        self.suppliers = []
        self.invoice = invoice

    def addSupplier(self, supplierName, supplierID, supplierAddress, email, phoneNum, supplierCompany, minGuests, maxGuests):
        # Add supplier to event
        newSupplier = Supplier(supplierName, supplierID, supplierAddress, email, phoneNum, supplierCompany, minGuests, maxGuests)
        self.suppliers.append(newSupplier)
        return newSupplier

    def removeSupplier(self, supplierID):
        # Remove supplier from event
        self.suppliers = [supplier for supplier in self.suppliers if supplier.supplierID != supplierID]

    def addGuest(self, guest):
        # Add guest to event
        self.guestList.append(guest)

    def removeGuest(self, guestID):
        # Remove guest from event
        self.guestList = [guest for guest in self.guestList if guest.guestID != guestID]

    def getInfo(self):
        # details of the event
        details = f"Event Name: {self.eventName}\n Event ID: {self.eventID}\n Type: {self.eventType}\n Date: {self.date}\n Time: {self.time}\n Duration: {self.duration}\n Venue Address: {self.venueAddress}\n Client ID: {self.clientID}\n Invoice: {self.invoice}"
        guests_info = '\n'.join([guest.getInfo() for guest in self.guestList])
        suppliers_info = '\n'.join([str(supplier) for supplier in self.suppliers])
        return f"{details}\nGuests:\n{guests_info}\nSuppliers:\n{suppliers_info}"


class ManagementSystem:
    """Class to represent the management system for the company and all the information"""
    def __init__(self, root):
        self.root = root  # Storing root window
        self.root.title("Welcome to the Management System")  # Setting the title of the main window
        # Loading information from pickle files
        self.employees = loadInfo()
        self.events = loadEventInfo()
        self.suppliers = loadSupplierInfo()
        self.guests = loadGuestInfo()
        self.clients = loadClientInfo()
        self.venues = loadVenueInfo()

        # Label widget
        ttk.Label(root, text="Welcome!").grid(row=0, column=0, columnspan=2)
        # Label widget that prompts the user to select a system to enter
        ttk.Label(root, text="Please select a system:").grid(row=1, column=0, sticky='w')
        self.systemVar = tk.StringVar()
        # Display options in the drop-down menu
        systemOpt = ['Employee', 'Client', 'Guest', 'Supplier', 'Venue', 'Event']
        # OptionMenu widget
        self.systemMenu = tk.OptionMenu(root, self.systemVar, *systemOpt)
        # Placing it in GUI
        self.systemMenu.grid(row=1, column=1)
        # Creating a button to confirm user selection
        ttk.Button(root, text="Enter", command=self.enterSystem).grid(row=2, column=0, columnspan=2)

        # Initializing ID counters
        self.empID_counter = self.idCounter(self.employees, "Employee ID", 2)
        self.supplierID_counter = self.idCounter(self.suppliers, "Supplier ID", 2)
        self.eventID_counter = self.idCounter(self.events, "Event ID", 2)
        self.guestID_counter = self.idCounter(self.guests, "Guest ID", 1)
        self.clientID_counter = self.idCounter(self.clients, "Client ID", 1)
        self.venueID_counter = self.idCounter(self.venues, "Venue ID", 1)

    def idCounter(self, items, idAttribute, sliceStart):
        if items:
            return max(int(getattr(item, idAttribute)[sliceStart:]) for item in items.values()) + 1
        return 1

    # Navigate to selected system
    def enterSystem(self):
        # Retrieve user's selection and opens the system management
        # Retrieving the value selected
        selectedSystem = self.systemVar.get()
        if selectedSystem == 'Employee':
            self.openEmpSystem()
        elif selectedSystem == "Event":
            self.openEventSystem()
        elif selectedSystem == "Supplier":
            self.openSupplierSystem()
        elif selectedSystem == "Guest":
            self.openGuestSystem()
        elif selectedSystem == "Client":
            self.openClientSystem()
        elif selectedSystem == "Venue":
            self.openVenueSystem()

    def openEmpSystem(self):
        # Open Employee management system if user chooses 'Employee' from the menu
        # Reload employee information from the storage file
        self.employees = loadInfo()
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Department", "Job Title", "Salary"), show="headings")
        # Defining headings for each column
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Department", text="Department")
        self.tree.heading("Job Title", text="Job Title")
        self.tree.heading("Salary", text="Salary")
        self.tree.grid(row=3, column=0, columnspan=2, sticky='nsew')

        # Button to add employee
        ttk.Button(self.root, text="Add Employee", command=self.openAddEmployee).grid(row=4, column=0)
        # Button to edit on existing employee information
        ttk.Button(self.root, text="Modify Employee", command=self.modifyEmployee).grid(row=4, column=1)
        # Button to remove employee
        ttk.Button(self.root, text="Remove Employee", command=self.removeEmployee).grid(row=5, column=0)
        # Button to find employee by ID
        ttk.Button(self.root, text="Find by ID", command=self.findEmployee).grid(row=5, column=1)

        # Refreshing the table
        self.refreshTable()

    def refreshTable(self):
        # Clearing all entries
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Looping through the employees dictionary and inserting each employee's data into the Treeview
        for empID, emp in self.employees.items():
            empID = getattr(emp, 'Employee ID', 'No ID')
            name = getattr(emp, 'Name', 'No Name')
            department = getattr(emp, 'Department', 'No Department')
            jobTitle = getattr(emp, 'Job Title', 'No Job Title')
            basicSalary = getattr(emp, 'Salary', 'No Salary')

            # Adding the employee's information into Treeview
            self.tree.insert("", "end", values=(empID, name, department, jobTitle, basicSalary))


    # Open a new window to add new employee
    def openAddEmployee(self):
        self.addWindow = tk.Toplevel(self.root)
        self.addWindow.title("Add a New Employee")

        # Defining labels
        lbls = ['Name', 'Phone Number:', 'Department:', 'Job Title:', 'Salary:', 'Employee ID:', 'Age']
        self.entries = {}
        departments = ["Marketing", "Operations", "Human Resources", "Finance", "Logistics", "Sales", "Event Planning"]
        jobTitles = ["Event Coordinator", "Event Manager", "Marketing Specialist", "Operations Manager", "HR Manager",
                      "Registration Coordinator", "Admin"]

        # Creating label and appropriate entry or dropdown for each field
        for i, label in enumerate(lbls):
            ttk.Label(self.addWindow, text=label).grid(row=i, column=0)

            if label == 'Department:':
                departmentVar = tk.StringVar()
                departmentMenu = ttk.OptionMenu(self.addWindow, departmentVar, *departments)
                departmentMenu.grid(row=i, column=1)
                self.entries[label] = departmentVar
            elif label == 'Job Title:':
                jobTitle_var = tk.StringVar()
                jobTitle_menu = ttk.OptionMenu(self.addWindow, jobTitle_var, *jobTitles)
                jobTitle_menu.grid(row=i, column=1)
                self.entries[label] = jobTitle_var
            else:
                entry = ttk.Entry(self.addWindow)
                entry.grid(row=i, column=1)
                self.entries[label] = entry

        # Save new employee info
        ttk.Button(self.addWindow, text="Save Employee", command=self.addEmployee).grid(row=len(lbls), column=1)


    # Collect data from the form and creates a new Employee and refreshes the employee list
    def addEmployee(self):
        try:
            # Attempting to retrieve data from entries with validation
            name = self.entries['Name:'].get()
            phoneNum = self.entries['Phone Number:'].get()
            department = self.entries['Department:'].get()
            jobTitle = self.entries['Job Title:'].get()
            basicSalary = self.entries['Salary:'].get()

            # Checking for empty fields
            if not (name and phoneNum and department and jobTitle and basicSalary):
                tk.messagebox.showerror("Error", "Fill in all the fields")
                return
            # Validating salary
            salary = float(basicSalary)

            # Assigning unique employee ID and incrementing counter
            empID = f"EP{self.empID_counter}"
            self.empID_counter += 1

            # Create new Employee
            emp = Employee(name, phoneNum, empID, department, jobTitle, basicSalary)
            self.employees[emp.empID] = emp
            saveInfo(self.employees)

            # Refreshing and closing the form
            self.refreshTable()
            self.addWindow.destroy()

        except ValueError:
            # Handling the error if salary is not a valid value
            tk.messagebox.showerror("Error", "Salary must be in numbers only (you may include decimal points).")


    # Modification for an existing employee's info
    def modifyEmployee(self):
        # Asks user to enter ID of the employee they want to modify
        empID = simpledialog.askstring("Modify on an Existing Employee", "Enter Employee ID")

        # Checking if the employee ID exists
        if empID in self.employees:
            emp = self.employees[empID]
            # Ask user for new department
            newDepartment = simpledialog.askstring("Modify on an Existing Employee",
                                              f"Current Department: {emp.department}. New Department (to keep current, leave empty):")
            if newDepartment:
                emp.department = newDepartment

            # Asking for new job title
            newJobTitle = simpledialog.askstring("Modify on an Existing Employee",
                                             f"Current Job Title: {emp.jobTitle}. New job title (to keep current, leave empty):")
            if newJobTitle:
                emp.jobTitle = newJobTitle

            # Asking for new salary and update, handling conversion errors
            newSalary = simpledialog.askstring("Modify on an Existing Employee",
                                                f"Current Salary: {emp.salary}. New salary (to keep current, leave empty):")
            if newSalary:
                try:
                    emp.salary = float(newSalary)
                except ValueError:
                    messagebox.showerror("Error", "Salary must be a number.")
                    return

                    # Saving modifications
            saveInfo(self.employees)
            self.refreshTable()
        else:
            messagebox.showerror("Error", "Employee not found")


    # Removes an employee from the system after user inputs employee ID
    def removeEmployee(self):
        # Asking the user to enter the ID of employee
        empID = simpledialog.askstring("Remove an Employee From the System", "Enter Employee ID")
        # Check if employee ID exists
        if empID in self.employees:
            # deleting the employee entry using their ID if found
            del self.employees[empID]
            # Saving the updated data
            saveInfo(self.employees)
            self.refreshTable()
        else:
            messagebox.showerror("Error", "Employee not found")


    # Search for details of employee by ID
    def findEmployee(self):
        empID = simpledialog.askstring("Find Employee", "Enter Employee ID")
        try:
            # Loading the current employees
            self.employees = loadInfo()

            # Check if employee ID exists in the loaded info
            if empID in self.employees:
                # Retrieving the employee based on ID
                emp = self.employees[empID]
                information = emp.getInfo()
                # Displaying the employee info
                messagebox.showinfo("Employee Information", information)
            else:
                messagebox.showerror("Error", "Employee not found")
        except Exception as e:
            messagebox.showerror("Error", f"Error while loading the information: {e}")


    # Initialize and display event management system
    def openEventSystem(self):
        # Loading event information
        self.events = loadEventInfo()

        # Display event details in tabular format
        self.eventTree = ttk.Treeview(self.root, columns=("Event Name", "Event ID", "Event Type", "Date", "Time", "Duration"),
                                       show="headings")
        self.eventTree.heading("Event Name", text="Event Name")
        self.eventTree.heading("Event ID", text="Event ID")
        self.eventTree.heading("Event Type", text="Event Type")
        self.eventTree.heading("Date", text="Date")
        self.eventTree.heading("Time", text="Time")
        self.eventTree.heading("Duration", text="Duration")
        self.eventTree.grid(row=3, column=0, columnspan=2, sticky='nsew')

        # Buttons to add, modify, remove, and find events
        ttk.Button(self.root, text="Add Event", command=self.openAddEventForm).grid(row=4, column=0)
        ttk.Button(self.root, text="Modify Event", command=self.modifyEvent).grid(row=4, column=1)
        ttk.Button(self.root, text="Remove Event", command=self.removeEvent).grid(row=5, column=0)
        ttk.Button(self.root, text="Find Event by ID", command=self.findEvent).grid(row=5, column=1)

        # Refresh event info
        self.refreshEventTable()


    # Clear and update event table
    def refreshEventTable(self):
        # Removing all existing entries
        for i in self.eventTree.get_children():
            self.eventTree.delete(i)
        # Inserting updated info
        for eventID, event in self.events.items():
            self.eventTree.insert("", "end", values=(
                event.eventName, event.eventID, event.eventType, event.date, event.time, event.duration))

    # New window for adding a new event
    def openAddEventForm(self):
        self.addEventWindow = tk.Toplevel(self.root)
        self.addEventWindow.title("Add New Event")

        # Labels for event properties
        lbls = ['Type:', 'Date:', 'Time:', 'Duration:']
        self.eventEntries = {}
        eventTypes = ["Wedding", "Birthday", "Themed Parties", "Graduation" ,"Conference", "Seminar", "Workshop"]

        # Iterating over the labels to create and place corresponding input widgets
        for i, label in enumerate(lbls):
            ttk.Label(self.addEventWindow, text=label).grid(row=i, column=0)
            if label == 'Type:':
                typeVar = tk.StringVar()
                ttk.OptionMenu(self.addEventWindow, typeVar, eventTypes[0], *eventTypes).grid(row=i, column=1)
                self.eventEntries[label] = typeVar
            else:
                entry = ttk.Entry(self.addEventWindow)
                entry.grid(row=i, column=1)
                self.eventEntries[label] = entry

        ttk.Button(self.addEventWindow, text="Save Event", command=self.addEvent).grid(row=len(lbls), column=1)


    # Collects information from the form and creates a new Event and refreshes the event table
    def addEvent(self):
        try:
            eventName = self.eventEntries['Name:'].get().strip()
            eventType = self.eventEntries['Type:'].get().strip()
            date = self.eventEntries['Date:'].get().strip()
            time = self.eventEntries['Time:'].get().strip()
            duration = self.eventEntries['Duration:'].get().strip()

            # Validating all fields are filled
            if not (eventType and date and time and duration):
                raise ValueError("All fields must be filled.")

            eventID = f"EV{self.eventID_counter}"
            self.eventID_counter += 1

            # Creating and saving the new event
            event = Event(eventName, eventID, eventType, date, time, duration)
            self.events[event.eventID] = event
            saveEventInfo(self.events)
            self.refreshEventTable()
            self.addEventWindow.destroy()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Unexpected error: {str(e)}")


    # Allows the user to modify an existing event
    def modifyEvent(self):
        eventID = simpledialog.askstring("Modify on an Event", "Enter Event ID")

        # Check if the event ID exists
        if eventID in self.events:
            event = self.events[eventID]
            # Asking for new event details
            newType = simpledialog.askstring("Modify on an Event",  f"Current Event Type: {event.eventType}. New Event type (to keep current, leave empty):")
            if newType:
                event.eventType = newType

            newDate = simpledialog.askstring("Modify on an Event", f"Current Event Date: {event.date}. New Event date (to keep current, leave empty):")
            if newDate:
                event.date = newDate

            newTime = simpledialog.askstring("Modify on an Event", f"Current Event Time: {event.time}. New Event time (to keep current, leave empty):")
            if newTime:
                event.time = newTime

            newDuration = simpledialog.askstring("Modify on an Event",  f"Current Event Duration: {event.duration}. New Event duration (to keep current, leave empty):")
            if newDuration:
                event.duration = newDuration

            # Saving the updated event data back to the storage
            saveEventInfo(self.events)
            self.refreshEventTable()

        else:
            messagebox.showerror("Error", "Event not found")


    #  Remove event from the system after user inputs event ID
    def removeEvent(self):
        eventID = simpledialog.askstring("Remove Event", "Enter Event ID")
        # Checking if the entered event ID exists
        if eventID in self.events:
            # If the event ID exists, delete the event from the dictionary
            del self.events[eventID]
            # Saving the updated events details
            saveEventInfo(self.events)
            self.refreshEventTable()
        else:
            messagebox.showerror("Error", "Event not found")


    # Prompts user to enter event ID and displays the event details
    def findEvent(self):
        eventID = simpledialog.askstring("Find Event", "Enter Event ID")
        try:
            # Loading current event info
            self.events = loadEventInfo()
            # Checking if event ID exists
            if eventID in self.events:
                event = self.events[eventID]
                information = event.getInformation()
                # Display details
                messagebox.showinfo("Event Information", information)
            else:
                messagebox.showerror("Error", "Event not found")
        except Exception as e:
            messagebox.showerror("Error", f"Error while loading the information: {e}")


    # Initialize and display supplier management
    def openSupplierSystem(self):
        # Loading supplier info
        self.suppliers = loadSupplierInfo()

        # Setting up a Treeview widget to display supplier info
        self.supplierTree = ttk.Treeview(self.root, columns=("Supplier Name", "Supplier ID", "Supplier Company"), show="headings")
        self.supplierTree.heading("Supplier Name", text="Supplier Name")
        self.supplierTree.heading("Supplier ID", text="Supplier ID")
        self.supplierTree.heading("Supplier Company", text="Supplier Company")
        self.supplierTree.grid(row=3, column=0, columnspan=2, sticky='nsew')

        # Buttons for functions
        ttk.Button(self.root, text="Add Supplier", command=self.openAddSupplierForm).grid(row=4, column=0)
        ttk.Button(self.root, text="Modify Supplier", command=self.modifySupplier).grid(row=4, column=1)
        ttk.Button(self.root, text="Remove Supplier", command=self.removeSupplier).grid(row=5, column=0)
        ttk.Button(self.root, text="Find Supplier by ID", command=self.findSupplier).grid(row=5, column=1)

        self.refreshSupplierTable()


    # Clears and refreshes supplier table
    def refreshSupplierTable(self):
        for i in self.supplierTree.get_children():
            self.supplierTree.delete(i)
        for supplierID, supplier in self.suppliers.items():
            self.supplierTree.insert("", "end", values=(
                supplier.supplierName, supplier.supplierID, supplier.SupplierCompany))


    # Open new window to add new supplier
    def openAddSupplierForm(self):
        # Creating a new window for adding a supplier
        self.addSupplierWindow = tk.Toplevel(self.root)
        self.addSupplierWindow.title("Add a New Supplier")

        lbls = ['Name:', 'Supplier Company:']
        supplierCompany = ['Catering', 'Sound System', 'Decoration', 'Photography', 'Security']

        self.supplierEntries = {}
        for i, label in enumerate(lbls):
            ttk.Label(self.addSupplierWindow, text=label).grid(row=i, column=0)
            if label == 'Service Type:':
                self.supplierCompany_var = tk.StringVar(self.addSupplierWindow)
                self.supplierCompany_var.set('Select Service Type')
                entry = tk.OptionMenu(self.addSupplierWindow, self.supplierCompany_var, *supplierCompany)
            else:
                entry = ttk.Entry(self.addSupplierWindow)

            entry.grid(row=i, column=1)
            self.supplierEntries[label] = entry

        ttk.Button(self.addSupplierWindow, text="Save Supplier", command=self.addSupplier).grid(row=len(lbls), column=1)


    # Collects data from the form and creates a new Supplier object and refreshes the supplier table.
    def addSupplier(self):
        try:
            supplierName = self.supplierEntries['Name:'].get().strip()
            supplierCompany = self.supplierCompany_var.get().strip()

            # Check if fields are empty
            if not supplierName or not supplierCompany:
                raise ValueError("All fields must be filled in.")

            # Validating service type
            if supplierCompany == 'Select Service Company':
                raise ValueError("Select a valid service type.")

            # Generate unique supplier ID and creating a new Supplier
            supplierID = f"SP{self.supplierID_counter}"
            self.supplierID_counter += 1
            supplier = Supplier(supplierID, supplierName, supplierCompany)

            self.suppliers[supplier.supplierID] = supplier
            saveSupplierInfo(self.suppliers)
            self.refreshSupplierTable()
            self.addSupplierWindow.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")


    # Modify on a selected supplier
    def modifySupplier(self):
        # Asking for the ID
        supplierID = simpledialog.askstring("Modify on a Supplier", "Enter Supplier ID")

        # Checking if the supplier ID exists
        if supplierID in self.suppliers:
            supplier = self.suppliers[supplierID]

            newName = simpledialog.askstring("Modify on a Supplier", f"Current Name: {supplier.supplierName}. Enter new supplier name (to keep current, leave empty):")
            if newName:
                supplier.name = newName
            newsupplierCompany = simpledialog.askstring("Modify on a Supplier", f"Current Service Type: {supplier.supplierCompany}. Enter new supplier company (to keep current, leave empty):")
            if newsupplierCompany:
                supplier.supplierCompany = newsupplierCompany
            # Saving updated supplier info and refreshing
            saveSupplierInfo(self.suppliers)
            self.refreshSupplierTable()
        else:
            messagebox.showerror("Error", "Supplier not found")


    # Remove supplier from the system by ID
    def removeSupplier(self):
        supplierID = simpledialog.askstring("Remove Supplier", "Enter Supplier ID")
        # Checking if supplier ID exists
        if supplierID in self.suppliers:
            del self.suppliers[supplierID]
            saveSupplierInfo(self.suppliers)
            self.refreshSupplierTable()
        else:
            messagebox.showerror("Error", "Supplier not found")

    # Find and display details of a supplier by ID
    def findSupplier(self):
        supplierID = simpledialog.askstring("Find Supplier", "Enter Supplier ID")
        try:
            self.suppliers = loadSupplierInfo()
            if supplierID in self.suppliers:
                supplier = self.suppliers[supplierID]
                details = str(supplier)
                messagebox.showinfo("Supplier Details", details)
            else:
                messagebox.showerror("Error", "Supplier not found")
        except Exception as e:
            messagebox.showerror("Error", f"Error while loading the information: {e}")



    # Initializes and displays the guest management system
    def openGuestSystem(self):
        self.guests = loadGuestInfo()
        # Setting up Treeview widget to display guest details
        self.guestTree = ttk.Treeview(self.root, columns=("Guest ID", "Name", "Phone Number"),
                                       show="headings")
        self.guestTree.heading("Guest ID", text="Guest ID")
        self.guestTree.heading("Name", text="Name")
        self.guestTree.heading("Phone Number", text="Phone Number")
        self.guestTree.grid(row=3, column=0, columnspan=2, sticky='nsew')

        # Buttons for adding, modifying, removing, and finding guests
        ttk.Button(self.root, text="Add Guest", command=self.openAddGuestForm).grid(row=4, column=0)
        ttk.Button(self.root, text="Modify Guest", command=self.modifyGuest).grid(row=4, column=1)
        ttk.Button(self.root, text="Remove Guest", command=self.removeGuest).grid(row=5, column=0)
        ttk.Button(self.root, text="Find Guest by ID", command=self.findGuest).grid(row=5, column=1)

        self.refreshGuestTable()


    # A function that clears and updates the guest table with the latest guest data
    def refreshGuestTable(self):
        for i in self.guestTree.get_children():
            self.guestTree.delete(i)
        for guestID, guest in self.guests.items():
            self.guestTree.insert("", "end",
                                   values=(guest.guestID, guest.guestName(), guest._phoneNum))

    # Opens a new window for adding a new guest
    def openAddGuestForm(self):
        self.addGuestWindow = tk.Toplevel(self.root)
        self.addGuestWindow.title("Add New Guest")

        labels = ['Name:', 'Phone Number:']
        self.guestEntries = {}

        # Adding entry fields for guest information
        for i, label in enumerate(labels):
            ttk.Label(self.addGuestWindow, text=label).grid(row=i, column=0)

        ttk.Button(self.addGuestWindow, text="Save Guest", command=self.addGuest).grid(row=len(labels), column=1)


    # Collects info from the form and creates a new Guest object and refreshes
    def addGuest(self):
        try:
            name = self.guestEntries['First Name:'].get().strip()
            phoneNum = self.guestEntries['Phone Number:'].get().strip()
            # Validating all fields are filled
            if not (name and phoneNum):
                raise ValueError("All fields must be filled in.")
            guestID = f"G{self.guestID_counter}"
            self.guestID_counter += 1

            # Saving the new guest
            guest = Guest(name, phoneNum)
            self.guests[guest.guestID] = guest
            saveGuestInfo(self.guests)
            self.refreshGuestTable()
            self.addGuestWindow.destroy()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Unexpected error: {str(e)}")


    # Modifies guest information
    def modifyGuest(self):
        guestID = simpledialog.askstring("Modify on the Guest", "Enter the ID of the guest to modify")
        if guestID in self.guests:
            guest = self.guests[guestID]

            newName = simpledialog.askstring("Modify on the Guest", f"Current Guest Name: {guest.name}. New guest name (to keep current, leave empty):")
            if newName:
                guest.guestName = newName

            new_phoneNum = simpledialog.askstring("Modify on the Guest", f"Current Phone Number: {guest._phoneNum}. New phone number (to keep current, leave empty):")
            if new_phoneNum:
                guest._phoneNum = new_phoneNum

            # Saving changes
            saveGuestInfo(self.guests)
            self.refreshGuestTable()
        else:
            messagebox.showerror("Error", "Guest not found")


    # Removes a guest
    def removeGuest(self):
        guestID = simpledialog.askstring("Remove Guest", "Enter Guest ID")
        if guestID in self.guests:
            del self.guests[guestID]
            saveGuestInfo(self.guests)
            self.refreshGuestTable()
        else:
            messagebox.showerror("Error", "Guest not found")


    # Finds and displays guest details based on user input
    def findGuest(self):
        guestID = simpledialog.askstring("Find Guest", "Enter Guest ID")
        if guestID in self.guests:
            guest = self.guests[guestID]
            details = guest.getInfo()
            messagebox.showinfo("Guest Details", details)
        else:
            messagebox.showerror("Error", "Guest not found")

    # Opens the client management system interface
    def openClientSystem(self):
        # Loading client data
        self.clients = loadClientInfo()
        # Initializing client treeview
        self.clientTree = ttk.Treeview(self.root, columns=("Client ID", "Name", "Phone", "Budget"),
                                        show="headings")
        self.clientTree.heading("Client ID", text="Client ID")
        self.clientTree.heading("Name", text="Name")
        self.clientTree.heading("Phone", text="Phone")
        self.clientTree.heading("Budget", text="Budget")
        self.clientTree.grid(row=3, column=0, columnspan=2, sticky='nsew')

        # Buttons for client management
        ttk.Button(self.root, text="Add Client", command=self.openAddClientForm).grid(row=4, column=0)
        ttk.Button(self.root, text="Modify Client", command=self.modifyClient).grid(row=4, column=1)
        ttk.Button(self.root, text="Remove Client", command=self.removeClient).grid(row=5, column=0)
        ttk.Button(self.root, text="Find Client by ID", command=self.findClient).grid(row=5, column=1)

        self.refreshClientTable()


    # Refresh client table
    def refreshClientTable(self):
        # Clearing existing entries
        for i in self.clientTree.get_children():
            self.clientTree.delete(i)
        # Add updated client info into treeview
        for clientID, client in self.clients.items():
            self.clientTree.insert("", "end", values=(
            client.clientID, client.clientName, client._phoneNum, client.budget))

    # Opens a new window for adding a new client
    def openAddClientForm(self):
        # New window for adding a client
        self.addClientWindow = tk.Toplevel(self.root)
        self.addClientWindow.title("Add New Client")

        # Defining labels for client properties
        labels = ['Name:', 'Phone Number:', 'Budget:']
        self.clientEntries = {}
        ttk.Button(self.addClientWindow, text="Save Client", command=self.addClient).grid(row=len(labels), column=1)


    # Collects data from the form and creates a new Client object and refreshes the client table
    def addClient(self):
        # Extracting data from the input fields
        name = self.clientEntries['Name:'].get()
        phoneNum = self.clientEntries['Phone Number:'].get()
        budget = self.clientEntries['Budget:'].get()

        # Validating and converting budget and number of events
        try:
            budget = float(budget) if budget.strip() else 0
        except ValueError:
            messagebox.showerror("Invalid Input",
                                 "Make sure budget is a number and number of events is an integer.")
            return

        # Handling empty inputs
        if not (name and phoneNum and budget):
            messagebox.showerror("Invalid Input", "Fill all fields.")
            return

        # Generating client ID
        clientID = f"C{self.clientID_counter}"
        self.clientID_counter += 1

        # Creating and saving new client
        client = Client(name, phoneNum, clientID, budget)
        self.clients[client.clientID] = client
        saveClientInfo(self.clients)
        self.refreshClientTable()
        self.addClientWindow.destroy()


    # Modification of an existing client's budget
    def modifyClient(self):
        clientID = simpledialog.askstring("Modify on a Client", "Enter ID")
        # Checking if the client exists in the client dictionary
        if clientID in self.clients:
            client = self.clients[clientID]

            newbudget = simpledialog.askstring("Modify Client",  f"Current Budget: {client.budget}. New budget (to keep current, leave empty):")
            if newbudget:
                try:
                    # Convert input to float and update budget
                    client.updateBudget(float(newbudget))
                except ValueError:
                    messagebox.showerror("Error", "Budget must be a number.")
                    return

            # Save client info
            saveClientInfo(self.clients)
            self.refreshClientTable()
        else:
            messagebox.showerror("Error", "Client not found")


    # Removes client from system
    def removeClient(self):
        clientID = simpledialog.askstring("Remove Client", "Enter ID")
        # Checking if client exists
        if clientID in self.clients:
            # Removing client
            del self.clients[clientID]
            # Saving the updated client
            saveClientInfo(self.clients)
            self.refreshClientTable()
        else:
            messagebox.showerror("Error", "Client not found")


    # Searches for a client by ID and displays information
    def findClient(self):
        clientID = simpledialog.askstring("Find Client", "Enter ID")
        # Checking if the client exists in the database
        if clientID in self.clients:
            client = self.clients[clientID]
            details = client.displayInfo()
            messagebox.showinfo("Client Details", details)
        else:
            messagebox.showerror("Error", "Client not found")

    # Opens venue management system
    def openVenueSystem(self):
        self.venues = loadVenueInfo()
        self.venueTree = ttk.Treeview(self.root, columns=("Venue ID", "Address", "Min Guests", "Max Guests"),
                                      show="headings")
        self.venueTree.heading("Venue ID", text="Venue ID")
        self.venueTree.heading("Address", text="Address")
        self.venueTree.heading("Min Guests", text="Min Guests")
        self.venueTree.heading("Max Guests", text="Max Guests")
        self.venueTree.grid(row=3, column=0, columnspan=2, sticky='nsew')

        ttk.Button(self.root, text="Add Venue", command=self.openAddVenueForm).grid(row=4, column=0)
        ttk.Button(self.root, text="Modify Venue", command=self.modifyVenue).grid(row=4, column=1)
        ttk.Button(self.root, text="Remove Venue", command=self.removeVenue).grid(row=5, column=0)
        ttk.Button(self.root, text="Find Venue by ID", command=self.findVenue).grid(row=5, column=1)

        self.refreshVenueTable()

    # Refreshes venue table
    def refreshVenueTable(self):
        for i in self.venueTree.get_children():
            self.venueTree.delete(i)
        for venueID, venue in self.venues.items():
            self.venueTree.insert("", "end",
                                  values=(venue.venueID, venue.venueAddress, venue.minGuests, venue.maxGuests))

    # Opens new window for adding a new venue.
    def openAddVenueForm(self):
        self.addVenueWindow = tk.Toplevel(self.root)  # Fixed variable name
        self.addVenueWindow.title("Add New Venue")

        labels = ['Address:', 'Min Guests:', 'Max Guests:']
        self.venueEntries = {}

        for i, label in enumerate(labels):
            ttk.Label(self.addVenueWindow, text=label).grid(row=i, column=0)  # Fixed variable name
            entry = ttk.Entry(self.addVenueWindow)
            entry.grid(row=i, column=1)
            self.venueEntries[label] = entry

        ttk.Button(self.addVenueWindow, text="Save Venue", command=self.addVenue).grid(row=len(labels), column=1)

    # Collects data from the form and creates a new Venue object and refreshes the venue table
    def addVenue(self):
        venueAddress = self.venueEntries['Address:'].get()
        minGuests = self.venueEntries['Min Guests:'].get()
        maxGuests = self.venueEntries['Max Guests:'].get()
        try:
            minGuests = int(minGuests)
            maxGuests = int(maxGuests)
            if not venueAddress:
                raise ValueError("Address cannot be empty.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        venueID = f"V{self.venueID_counter}"
        self.venueID_counter += 1

        venue = Venue(venueID, venueAddress, minGuests, maxGuests)
        self.venues[venue.venueID] = venue
        saveVenueInfo(self.venues)
        self.refreshVenueTable()
        self.addVenueWindow.destroy()

    # Modifies venue information based on user input
    def modifyVenue(self):
        venueID = simpledialog.askstring("Modify Venue", "Enter the ID of the venue to modify")
        if venueID in self.venues:
            venue = self.venues[venueID]

            newAddress = simpledialog.askstring("Modify Venue",
                                                f"Current Address: {venue.venueAddress}. New address (to keep current, leave empty):")
            if newAddress:
                venue.venueAddress = newAddress  # Fixed attribute name

            new_minGuests = simpledialog.askstring("Modify Venue",
                                                   f"Current Min Guests: {venue.minGuests}. New minimum guests number(to keep current, leave empty):")
            if new_minGuests:
                try:
                    venue.minGuests = int(new_minGuests)
                except ValueError:
                    messagebox.showerror("Error", "Minimum guests must be a number.")
                    return

            new_maxGuests = simpledialog.askstring("Modify Venue",
                                                   f"Current Max Guests: {venue.maxGuests}. New maximum guests number (to keep current, leave empty):")
            if new_maxGuests:
                try:
                    venue.maxGuests = int(new_maxGuests)
                except ValueError:
                    messagebox.showerror("Error", "Maximum guests must be a valid number.")
                    return

            saveVenueInfo(self.venues)
            self.refreshVenueTable()
        else:
            messagebox.showerror("Error", "Venue not found")

    # Removes venue from the system
    def removeVenue(self):
        venueID = simpledialog.askstring("Remove Venue", "Enter ID")
        if venueID in self.venues:
            del self.venues[venueID]
            saveVenueInfo(self.venues)
            self.refreshVenueTable()
        else:
            messagebox.showerror("Error", "Venue not found")

    # Finds and displays venue info
    def findVenue(self):
        venueID = simpledialog.askstring("Find Venue", "Enter ID")
        if venueID in self.venues:
            venue = self.venues[venueID]
            details = str(venue)
            messagebox.showinfo("Venue Details", details)
        else:
            messagebox.showerror("Error", "Venue not found")


root = tk.Tk()
app = ManagementSystem(root)
root.mainloop()
