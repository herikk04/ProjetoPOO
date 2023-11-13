import pandas as pd

class Agenda:
    agendaData = []

    ## PARECE TER UM ERRO NA CRIAÇÃO DE AGENDAS, VERIFICAR PARA DIAS DA SEMANA --  scripts.js, flaskrun.py
    def __init__(self, aCourt, courtAgenda):
        self.__agendaID = aCourt
        self.courtAgenda = courtAgenda
        print("______________________________________")
        print(f"Agenda {self.agendaID} created")
        __class__.agendaData.append(self.courtAgenda)
        ## create csv for each agenda
        newAgendaData = pd.DataFrame(self.__dict__)
        newAgendaData.to_csv(f"agendaData/agendaData{self.agendaID}.csv", index=False)
    
    @property
    def agendaID(self):

        return self.__agendaID

    @classmethod
    def getAgenda(__class__, agendaID):

        return __class__.agendaData[agendaID]
    

    @classmethod
    def updateAgenda(__class__, agendaID, date, startTime, endTime, value):
        for i in range(startTime,endTime+1):
            __class__.agendaData[agendaID][date-1][i] = value
        newAgendaData = pd.DataFrame(__class__.agendaData[agendaID])
        newAgendaData.to_csv(f"agendaData/agendaData{agendaID}.csv", index=True)
        


       
