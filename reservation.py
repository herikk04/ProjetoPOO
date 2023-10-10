import court, user

class Reservation:
    ser = 0
    reservationsData = []


    def __init__(self, court, user, date, startTime, endTime):
        self.__class__.ser+=1
        self.id = self.__class__.ser
        self.court = court
        self.user = user
        self.reservationData = (date, startTime, endTime)
        __class__.reservationsData.append([self.id, self.reservationData, court])


    
    def getResData(self):

        return self.resevationData
    

    def getResUser(self):

        return self.user
    
    def getResId(self):

        return self.id