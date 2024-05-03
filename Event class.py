class Event(Venue, Client, Guest, Caterer):
    """Class to represent the event information"""
    def __init__(self, eventName, eventID, eventType, eventTheme, date, time, duration, venueAddress, clientID, guestName, guestID, guestAddress, email, phoneNum, catererName, catererID, address, catererPhoneNum, catererEmail, serviceType, invoice):
        Venue.__init__(self, venueAddress)
        Client.__init__(self, clientID)
        Guest.__init__(self, guestName, guestID, guestAddress, email, phoneNum)
        Caterer.__init__(self, catererName, catererID, address, catererPhoneNum, catererEmail, serviceType)
        self.eventName = eventName
        self.eventID = int(eventID)
        self.eventType = eventType
        self.eventTheme = eventTheme
        self.date = date
        self.time = time
        self.duration = duration
        self.invoice = float(invoice)
