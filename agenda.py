import court

class Agenda:
    courtAgendaData = []
    
    
    def __init__(self, aCourt, weekDays, weekend):
        self.id = aCourt
        self.courtAgenda = [[(' ').split(weekDays)]*5,[(' ').split(weekend)]*2] * 100
        for day in self.courtAgenda:
            for timeSlot in day:
                if timeSlot == '0':
                    timeSlot = [None, False]
                elif timeSlot == '1':
                    timeSlot = [None, True]
        self.__class__.courtAgendaData.insert(self.id,self.courtAgenda)


    @classmethod
    def getAvailabilty(__class__, id):

        return __class__.courtAgendaData[id]
