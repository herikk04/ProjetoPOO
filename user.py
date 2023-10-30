import court, flaskrun
class User:
    ser = 0
    userData = {"Locator": [], "Renter": []}

    def __init__(self, name, email, phoneNumber):
        self.userID = self.__class__.ser
        self.__class__.ser+=1
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber


class Locator(User):
    ser = 0

    def __init__(self, name, username, password, email, phoneNumber, ownedCourtsNum): ## TERMINAR A LÓGICA DE SENHA E USUÁRIO
        super().__init__(name, email, phoneNumber)
        self.locatorID = self.__class__.ser
        self.__class__.ser+=1
        self.ownedCourts = []
        for _ in range(ownedCourtsNum):
            type = input()
            location = input()
            pricePerHour = input()
            week_days = input()
            weekend = input()
            thiscourt = court.Court(type, location, pricePerHour, week_days, weekend)
            self.ownedCourts.append(thiscourt.giveID())

        super().userData["Locator"].append([self.locatorID, self.name, self.email, self.phoneNumber, self.ownedCourts]) ## parâmetro self.ownedCourts tem os ID's das quadras


class Renter(User):
    ser = 0

    def __init__(self, name, username, password, email, phoneNumber):
        super().__init__(name, email, phoneNumber)
        self.renterID = self.__class__.ser
        self.__class__.ser+=1
        self.reservations = []
        super().userData["Renter"].append(self.renterID, self.name, self.email, self.phoneNumber, self.reservations)


    @classmethod
    def registerReservation(__class__, reservationID, userID):
        super().userData["Renter"][userID][4].append(reservationID)


    @classmethod
    def unregisterReservation(__class__, reservationID, userID):
        del super().userData["Renter"][userID][4][reservationID] ## PRECISA SER OBSERVADO --> NA HORA DE REMOVER A RESERVA CERTA
    
    
    @classmethod
    def getRenterName(__class__, userID):  ## TALVEZ SERÁ PASSADO PARA A CLASSE MÃE
        
        return super().userData["Renter"]
    

    

    
