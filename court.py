import reservation, agenda, renter, user
import pandas as pd
from ast import literal_eval

class Court:
    ser = 0
    courtReservationData = []
    courtData = {}


    def __init__(self, thisLocator, locatorID, courtType, location, pricePerHour, courtagenda):
        self.courtID = self.__class__.ser
        self.__class__.ser+=1
        self.thisLocator = thisLocator
        self.locatorID = locatorID
        self.courtType = courtType
        self.location = location
        self.pricePerHour = pricePerHour
        thisAgenda = agenda.Agenda(self, courtagenda)
        self.agenda = thisAgenda

        userexsits = self.locatorID in list(__class__.courtData.keys())
        
        if userexsits: 
            __class__.courtData[self.locatorID][self.courtID] = self.__dict__ 
            thisLocator.ownedCourts.append(self)
        else:
            __class__.courtData[self.locatorID] = {self.courtID : self.__dict__} ## VERIFICAR SE ESTÁ FUNCIONANDO ( )
            thisLocator.ownedCourts.append(self)

        ## print("______________________________________")
        ## print(f"Court {self.courtID} created")
        ## print(f"Court {self.courtID} data: {self.__dict__}")
        ## print(f"Court Data: {__class__.courtData}")
        
        self.updateCourtData(userexsits)
        user.User.updateUserData("Locator")
    
    def getDetails(self):
        details = {}
        details["courtType"] = self.courtType
        details["location"] = self.location
        details["pricePerHour"] = self.pricePerHour
        details["courtID"] = self.courtID
        details["locatorID"] = self.locatorID

        return details

    def getCourtID(self):

        return self.courtID

    def updateCourtData(self, userexsits):
        ## create csv for each locator
        newCourtData = pd.DataFrame(self.__class__.courtData[self.locatorID][self.courtID], index=[self.courtID])
        if userexsits:
            oldCourtData = pd.read_csv(f"courtData/locator{self.locatorID}CourtData.csv")
            newCourtData = pd.concat([oldCourtData, newCourtData], ignore_index=True)
        newCourtData.to_csv(f"courtData/locator{self.locatorID}CourtData.csv", index=False)

    def bookCourt(self, userID, startTime):
        today = pd.Timestamp('now').day
        date = today
        startTime = self.hourToInt(startTime) - 1
        endTime = startTime + 1
        print("______________________________________")
        print(f"Booking court {self.courtID} for user {userID}")
        print("______________________________________")
        print(f"Reservation data: {date}, {startTime}, {endTime}")
        if self.checkAvailability(date, startTime, endTime) == True:
            thisreservation = reservation.Reservation(self.courtID, userID, user.User.getUserName("Renter", userID), date, startTime, endTime)
            self.agenda.updateAgenda(date, startTime, endTime, [user.User.getUserName("Renter", userID), False])
            renter.Renter.registerReservation(thisreservation, userID)
            print("______________________________________")
            print(f"Reservation {thisreservation} created")
            print(f"Reservation {thisreservation} data: {thisreservation.getResData()}")
        else:
            return False

    def cancelBooking(self, resID):
        reservationToCancel = reservation.Reservation.getResData[resID] 
        if self.checkAvailability(agenda.Agenda.agendaData[self.courtID][reservationToCancel[1][0]][reservationToCancel[1][1]:reservationToCancel[1][2]]) == False:
            agenda.Agenda.updateAgenda(resID, reservationToCancel[1][0], reservationToCancel[1][1], reservationToCancel[1][2], [None, True])
            renter.Renter.unregisterReservation(reservationToCancel)
        else:

            return False
    

    def checkAvailability(self, date, startTime, endTime):
        for timeSlot in literal_eval(agenda.Agenda.getAgenda(self.courtID)[date])[startTime:endTime]:
            print("______________________________________")
            print(timeSlot)
            print("______________________________________")
            if timeSlot[1] == False:

                return False
            
        return True
    
    @staticmethod
    def hourToInt(hour):
        hour = hour.split(":")
        hour = int(hour[0])
        return hour
    