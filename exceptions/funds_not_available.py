# Funds Not Available Exception

class FundsNotAvailable(Exception):

    def __init__(self, message):
        self.message = message
