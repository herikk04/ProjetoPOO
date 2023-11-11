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
        self.__name = name
        self.__email = email
        self.phoneNumber = phoneNumber
        self.__username = username
        self.password = password
        print("______________________________________")
        print(f"User created")

    @property
    def name(self):
            
            return self.__name
    
    @property
    def email(self):
                
            return self.__email
    
    @property
    def username(self):
                    
            return self.__username

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
        self.__userType = "Locator"
        self.__locatorID = self.__class__.locatorSer
        self.__class__.locatorSer+=1
        self.ownedCourts = []
        self.object = self
        super().userData["Locator"].append(self.__dict__)
        print("______________________________________")
        print(f"Locator {self.locatorID} created")
        print(f"Locator {self.locatorID} data: {self.__dict__}")
        super().updateUserData("Locator")

    @property  
    def locatorID(self):
            
        return self.__locatorID
    
    @property
    def userType(self):
         
         return self.__userType

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
        self.__userType = "Renter"
        self.__renterID = self.__class__.renterSer
        self.__class__.renterSer+=1
        self.reservations = []
        self.object = self
        super().userData["Renter"].append(self.__dict__)
        print("______________________________________")
        print(f"Renter {self.renterID} created")
        print(f"Renter {self.renterID} data: {self.__dict__}")
        super().updateUserData("Renter")

    @property
    def renterID(self):
            
        return self.__renterID
    
    @property
    def userType(self):
         
         return self.__userType

    @classmethod
    def registerReservation(__class__, reservationID, userID):
        super().userData["Renter"][userID]["reservations"].append(reservationID)
        super().updateUserData("Renter")


    @classmethod
    def unregisterReservation(__class__, reservationID, userID):
        del super().userData["Renter"][userID]["reservations"] ## PRECISO DE UM ID DE RESERVA PARA CADA USUÁRIO: MOSTRA ONDE ESTÁ A RESERVA EM SELF.RESERVATIONS
        super().updateUserData("Renter")                       ## PENSAR EM UMA LÓGICA PARA DELETAR A RESERVA
    
    
    @classmethod
    def getRenterName(__class__, userID):  ## TALVEZ SERÁ PASSADO PARA A CLASSE MÃE
        
        return super().userData["Renter"]
    
    def getID(self):

        return self.renterID

