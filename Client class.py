class Client:
    """Class to represent the client information"""
    def __init__(self, clientName, clientID, clientAddress, email, phoneNum, clientBudget):
        self.clientName = clientName
        self.clientID = clientID
        self.clientAddress = clientAddress
        self.email = email
        self.phoneNum = phoneNum
        self.clientBudget = clientBudget
