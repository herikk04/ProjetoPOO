import agenda, court, user
from pandas import read_csv
from numpy import zeros

def filterAgendaData(weekDays, weekend):
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

    courtAgenda = list(zeros(700))
    for i in range(0,699,7):
        courtAgenda[i] = wD.copy()
        courtAgenda[i+1] = wD.copy()
        courtAgenda[i+2] = wD.copy()
        courtAgenda[i+3] = wD.copy()
        courtAgenda[i+4] = wD.copy()
        courtAgenda[i+5] = wE.copy()
        courtAgenda[i+6] = wE.copy()
    return courtAgenda

def recoverAgendaObjects(courtID):
    agendaData = read_csv(f"agendaData/agendaData{courtID}.csv")
    thisAgenda = agenda.Agenda(courtID, agendaData["courtAgenda"])
    print(f"Agenda {thisAgenda.agendaID} recovered")
    

def recoverCourtsObjects(locatorID):
    courts = read_csv(f"courtData/locator{locatorID}CourtData.csv")
    for eachcourt in courts.iterrows():
        courtagenda = read_csv(f"agendaData/agendaData{eachcourt[1]['_Court__courtID']}.csv")["courtAgenda"]
        recoveredCourt = court.Court(locatorID, eachcourt[1]["_Court__courtType"], eachcourt[1]["_Court__location"], eachcourt[1]["pricePerHour"], courtagenda)
        recoverAgendaObjects(recoveredCourt.courtID)
        print(f"Court {recoveredCourt.courtID} recovered")

def recoverReservationsObjects(renterID):
    pass

def recoverLocatorObjects():
    locators = read_csv("userData/locatorData.csv")
    for locator in locators.iterrows():
        recoveredLocator = user.Locator(locator[1]["name"], locator[1]["email"], locator[1]["phoneNumber"], locator[1]["username"], locator[1]["password"])
        recoverCourtsObjects(recoveredLocator.locatorID)
        print(f"Locator {recoveredLocator.locatorID} recovered")
        

def recoverRenterObjects():
    renters = read_csv("userData/renterData.csv")
    for renter in renters.iterrows():
        recoveredRenter = user.Renter(renter[1]["name"], renter[1]["email"], renter[1]["phoneNumber"], renter[1]["username"], renter[1]["password"])
        recoverReservationsObjects(recoveredRenter.renterID)
        print(f"Renter {recoveredRenter.renterID} recovered")