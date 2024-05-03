class Caterer:
    """Class to represent the caterer information"""
    def __init__(self, catererName, catererID, address, catererPhoneNum, catererEmail, serviceType, minGuests, maxGuests):
        self.catererName = catererName
        self.catererID = int(catererID)
        self.address = address
        self.catererPhoneNum = int(catererPhoneNum)
        self.catererEmail = catererEmail
        self.serviceType = serviceType
        self.minGuests = int(minGuests)
        self.maxGuests = int(maxGuests)
