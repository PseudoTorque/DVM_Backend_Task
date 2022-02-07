# This is the class that will serve as the debit card of the user, use is pretty redundant but I decided to implement
# as it was mentioned in the task requirements.
# Class stores basic card data such as the card number(randomly generated on registering a new account), the PIN; which
# the user will be authenticated against.

class card:
    def __init__(self, Number, PIN, FailedAttempts=0):
        self.Number = Number
        self.PIN = PIN
        self.FailedAttempts = FailedAttempts