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

        ttk.Button(self.addEventWindow, text="Save Event", command=self.add_event).grid(row=len(lbls), column=1)


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
