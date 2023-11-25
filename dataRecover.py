import agenda, court, locator, renter, reservation
from pandas import read_csv
from numpy import zeros

class DataRecover:
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

    def recoverCourtsObjects(thisLocator):
        courts = read_csv(f"courtData/locator{thisLocator.locatorID}CourtData.csv")
        for eachcourt in courts.iterrows():
            courtagenda = read_csv(f"agendaData/agendaData{eachcourt[1]['courtID']}.csv")["courtAgenda"]
            recoveredCourt = court.Court(thisLocator, thisLocator.locatorID, eachcourt[1]["courtType"], eachcourt[1]["location"], eachcourt[1]["pricePerHour"], courtagenda)
            print(f"Court {recoveredCourt.courtID} recovered")

    def recoverReservationsObjects(renterID):
        pass

    def recoverLocatorObjects():
        locators = read_csv("userData/locatorData.csv")
        for thisLocator in locators.iterrows():
            recoveredLocator = locator.Locator(thisLocator[1]["name"], thisLocator[1]["email"], thisLocator[1]["phoneNumber"], thisLocator[1]["username"], thisLocator[1]["password"])
            try:
                __class__.recoverCourtsObjects(recoveredLocator)
            except:
                print(f"Locator {recoveredLocator.locatorID} has no courts")
            print(f"Locator {recoveredLocator.locatorID} recovered")
            

    def recoverRenterObjects():
        renters = read_csv("userData/renterData.csv")
        for thisRenter in renters.iterrows():
            recoveredRenter = renter.Renter(thisRenter[1]["name"], thisRenter[1]["email"], thisRenter[1]["phoneNumber"], thisRenter[1]["username"], thisRenter[1]["password"])
            __class__.recoverReservationsObjects(recoveredRenter.renterID)
            print(f"Renter {recoveredRenter.renterID} recovered")