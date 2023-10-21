import court

class Agenda:
    courtAgendaData = []
    
    
    def __init__(self, aCourt, weekDays, weekend):
        self.agendaID = aCourt
        wD, wE = [(weekDays).split(' ')]*5,[(weekend).split(' ')]*2
        w = wD + wE
        self.courtAgenda = w*100
        for i in range(len(self.courtAgenda)):
            for j, timeSlot in list(enumerate(self.courtAgenda[i])):
                if timeSlot == '0':
                    self.courtAgenda[i][j] = [None, False]
                elif timeSlot == '1':
                    self.courtAgenda[i][j] = [None, True]
        self.__class__.courtAgendaData.append(self.courtAgenda)


    @classmethod
    def getAgenda(cls, agendaID):

        return cls.courtAgendaData[agendaID]
    

    @classmethod
    def updateAgenda(cls, agendaID, date, startTime, endTime, value):
        for i in range(startTime,endTime+1):
            cls.courtAgendaData[agendaID][date][i] = value
        
