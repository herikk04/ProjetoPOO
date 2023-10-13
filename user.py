class User:
    ser = 0

    def __init__(self, name, email, phoneNumber):
        self.userID = self.__class__.ser
        self.__class__.ser+=1
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber


class Locator(User):

    def __init__(self, name, email, phoneNumber, ownedCourtsNum, ownedCourts):
        self.ownedCourts = []
        for i in range(ownedCourtsNum):
            self.ownedCourts.append(ownedCourts[i])
    

    
