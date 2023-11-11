from typing import Any
import reservation, user, agenda
import pandas as pd

class Court:
    ser = 0
    courtReservationData = []
    courtData = []


    def __init__(self, locatorID, courtType, location, pricePerHour, week_days, weekend):
        self.__courtID = self.__class__.ser
        self.__class__.ser+=1
        self.__locatorID = locatorID
        self.__courtType = courtType
        self.__location = location
        self.pricePerHour = pricePerHour
        thisAgenda = agenda.Agenda(self.courtID, week_days, weekend)
        self.agendaID = thisAgenda.agendaID
        

        userexsits = False

        for locatordata in __class__.courtData:
            if locatorID in locatordata:
                userexsits = True
                break
        
        if userexsits: 
            __class__.courtData[0][self.locatorID].append(self.__dict__) 
            user.User.getUserObject("Locator", self.locatorID).ownedCourts.append(self.courtID)
        else:
            __class__.courtData.append({self.locatorID: [self.__dict__]})
            user.User.getUserObject("Locator", self.locatorID).ownedCourts.append(self.courtID)

        print("______________________________________")
        print(f"Court {self.courtID} created")
        print(f"Court {self.courtID} data: {self.__dict__}")
        print(f"Court Data: {__class__.courtData}")
        
        __class__.updateCourtData(self.locatorID)
    
    @property
    def courtID(self):

        return self.__courtID
    
    @property
    def locatorID(self):

        return self.__locatorID
    
    @property
    def courtType(self):

        return self.__courtType
    
    @property
    def location(self):

        return self.__location

    @classmethod
    def updateCourtData(__class__, locatorID):
        ## create csv for each locator
        newCourtData = pd.DataFrame(__class__.courtData[0][locatorID])
        newCourtData.to_csv(f"courtData/locator{locatorID}CourtData.csv", index=False)
        


    def bookCourt(self, userID, date, startTime, endTime):
        if self.checkAvailability(date, startTime, endTime) == True:
            thisreservation = reservation.Reservation(self.courtID, userID, user.Renter.getRenterName(userID), date, startTime, endTime)
            agenda.Agenda.updateAgenda(self.courtID, date, startTime, endTime, [user.Renter.getRenterName(userID), False])
            user.Renter.registerReservation(thisreservation.getResID(self.courtID), userID)
        else:
            
            return False

    def cancelBooking(self, resID):
        reservationToCancel = reservation.Reservation.getResData[resID] 
        if self.checkAvailability(agenda.Agenda.agendaData[self.courtID][reservationToCancel[1][0]][reservationToCancel[1][1]:reservationToCancel[1][2]]) == False:
            agenda.Agenda.updateAgenda(resID, reservationToCancel[1][0], reservationToCancel[1][1], reservationToCancel[1][2], [None, True])
            user.Renter.unregisterReservation(reservationToCancel)
        else:

            return False
    
    def getCourtID(self):

        return self.courtID
    

    def checkAvailability(self, date, startTime, endTime):
        for timeSlot in agenda.Agenda.getAgenda(self.courtID)[date][startTime:endTime]:
            if timeSlot[1] == False:

                return False
            
        return True

    @classmethod
    def getDetails(__class__, courtID):

        return __class__.courtReservationData[courtID]