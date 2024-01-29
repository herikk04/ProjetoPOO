import pandas as pd
from ast import literal_eval


class User:
    userData = {"Locator": [], "Renter": []}

    def __init__(self, name, email, phoneNumber, username, password):
        self.userType = None
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = password
        ## print("______________________________________")
        ## print(f"User created")


    @classmethod
    def authenticateUser(__class__, username, password, userType):
        for user in __class__.userData[userType]:
            if user["username"] == username and user["password"] == password:
                ## print("______________________________________")
                ## print(f"User {username} succesfully authenticated!")
                if userType == "Locator":
                    return True, user["locatorID"]
                elif userType == "Renter":
                    return True, user["renterID"]
        return False, None


    @classmethod
    def updateUserData(__class__, userType, userObject=None):
        if userType == "Locator":
            if userObject != None:
                __class__.userData["Locator"][userObject.locatorID] = userObject.__dict__
            newLocatorData = pd.DataFrame(__class__.userData["Locator"])
            newLocatorData.to_csv("userData/locatorData.csv", index=False)
            
        elif userType == "Renter":
            if userObject != None:
                __class__.userData["Renter"][userObject.renterID] = userObject.__dict__
            newRenterData = pd.DataFrame(__class__.userData["Renter"])
            newRenterData.to_csv("userData/renterData.csv", index=False)


    @classmethod
    def getUserObject(__class__, userType, userID):
        if userType == "Locator":
            return __class__.userData["Locator"][userID]["object"]
        
        elif userType == "Renter":
            return __class__.userData["Renter"][userID]["object"]


    @classmethod
    def getUserName(__class__, userType, userID):
        if userType == "Locator":

            return __class__.userData["Locator"][userID]["name"]
        
        elif userType == "Renter":

            return __class__.userData["Renter"][userID]["name"]