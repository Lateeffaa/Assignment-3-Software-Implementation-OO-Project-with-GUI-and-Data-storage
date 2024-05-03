class Venue:
    """Class to represent the venue information"""
    def __init__(self, venueName, venueID, venueAddress, contactNum, minGuests, maxGuests):
        self.venueName = venueName
        self.venueID = venueID
        self.venueAddress = venueAddress
        self.contactNum = contactNum
        self.minGuests = minGuests
        self.maxGuests = maxGuests
