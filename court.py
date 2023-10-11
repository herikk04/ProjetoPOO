import reservation, user, agenda


class Court:
    ser = 0
    courtReservationData = []


    def __init__(self, type, location, pricePerHour, availability):
        self.agenda = agenda.Agenda(self.id, availability)
        self.__class__.ser+=1
        self.id = self.__class__.ser
        self.type = type
        self.location = location
        self.pricePerHour = pricePerHour
        self.availability = agenda.Agenda.getAvailabilty(self.id)
    

    def getDetails(self):

        return self.type, self.location, self.pricePerHour
    

    def checkAvailability(self, date, startTime, endTime):
        for timeSlot in agenda.Agenda.courtAgendaData[self.id][date][startTime:endTime]:
            if timeSlot == False:

                return False
            
        return True
    

    def bookCourt(self, user, date, startTime, endTime):
        userReservation = reservation.Reservation(self.id, user, date, startTime, endTime)
        if self.checkAvailability(userReservation.getResData()) == True:
            for timeSlot in agenda.Agenda.courtAgendaData[self.id][date][startTime:endTime]:
                timeSlot = [userReservation.getResUser(), False]

            __class__.courtReservationData.append(userReservation.getResId()) ## Guardar os id's de reserva em todos os objetos User
    

    def cancelBooking(self, resID):
        reservationToCancel = reservation.Reservation.getResData[resID]
        if self.checkAvailability(agenda.Agenda.courtAgendaData[self.id][reservationToCancel[1][0]][reservationToCancel[1][1]:reservationToCancel[1][2]]) == False:
            for timeSlot in agenda.Agenda.courtAgendaData[self.id][reservationToCancel[1][0]][reservationToCancel[1][1]:reservationToCancel[1][2]]:
                timeSlot = [None, True]

