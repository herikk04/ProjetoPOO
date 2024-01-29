import pandas as pd
from ast import literal_eval
class Agenda:
    agendaData = []
    ser = 0

    def __init__(self, court, courtAgenda):
        self.agendaID = self.__class__.ser
        self.__class__.ser+=1
        self.court = court
        self.courtAgenda = courtAgenda
        ## print("______________________________________")
        ## print(f"Agenda {self.agendaID} created")
        __class__.agendaData.append(self.courtAgenda)
        ## create csv for each agenda
        newAgendaData = pd.DataFrame(self.__dict__)
        newAgendaData.to_csv(f"agendaData/agendaData{self.agendaID}.csv", index=False)

    @classmethod
    def getAgenda(__class__, agendaID): 
        return __class__.agendaData[agendaID]
    

    def updateAgenda(self, date, startTime, endTime, value):
        for i in range(startTime, endTime+1):
            literal_eval(self.courtAgenda[date])[i] = value
        # update dataframe
        self.courtAgenda.to_csv(f"agendaData/agendaData{self.agendaID}.csv", index=True)

    @classmethod
    def filterAgenda(__class__, agenda):
        today = pd.Timestamp('now').day
        agenda = list(agenda)
        agenda = agenda[today]
        agenda = literal_eval(agenda) ## mudar essa lógica para a classe dataRecover
        ## create series for hours from 0 to 23
        hours = pd.Series(range(0,24))
        hours = hours.apply(lambda x: f"{x}:00")
        agenda = pd.DataFrame(agenda, index=hours)
        ## set column name
        agenda.columns = ["None", "Disponibilidade"]
        agenda = agenda.drop("None", axis=1)
        for i, timeSlot in enumerate(agenda["Disponibilidade"]):
            if timeSlot == True:
                agenda["Disponibilidade"].iloc[i] = "Disponível"
            else:
                agenda["Disponibilidade"].iloc[i] = "Indisponível"
        print(agenda)
        ## tem alguma coisa errada, não estão aparecendo todos os horários livres
        return agenda

       
