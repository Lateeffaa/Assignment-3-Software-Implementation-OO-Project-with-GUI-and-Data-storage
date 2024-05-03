class Guest:
    """Class to represent the guest information"""
    def __init__(self, guestName, guestID, guestAddress, email, phoneNum):
        self.guestName = guestName
        self.guestID = int(guestID)
        self.guestAddress = guestAddress
        self.email = email
        self.phoneNum = int(phoneNum)
