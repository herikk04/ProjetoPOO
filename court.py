import reservation, user, agenda


class Court:
    ser = 0
    courtReservationData = []
    courtData = []


    def __init__(self, locatorID, courtType, location, pricePerHour, week_days, weekend):
        self.courtID = self.__class__.ser
        self.__class__.ser+=1
        self.locatorID = locatorID
        self.courtType = courtType
        self.location = location
        self.pricePerHour = pricePerHour
        self.agenda = agenda.Agenda(self.courtID, week_days, weekend)
        print(f"Court {self.courtID} created")
        print(f"Court {self.courtID} data: {self.__dict__}")

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


    def bookCourt(self, userID, date, startTime, endTime):
        if self.checkAvailability(date, startTime, endTime) == True:
            thisreservation = reservation.Reservation(self.courtID, user.Locator.getRenterName(userID), date, startTime, endTime)
            agenda.Agenda.updateAgenda(self.courtID, date, startTime, endTime, [user, False])
            
            __class__.courtReservationData.append(thisreservation.getResID(self.courtID)) ## Guardar os courtID's de reserva em todos os objetos User
            user.Renter.registerReservation(thisreservation.getResID(self.courtID))
        else:
            
            return False

    def cancelBooking(self, resID):
        reservationToCancel = reservation.Reservation.getResData[resID] 
        if self.checkAvailability(agenda.Agenda.courtAgendaData[self.courtID][reservationToCancel[1][0]][reservationToCancel[1][1]:reservationToCancel[1][2]]) == False:
            agenda.Agenda.updateAgenda(resID, reservationToCancel[1][0], reservationToCancel[1][1], reservationToCancel[1][2], [None, True])
            user.Renter.unregisterReservation(reservationToCancel)
        else:

            return False
    
    def getCourtID(self):

        return self.courtID

    @classmethod
    def getDetails(__class__, courtID):

        return __class__.courtReservationData[courtID]
    

    def checkAvailability(self, date, startTime, endTime):
        for timeSlot in agenda.Agenda.getAgenda(self.courtID)[date][startTime:endTime]:
            if timeSlot[1] == False:

                return False
            
        return True
