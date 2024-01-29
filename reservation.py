import pandas as pd

class Reservation:
    ser = 0
    reservationsData = []

    ## Trocar IDs por objetos
    def __init__(self, court, userName, user, date, startTime, endTime):
        self.resID = self.__class__.ser
        self.__class__.ser+=1
        self.court = court
        self.userName = userName
        self.user = user
        self.reservationInfo = (date, startTime, endTime)
        __class__.reservationsData.append(self.__dict__)
        self.updateReservationsData()
    

    def updateReservationsData(self):
        newReservationsData = pd.DataFrame(self.__class__.reservationsData)
        newReservationsData.to_csv("reservationData/reservationsData.csv", index=False)

    def getResData(self):

        return self.reservationsData
    

    def getResUser(self):

        return self.user
    
    def getResID(self):

        return self.resID