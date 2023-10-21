import reservation, user, agenda


class Court:
    ser = 0
    courtReservationData = []


    def __init__(self, type, location, pricePerHour, week_days, weekend):
        self.courtID = self.__class__.ser
        self.__class__.ser+=1
        self.type = type
        self.location = location
        self.pricePerHour = pricePerHour
        self.agenda = agenda.Agenda(self.courtID, week_days, weekend)


    def bookCourt(self, user, date, startTime, endTime):
        if self.checkAvailability(date, startTime, endTime) == True:
            reservation.Reservation(self.courtID, user, date, startTime, endTime)
            agenda.Agenda.updateAgenda(self.courtID, date, startTime, endTime, [user, False])
            
            __class__.courtReservationData.append(reservation.Reservation.getResID(self.courtID)) ## Guardar os courtID's de reserva em todos os objetos User
        else:
            return False

    def cancelBooking(self, resID):
        reservationToCancel = reservation.Reservation.getResData[resID] 
        if self.checkAvailability(agenda.Agenda.courtAgendaData[self.courtID][reservationToCancel[1][0]][reservationToCancel[1][1]:reservationToCancel[1][2]]) == False:
            agenda.Agenda.updateAgenda(resID, reservationToCancel[1][0], reservationToCancel[1][1], reservationToCancel[1][2], [None, True])

    
    @classmethod
    def getDetails(__class__, courtID):


        return __class__.courtReservationData[courtID]
    

    def checkAvailability(self, date, startTime, endTime):
        for timeSlot in agenda.Agenda.getAgenda(self.courtID)[date][startTime:endTime]:
            if timeSlot[1] == False:

                return False
            
        return True