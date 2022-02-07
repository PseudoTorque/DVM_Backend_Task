# This is the class that will serve as a representation of the user.
# Class stores basic user data such as the username of the account that the user holds, the card number; which are
# linked together.

class user:
    def __init__(self, AccountUsername, CardNumber):
        self.AccountUsername = AccountUsername
        self.CardNumber = CardNumber
