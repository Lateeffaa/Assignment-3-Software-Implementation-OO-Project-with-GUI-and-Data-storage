class Client:
    """Class to represent the client information"""
    def __init__(self, clientName, clientID, clientAddress, email, phoneNum, clientBudget):
        self.clientName = clientName
        self.clientID = int(clientID)
        self.clientAddress = clientAddress
        self.email = email
        self.phoneNum = int(phoneNum)
        self.clientBudget = float(clientBudget)
