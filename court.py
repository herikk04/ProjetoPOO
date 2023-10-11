import reservation, user, agenda


class Court:
    ser = 0
    courtReservationData = []


    def __init__(self, type, location, pricePerHour, week_days, weekend):
        self.id = self.__class__.ser
        self.__class__.ser+=1
        self.type = type
        self.location = location
        self.pricePerHour = pricePerHour
        self.agenda = agenda.Agenda(self.id, week_days, weekend)
    

    def getDetails(self):

        return self.type, self.location, self.pricePerHour
    

    def checkAvailability(self, date, startTime, endTime):
        for timeSlot in agenda.Agenda.courtAgendaData[self.id][date][startTime:endTime]:
            if timeSlot == False:

                return False
            
        return True
    

    def bookCourt(self, user, date, startTime, endTime):
        reservation.Reservation(self.id, user, date, startTime, endTime)
        if self.checkAvailability(date, startTime, endTime) == True:
            for timeSlot in agenda.Agenda.courtAgendaData[self.id][date][startTime:endTime]:
                timeSlot = [reservation.Reservation.getResUser(self.id), False]
            __class__.courtReservationData.append(reservation.Reservation.getResId(self.id)) ## Guardar os id's de reserva em todos os objetos User
    

    def cancelBooking(self, resID):
        reservationToCancel = reservation.Reservation.getResData[resID]
        if self.checkAvailability(agenda.Agenda.courtAgendaData[self.id][reservationToCancel[1][0]][reservationToCancel[1][1]:reservationToCancel[1][2]]) == False:
            for timeSlot in agenda.Agenda.courtAgendaData[self.id][reservationToCancel[1][0]][reservationToCancel[1][1]:reservationToCancel[1][2]]:
                timeSlot = [None, True]

