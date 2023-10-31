import court, flaskrun
class User:
    ser = 0
    userData = {"Locator": [], "Renter": []}

    def __init__(self, name, email, phoneNumber, username, password):
        self.userType = None
        self.userID = self.__class__.ser
        self.__class__.ser+=1
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = password


    def getSelfType(self):
            
        return self.userType


    def getSelfUserID(self):

        return self.userID


    @classmethod
    def getUserObject(__class__, userType, userID):
        if userType == "Locator":

            return __class__.userData["Locator"][userID]["object"]
        
        elif userType == "Renter":

            return __class__.userData["Renter"][0][0]["object"]

class Locator(User):
    ser = 0

    def __init__(self, name, email, phoneNumber, username, password): ## TERMINAR A LÓGICA DE SENHA E USUÁRIO
        super(Locator,self).__init__(name, email, phoneNumber, username, password)
        self.userType = "Locator"
        self.locatorID = self.__class__.ser
        self.__class__.ser+=1
        self.ownedCourts = []
        self.object = self
        super().userData["Locator"].append(self.__dict__) ## parâmetro self.ownedCourts tem os ID's das quadras


    def addCourts(self, courtType, location, pricePerHour, weekend, week_days):
        print("OI")
        court.Court(self, courtType, location, pricePerHour, weekend, week_days)


class Renter(User):
    ser = 0

    def __init__(self, name, email, phoneNumber, username, password,):
        super().__init__(name, email, phoneNumber, username, password)
        self.userType = "Renter"
        self.renterID = self.__class__.ser
        self.__class__.ser+=1
        self.reservations = []
        super().userData["Renter"].append([self, self.userType, self.userID, self.renterID, self.username, self.password, self.name, self.email, self.phoneNumber, self.reservations])


    @classmethod
    def registerReservation(__class__, reservationID, userID):
        super().userData["Renter"][0][userID][8].append(reservationID)


    @classmethod
    def unregisterReservation(__class__, reservationID, userID):
        del super().userData["Renter"][0][userID][8][reservationID] ## PRECISA SER OBSERVADO --> NA HORA DE REMOVER A RESERVA CERTA
    
    
    @classmethod
    def getRenterName(__class__, userID):  ## TALVEZ SERÁ PASSADO PARA A CLASSE MÃE
        
        return super().userData["Renter"]

