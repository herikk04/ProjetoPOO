from  user import User

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
        ## print("______________________________________")
        ## print(f"Renter {self.renterID} created")
        ## print(f"Renter {self.renterID} data: {self.__dict__}")
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

