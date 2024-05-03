class Venue:
    """Class to represent the venue information"""
    def __init__(self, venueName, venueID, venueAddress, contactNum, minGuests, maxGuests):
        self.venueName = venueName
        self.venueID = int(venueID)
        self.venueAddress = venueAddress
        self.contactNum = int(contactNum)
        self.minGuests = int(minGuests)
        self.maxGuests = int(maxGuests)
