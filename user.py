import court, flaskrun
import pandas as pd

class User:
    userData = {"Locator": [], "Renter": []}
    firstRun = True

    if firstRun:
        print("______________________________________")
        print("Creating user first csv files...")
        locatorData = pd.DataFrame(userData["Locator"],columns=["userType", "name", "email", "phoneNumber", "username", "password", "ownedCourts"])
        renterData = pd.DataFrame(userData["Renter"], columns=["userType", "name", "email", "phoneNumber", "username", "password", "reservations"])
        locatorData.to_csv("locatorData.csv", index=False)
        renterData.to_csv("renterData.csv", index=False)
        firstRun = False

    def __init__(self, name, email, phoneNumber, username, password):
        self.userType = None
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = password
        print("______________________________________")
        print(f"User created")

    def getSelfType(self):
            
        return self.userType


    @classmethod
    def updateUserData(__class__, userType):
        if userType == "Locator":
            newLocatorData = pd.DataFrame(__class__.userData["Locator"], columns=["userType", "name", "email", "phoneNumber", "username", "password", "ownedCourts"])
            newLocatorData.to_csv("locatorData.csv", index=False)
            
        elif userType == "Renter":
            newRenterData = pd.DataFrame(__class__.userData["Renter"], columns=["userType", "name", "email", "phoneNumber", "username", "password", "reservations"])
            newRenterData.to_csv("renterData.csv", index=False)


    @classmethod
    def getUserObject(__class__, userType, userID):
        if userType == "Locator":

            return __class__.userData["Locator"][userID]["object"]
        
        elif userType == "Renter":

            return __class__.userData["Renter"][userID]["object"]

class Locator(User):
    locatorSer = 0

    def __init__(self, name, email, phoneNumber, username, password): ## TERMINAR A LÓGICA DE SENHA E USUÁRIO
        super(Locator,self).__init__(name, email, phoneNumber, username, password)
        self.userType = "Locator"
        self.locatorID = self.__class__.locatorSer
        self.__class__.locatorSer+=1
        self.ownedCourts = []
        self.object = self
        super().userData["Locator"].append(self.__dict__)
        print("______________________________________")
        print(f"Locator {self.locatorID} created")
        print(f"Locator {self.locatorID} data: {self.__dict__}")
        super().updateUserData("Locator")


    def addCourts(self, courtType, location, pricePerHour, weekend, week_days):
        thisCourt = court.Court(self.locatorID, courtType, location, pricePerHour, weekend, week_days)
        print("______________________________________")
        print(f"Locator {self.locatorID} added court {thisCourt.getCourtID()}")
        super().updateUserData("Locator")


    def getID(self):

        return self.locatorID


class Renter(User):
    renterSer = 0

    def __init__(self, name, email, phoneNumber, username, password,):
        super().__init__(name, email, phoneNumber, username, password)
        self.userType = "Renter"
        self.renterID = self.__class__.renterSer
        self.__class__.renterSer+=1
        self.reservations = []
        self.object = self
        super().userData["Renter"].append(self.__dict__)
        print("______________________________________")
        print(f"Renter {self.renterID} created")
        print(f"Renter {self.renterID} data: {self.__dict__}")
        super().updateUserData("Renter")

    @classmethod
    def registerReservation(__class__, reservationID, userID):
        super().userData["Renter"][userID]["reservations"].append(reservationID)
        super().updateUserData("Renter")


    @classmethod
    def unregisterReservation(__class__, reservationID, userID):
        del super().userData["Renter"][userID]["reservations"] ## PRECISA SER OBSERVADO --> NA HORA DE REMOVER A RESERVA CERTA
        super().updateUserData("Renter")
    
    
    @classmethod
    def getRenterName(__class__, userID):  ## TALVEZ SERÁ PASSADO PARA A CLASSE MÃE
        
        return super().userData["Renter"]
    
    def getID(self):

        return self.renterID

