import court
from numpy import zeros
import pandas as pd

class Agenda:
    agendaData = []

    ## PARECE TER UM ERRO NA CRIAÇÃO DE AGENDAS, VERIFICAR PARA DIAS DA SEMANA --  scripts.js, flaskrun.py
    def __init__(self, aCourt, weekDays, weekend):
        self.agendaID = aCourt
        wD, wE = weekDays, weekend
        
        for i, timeSlot in list(enumerate(wD)):
            if timeSlot == 0:
                wD[i] = [None, False]
            elif timeSlot == 1:
                wD[i] = [None, True]
        
        for i, timeSlot in list(enumerate(wE)):
            if timeSlot == 0:
                wE[i] = [None, False]
            elif timeSlot == 1:
                wE[i] = [None, True]

        self.courtAgenda = list(zeros(700))
        for i in range(0,699,7):
            self.courtAgenda[i] = wD.copy()
            self.courtAgenda[i+1] = wD.copy()
            self.courtAgenda[i+2] = wD.copy()
            self.courtAgenda[i+3] = wD.copy()
            self.courtAgenda[i+4] = wD.copy()
            self.courtAgenda[i+5] = wE.copy()
            self.courtAgenda[i+6] = wE.copy()
        
        print("______________________________________")
        print(f"Agenda {self.agendaID} created")
        __class__.agendaData.append(self.courtAgenda)
        ## create csv for each agenda
        newAgendaData = pd.DataFrame(self.__dict__)
        newAgendaData.to_csv(f"agendaData/agendaData{self.agendaID}.csv", index=False)


    @classmethod
    def getAgenda(__class__, agendaID):

        return __class__.agendaData[agendaID]
    

    @classmethod
    def updateAgenda(__class__, agendaID, date, startTime, endTime, value):
        for i in range(startTime,endTime+1):
            __class__.agendaData[agendaID][date-1][i] = value
        newAgendaData = pd.DataFrame(__class__.agendaData[agendaID])
        newAgendaData.to_csv(f"agendaData/agendaData{agendaID}.csv", index=True)
        


       
