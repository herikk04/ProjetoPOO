import pandas as pd


class User:
    userData = {"Locator": [], "Renter": []}

    def __init__(self, name, email, phoneNumber, username, password):
        self.userType = None
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = password
        print("______________________________________")
        print(f"User created")

    def getSelfType(self):
            
        return self.userType


    @classmethod
    def updateUserData(__class__, userType):
        if userType == "Locator":
            newLocatorData = pd.DataFrame(__class__.userData["Locator"])
            newLocatorData.to_csv("userData/locatorData.csv", index=False)
            
        elif userType == "Renter":
            newRenterData = pd.DataFrame(__class__.userData["Renter"])
            newRenterData.to_csv("userData/renterData.csv", index=False)


    @classmethod
    def getUserObject(__class__, userType, userID):
        if userType == "Locator":

            return __class__.userData["Locator"][userID]["object"]
        
        elif userType == "Renter":

            return __class__.userData["Renter"][userID]["object"]
