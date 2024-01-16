import pandas as pd
import ast

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
    

    @classmethod
    def updateAgenda(self, date, startTime, endTime, value):
        for i in range(startTime,endTime+1):
            self.agendaData[date-1][i] = value
        newAgendaData = pd.DataFrame(self.agendaData)
        newAgendaData.to_csv(f"agendaData/agenda{self.agendaID}Data.csv", index=True)

    @classmethod
    def filterAgenda(__class__, agenda):
        today = pd.Timestamp('now').day
        agenda = list(agenda)
        agenda = agenda[today]
        agenda = ast.literal_eval(agenda)
        ## create series for hours from 0 to 23
        hours = pd.Series(range(0,24))
        hours = hours.apply(lambda x: f"{x}:00")
        agenda = pd.DataFrame(agenda, index=hours)
        ## set column name
        agenda.columns = ["None", "Disponibilidade"]
        agenda = agenda.drop("None", axis=1)
        for i, timeSlot in enumerate(agenda["Disponibilidade"]):
            if timeSlot == True:
                agenda["Disponibilidade"][i] = "Disponível"
            else:
                agenda["Disponibilidade"][i] = "Indisponível"
        print(agenda)
        return agenda

       
