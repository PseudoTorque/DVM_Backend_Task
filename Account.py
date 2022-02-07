# This is the class that will serve as the Account of the user.
# Class stores basic user account data such as the account balance, username and password; which the user will be
# authenticated against.

import logging

class account:
    def __init__(self, Username, Password, Balance=0):
        self.Username = Username
        self.Password = Password
        self.Balance = Balance

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if (self.Balance < amount):
                print("Insufficient funds in account! ")
                return False
            else:
                self.Balance -= amount
                if(amount < 0 or amount == 0):
                    print("Amount is invalid or zero. Make sure the amount is a positive, non-zero number! ")
                    return False
                print("\nWithdrawal succesful, new account balance is %.2f$." % self.Balance)
                logging.info("%s withdrew %.2f$ for new balance of %.2f$" % (self.Username, amount, self.Balance))
                return True
        except:
            print("Amount is invalid or zero. Make sure the amount is a positive, non-zero number! ")
            return False
    def deposit(self, amount):
        try:
            amount = float(amount)
            self.Balance += amount
            if (amount < 0 or amount == 0):
                print("Amount is invalid or zero. Make sure the amount is a positive, non-zero number! ")
                return False
            print("\nDeposit succesful, new account balance is %.2f$." % self.Balance)
            logging.info("%s deposited %.2f$ for new balance of %.2f$" % (self.Username, amount, self.Balance))
            return True
        except:
            print("Amount is invalid or zero. Make sure the amount is a positive, non-zero number! ")
            return False
    def displayBalance(self):
        print("\nAccount balance is %.2f$." % self.Balance)