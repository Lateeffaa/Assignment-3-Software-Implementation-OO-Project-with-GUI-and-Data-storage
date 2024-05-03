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
        return (f"Name: {self.name()}\nEmployee ID: {self.empID}\nDepartment: {self.department}\nJob Title: {self.jobTitle}\nBasic Salary: {self.basicSalary}\nAge: {self.age}"
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
        self.budget = newBudget
    def displayInfo(self):
        # Return details of the client
        return f"Client Name: {self.clientName}\nClient ID: {self.clientID}\nClient Address: {self.clientAddress}\nEmail: {self.email}\n Phone Number: {self.phoneNum}\nBudget: {self.budget}"

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
    def __init__(self, supplierName, supplierID, supplierAddress, email, phoneNum, supplierCompany, minGuests, maxGuests):
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
    def __init__(self, eventName, eventID, eventType, eventTheme, date, time, duration, venueAddress, clientID, guestList, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany,
                 furnitureSupplyCompany, invoice):
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

    def addSupplier(self, supplierName, supplierID, supplierAddress, email, phoneNum, supplierCompany):
        # Add supplier to event
        newSupplier = Supplier(supplierName, supplierID, supplierAddress, email, phoneNum, supplierCompany)
        self.suppliers.append(newSupplier)
        return newSupplier
    def removeSupplier(self, supplierID):
        # Remove supplier from event
        self.suppliers = [supplier for supplier in self.suppliers if supplier.supplierID != supplierID]

    def addGuest(self, guest):
        # Add guest to event
        self.guests.append(guest)
    def removeGuest(self, guestID):
        # Remove guest from event
        self.guests = [guest for guest in self.guests if guest.guestID != guestID]
    def getInfo(self):
        # details of the event
        details = f"Event Name: {self.eventName}\n Event ID: {self.eventID}\n Type: {self.eventType}\n Date: {self.date}\n Time: {self.time}\n Duration: {self.duration}\n Venue Address: {self.venueAddress}\n Client ID: {self.clientID}\n Guest List: {self.guestList}\n Supplier List: {self.suppliers}\n Invoice: {self.invoice}"
        getInfo = ', '.join([guest.getInfo() for guest in self.guests])
        return f"{details}\nGuests: {getInfo}"
