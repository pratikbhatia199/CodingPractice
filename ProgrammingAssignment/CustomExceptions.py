__author__ = 'pratik'

import Globals


class BlankValues(Exception):
    def __init__(self, row_number, col_name):
        self.msg = col_name+" cannot be blank at row "+str(row_number)

    def __str__(self):
        return repr(self.msg)


class DealValue(Exception):
    def __init__(self, row_number, value):
        self.msg = "Deal Value should be negative. "+\
                   "Found "+str(value)+", at row "+ str(row_number)

    def __str__(self):
        return repr(self.msg)


class DealType(Exception):
    def __init__(self, row_number, value):
        self.msg = "Deal type can only be of following types: " + \
                   ', '.join(Globals.set_possible_deal_types)+\
                   ". Found "+value+", at row "+str(row_number)

    def __str__(self):
        return repr(self.msg)

class InvalidSequence(Exception):
    def __init__(self, row_number, start_date, end_date):
        self.msg = "Start date "+start_date+\
                   " cannot be greater than end date "+end_date+\
                   " found at row "+row_number

    def __str__(self):
        return repr(self.msg)

class InvalidCommandLine:
    def __init__(self):
        self.msg = "Invalid command line parametes"

    def __str__(self):
        return repr(self.msg)

class NegativeStay:
    def __init__(self, value):
        self.msg = "Stay days cannot be negative. Found "+value

    def __str__(self):
        return repr(self.msg)
