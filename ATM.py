# This is the class that will serve as a representation of the ATM.
# Since the class is a representation of the actual ATM, it performs all the basic functions such as facilitating the
# user to withdraw, deposit and view the balance of their account. It can also be used to create an account for the user
# and provide a debit card. The ATM queries the mock server to authenticate entered credentials.

from Card import card
from User import user
from Account import account
from Server import server

import random

class atm:
    def __init__(self):
        self.server = server()
        self.server.loadData()
    def registerNewUser(self):
        while True:
            print("\n-----------------Creating an Account-----------------")
            print("Enter (Exit.) for exiting the account creation process.\n")
            print("Enter the username of your choice for the account: ", end="")
            username = input()
            if (username == "Exit."):
                break
            if (not self.server.addOrValidateData(data=username, validation="Account")):
                print("The username already exists. ")
            else:
                while True:
                    print("\nEnter the password to your account: ", end="")
                    password = input()
                    print("Enter the password again to confirm: ", end="")
                    confirm_password = input()
                    if (password == confirm_password):
                        break
                    else:
                        print("The entered passwords do not match. ")
                NewAccount = account(username, password)
                CardNumber = 4988
                while (not self.server.addOrValidateData(data=CardNumber, validation="Card")) or (
                        len(str(CardNumber)) == 4):
                    CardNumber = int(str(CardNumber) + str(int(random.random() * 1000000000000)))
                while True:
                    while True:
                        print("\nEnter the PIN for your new Debit Card (Number: %d) (Only digits allowed): " % (CardNumber),
                              end="")
                        try:
                            PIN = int(input())
                            PIN = str(PIN)
                            if(len(PIN) != 4):
                                print("The entered PIN should be 4 digits long. ")
                            else:
                                break
                        except:
                            print("The entered PIN can only be digits. ")
                    print("Enter the PIN again to confirm: ", end="")
                    confirm_PIN = input()
                    if (PIN == confirm_PIN):
                        break
                    else:
                        print("The entered PINs do not match. ")
                NewCard = card(CardNumber, PIN)
                NewUser = user(username, CardNumber)

                self.server.addOrValidateData(NewCard)
                self.server.addOrValidateData(NewUser)
                self.server.addOrValidateData(NewAccount)

                print("\nYour Account has been successfully created!\n")
                self.server.saveData()
                break
    def login(self):
        details = []
        while True:
            print("\n-----------------Login to your Account-----------------")
            print("Enter (Exit.) for exiting account management mode.\n")
            print("Enter the username for your account: ", end="")
            username = input()
            if(username == "Exit."):
                return
            if(self.server.addOrValidateData(data=username, validation="Account")):
                print("This account does not exist. ")
            else:
                while True:
                    print("Enter the password to your account: ", end="")
                    password = input()
                    response = self.server.validateAndFindUser(username, password)
                    if(response==False):
                        print("The entered password is incorrect. \n")
                    else:
                        details = response
                        while True:
                            if (details[0].FailedAttempts == 3):
                                print( "\nYour Debit Card (Card Number: %d) has been BLOCKED due to too many failed attempts. "%details[0].Number)
                                return
                            print("\nEnter the PIN for the card inserted (Card Number: %d) (%d Attempts remain): " % (details[0].Number, (3-details[0].FailedAttempts)), end="")
                            PIN = input()
                            try:
                                PIN = int(PIN)
                                PIN = str(PIN)
                                if(len(PIN) != 4):
                                    print("The entered PIN should be 4 digits long. ")
                                else:
                                    if(PIN == details[0].PIN):
                                        details[0].FailedAttempts = 0
                                        return details
                                    else:
                                        details[0].FailedAttempts += 1
                                        self.server.saveData()
                                        if (details[0].FailedAttempts == 3):
                                            print("\nYour Debit Card (Card Number: %d) has been BLOCKED due to too many failed attempts. " %details[0].Number)
                                            return
                                        print("The entered PIN is incorrect (%d Attempts remain). " % (3-details[0].FailedAttempts))
                            except:
                                print("The entered PIN can only be digits. ")
    def start(self):
        while True:
            print("\nWelcome to the Tyagi Bank, how may we be of service to you?")
            print("1. Withdraw/Deposit/View Balance")
            print("2. Create an Account with Us")
            print("3. Exit\n")
            answer = input()
            try:
                answer = int(answer)
                if (answer == 1):
                    details = self.login()
                    if (details):
                        while True:
                            print("\n-----------------Welcome %s!-----------------" % details[2].Username)
                            print("1. Withdraw Funds")
                            print("2. Deposit Funds")
                            print("3. View Account Balance")
                            print("4. Exit\n")
                            answer = input()
                            try:
                                answer = int(answer)
                                if (answer == 1):
                                    while True:
                                        print(
                                            "\nEnter the amount to be withdrawn from your account ((Exit.) to exit): ",
                                            end="")
                                        amount = input()
                                        if (amount == "Exit."):
                                            break
                                        response = details[2].withdraw(amount)
                                        if (response):
                                            break
                                    self.server.saveData()
                                if (answer == 2):
                                    while True:
                                        print("\nEnter the amount to be deposited to your account ((Exit.) to exit): ",
                                              end="")
                                        amount = input()
                                        if (amount == "Exit."):
                                            break
                                        response = details[2].deposit(amount)
                                        if (response):
                                            break
                                    self.server.saveData()
                                if (answer == 3):
                                    details[2].displayBalance()
                                if (answer == 4):
                                    break
                            except:
                                print("Enter a valid value. ")
                elif (answer == 2):
                    self.registerNewUser()
                elif (answer == 3):
                    self.server.saveData()
                    break
                else:
                    print("Enter a valid value. ")
            except:
                print("Enter a valid value. ")

