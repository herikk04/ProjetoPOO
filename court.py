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
        for timeSlot in self.availability[date][startTime:endTime]:
            if timeSlot[1] == False:
                return False
        
        return True
    

    def bookCourt(self, user, date, startTime, endTime):
        userReservation = reservation.Reservation(self.id, user, date, startTime, endTime)
        if self.checkAvailability(userReservation.getResData()) == True:
            for timeSlot in self.availability[date][startTime:endTime]:
                timeSlot = [userReservation.getResUser(), False]
            __class__.courtReservationData.append(userReservation.getResId())
    

    def cancelBooking(self, resID):
        reservationToCancel = reservation.Reservation.reservationsData[resID]
        if self.checkAvailability(reservationToCancel[1]) == False:
            for timeSlot in self.availability[reservationToCancel[1][0]][reservationToCancel[1][1]:reservationToCancel[1][2]]:
                timeSlot = [None, True]

                