import court, user

class Reservation:
    ser = 0
    reservationsData = []


    def __init__(self, court, userName, userID, date, startTime, endTime):
        self.__resID = self.__class__.ser
        self.__class__.ser+=1
        self.__court = court
        self.__userName = userName
        self.__userID = userID
        self.__reservationData = (date, startTime, endTime)
        __class__.reservationsData.append(self.__dict__)

    @property
    def resID(self):

        return self.__resID
    
    @property
    def court(self):

        return self.__court
    
    @property
    def userName(self):

        return self.__userName
    
    @property
    def userID(self):

        return self.__userID
    
    @property
    def reservationData(self):

        return self.__reservationData

    @classmethod
    def getResData(__class__, resID):

        return __class__.reservationsData[resID][0]
    

    @classmethod
    def getResUser(__class__, resID):

        return __class__.reservationsData[resID][1]
    
    @classmethod
    def getResID(__class__, resID):

        return __class__.reservationsData[resID][2]