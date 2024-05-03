class Supplier:
    """Class to represent the supplier information"""
    def __init__(self, supplierName, supplierID, supplierAddress, email, phoneNum, supplierCompany, minGuests, maxGuests):
        self.supplierName = supplierName
        self.supplierID = int(supplierID)
        self.supplierAddress = supplierAddress
        self.email = email
        self.phoneNum = int(phoneNum)
        self.supplierCompany = supplierCompany
        self.minGuests = int(minGuests)
        self.maxGuests = int(maxGuests)
