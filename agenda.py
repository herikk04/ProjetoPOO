import court

class Agenda:
    courtAgendaData = []
    
    def __init__(self, aCourt, week_days, weekend):
        self.id = aCourt
        self.courtAgenda = [[week_days]*5,[weekend]*2] * 100
        for day in self.courtAgenda:
            for timeSlot in day:
                if timeSlot == 0:
                    timeSlot = [None, False]
                elif timeSlot == 1:
                    timeSlot = [None, True]
        self.__class__.courtAgendaData.insert(self.id,self.courtAgenda)


    @classmethod
    def getAvailabilty(id):

        return __class__.courtAgendaData[id]
