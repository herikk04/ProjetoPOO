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
        __class__.reservationsData.append([self.reservationData, self.user, self.id, self.court])

    
    @classmethod
    def getResData(id):

        return __class__.reservationsData[id][0]
    

    @classmethod
    def getResUser(id):

        return __class__.reservationsData[id][1]
    
    @classmethod
    def getResId(id):

        return __class__.reservationsData[id][2]