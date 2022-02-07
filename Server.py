# This is the class that will serve as a representation of the server (a mock server).
# Class stores all the data of the class objects and therefore serves as the actual server that real ATMs query to.
# Loading and saving is done to a JSON file.

import json
import logging

from Card import card
from User import user
from Account import account

class server:
    def __init__(self):
        #initializing the storage containers for the databases.
        self.CardDatabase = []
        self.UserDatabase = []
        self.AccountDatabase = []

    #loads data from json file in the form a dict list and converts to class object by matching appropriate fields.
    def loadData(self):
        with open("data.json", "r") as file:
            data = json.load(file)
        try:
            for i in data["CardDatabase"]:
                self.CardDatabase.append(card(i["Number"], i["PIN"], i["FailedAttempts"]))
        except:
            logging.warning("Could not load Card data.")
        try:
            for i in data["UserDatabase"]:
                self.UserDatabase.append(user(i["AccountUsername"], i["CardNumber"]))
        except:
            logging.warning("Could not load User data.")
        try:
            for i in data["AccountDatabase"]:
                self.AccountDatabase.append(account(i["Username"], i["Password"], i["Balance"]))
        except:
            logging.warning("Could not load Account data.")

    #saves data to the json data file by converting object fields to a dict and storing.
    def saveData(self):
        data = {
            "CardDatabase": [i.__dict__ for i in self.CardDatabase],
            "UserDatabase": [i.__dict__ for i in self.UserDatabase],
            "AccountDatabase": [i.__dict__ for i in self.AccountDatabase]
        }
        with open("data.json", "w+") as file:
            json.dump(data, file)
        logging.info("Saved to server data to file.")

    #used to add an entry to the databases and/or validate for redundancy
    def addOrValidateData(self, data, validation=""):
        if(validation==""):
            if(str(type(data))=="<class 'Card.card'>"):
                if(data.__dict__ in [i.__dict__ for i in self.CardDatabase]):
                    logging.warning("The data already exists in the server")
                    return False
                self.CardDatabase.append(data)
                logging.info("Data added")
                return True
            if (str(type(data)) == "<class 'User.user'>"):
                if (data.__dict__ in [i.__dict__ for i in self.UserDatabase]):
                    logging.warning("The data already exists in the server")
                    return False
                self.UserDatabase.append(data)
                logging.info("Data added")
                return True
            if (str(type(data)) == "<class 'Account.account'>"):
                if (data.__dict__ in [i.__dict__ for i in self.AccountDatabase]):
                    logging.warning("The data already exists in the server")
                    return False
                self.AccountDatabase.append(data)
                logging.info("Data added")
                return True
            logging.warning("Illegal data added to server attempt")
            return False
        if(validation == "Card"):
            if(data in [i.__dict__["Number"] for i in self.CardDatabase]):
                return False
            return True
        if(validation == "Account"):
            if (data in [i.__dict__["Username"] for i in self.AccountDatabase]):
                return False
            return True
    def validateAndFindUser(self, username, password):
        if(username in [i.Username for i in self.AccountDatabase]):
            for i in self.AccountDatabase:
                if(i.Username == username):
                    acc = i
                    break
            if(i.Password == password):
                for i in self.UserDatabase:
                    if(i.AccountUsername == username):
                        us = i
                for i in self.CardDatabase:
                    if(i.Number == us.CardNumber):
                        crd = i
                return [crd, us, acc]
            else:
                return False
        else:
            return False
