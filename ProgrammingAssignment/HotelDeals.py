__author__ = 'pratik'
import sys
import csv
from collections import defaultdict
import dateutil.parser as dparser
from datetime import datetime as datecheck
from CustomExceptions import DealValue, DealType, BlankValues, InvalidSequence, InvalidCommandLine, NegativeStay
import Constants


class HotelDeals:
    """
    This class is for a hotel deal instance with following attributes:
    hotel_name    : Hotel Name
    nightly_rate  : Rate per night of stay
    promo_txt     : The text for a given deal
    deal_value    : The discount, can be percentage if type is pct or a
                    dollar amount if type is rebate or rebate_3plus
    deal_type     : 1. pct: Percentage off,
                    2. rebate: Amount of discount off
                    3. rebate_3plus: Amount off if reservation is for more than 3 nights
    start_date    : The first day when promotion is valid
    end_date      : Last day when promotion is applicable
    """

    def __init__(self, hotel_name, nightly_rate, promo_txt, deal_value, deal_type, start_date, end_date):
        self.hotel_name = hotel_name
        self.nightly_rate = nightly_rate
        self.promo_txt = promo_txt
        self.deal_value = deal_value
        self.deal_type = deal_type
        self.start_date = dparser.parse(start_date)
        self.end_date = dparser.parse(end_date)

    def get_hotel_name(self):
        return self.hotel_name

    def get_nightly_rate(self):
        return self.nightly_rate

    def get_promo_txt(self):
        return self.promo_txt

    def get_deal_value(self):
        return self.deal_value

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_deal_type(self):
        return self.deal_type

    def get_all_attributes(self):
        return self.get_hotel_name(), self.get_nightly_rate(), self.get_promo_txt(), self.get_deal_value(), self.get_deal_type(), self.get_start_date(), self.get_end_date()

class Reservation:
    """
    This class is for a reservation to be made. This has following attributes:
    hotel_name   : Name of the hotel
    checkin_date : Date to check in
    num_stay_days: Number of days for stay
    """

    def __init__(self, hotel_name, checkin_date, num_stay_days):
        self.hotel_name = hotel_name
        self.checkin_date = dparser.parse(checkin_date)
        self.num_stay_days = int(num_stay_days)

    def get_checkin_date(self):
        return self.checkin_date

    def get_hotel_name(self):
        return self.hotel_name

    def get_num_stay_days(self):
        return self.num_stay_days

    def get_all_attributes(self):
        return self.get_hotel_name(), self.get_checkin_date(), self.get_num_stay_days()

def check_reservation_parameters(hotel_name, checkin_date, num_stay_days):
    try:
        datecheck.strptime(checkin_date, "%Y-%m-%d")
    except ValueError as err:
        print "Check-in date invalid."
        print err
        sys.exit(0)

    if not hotel_name.strip():
        raise BlankValues(0, "Hotel Name")

    if int(num_stay_days) < 1:
        raise NegativeStay(num_stay_days)


def process_command_line_args(args):
    """
    This function processes command line arguments
    It returns the file_name and a reservation instance
    """
    if len(args) == 5:
        program_name, file_name, hotel_name, checkin_date, num_stay_days = args
    else:
        try:
            raise InvalidCommandLine()
        except InvalidCommandLine:
            print "Specify the file name, hotel name, checkin date and number of days of stay separated by spaces. \n" +\
                  "Correct format: python HotelDeals.py <file_name> \"<hotel_name>\" <checkin date> <number of days>\n" +\
                  "Example: > python HotelDeals.py ./deals.txt \"Hotel CommonWealth\" 2014-06-30 3"
        sys.exit(0)

    try:
        int(num_stay_days)
    except ValueError as err:
        print 'The stay days should be a number greater than 0'
        print err
        sys.exit(0)


    check_reservation_parameters(hotel_name, checkin_date, num_stay_days)
    reservation = Reservation(hotel_name, checkin_date, num_stay_days)
    return file_name, reservation

def check_blank_values(row_number, hotel_name, nightly_rate, promo_txt, deal_value, deal_type, start_date, end_date):
    if not hotel_name:
        raise BlankValues(row_number, "Hotel Name")

    if not nightly_rate:
        raise BlankValues(row_number, "Nightly Rate")

    if not promo_txt:
        raise BlankValues(row_number, "Promotion Text")

    if not deal_value:
        raise BlankValues(row_number, "Deal Value")

    if not deal_type:
        raise BlankValues(row_number, "Deal Type")


    if not start_date:
        raise BlankValues(row_number, "Start Date")

    if not end_date:
        raise BlankValues(row_number, "End Date")

def check_values_of_files(row_number, hotel_name, nightly_rate, promo_txt, deal_value, deal_type, start_date, end_date):

    check_blank_values(row_number, hotel_name, nightly_rate, promo_txt, deal_value, deal_type, start_date, end_date)

    #The deal value can never be positive or zero
    if int(deal_value) >= 0:
        raise DealValue(row_number, deal_value)
    #Deal type can be only the ones specified
    if deal_type not in Constants.set_possible_deal_types:
        raise DealType(row_number, deal_type)
    #Date format is YYYY-MM-DD
    try:
        datecheck.strptime(start_date, "%Y-%m-%d")
    except ValueError as err:
        print "Start date invalid, row number: ", row_number
        print err
        sys.exit(0)

    try:
        datecheck.strptime(end_date, "%Y-%m-%d")
    except ValueError as err:
        print "End date invalid, row number: ", row_number
        print err
        sys.exit(0)

    #Start date cannot be after than the end date value
    if dparser.parse(start_date) > dparser.parse(end_date):
        raise InvalidSequence(row_number, start_date, end_date)


def populate_hotel_deals_from_file(file_name, dict_hotel_deals):
    """
        This function reads a csv file and populates a dictionary of hotel deal objects
        key: hotel_name
        value: list of the hotel deal objects for that hotel name
        return: dict_hotel_name_checkin_date
    """
    try:
        with open(file_name, 'rb') as deals_file:
            dealreader = csv.reader(deals_file, delimiter=',', quotechar='|')
            row_number = 1
            try:
                for hotel_name, nightly_rate, promo_txt, deal_value, deal_type, start_date, end_date in dealreader:
                    check_values_of_files(row_number, hotel_name, nightly_rate, promo_txt, deal_value, deal_type, start_date, end_date)
                    row_number += 1
                    hotel_deal = HotelDeals(hotel_name, nightly_rate, promo_txt, deal_value, deal_type, start_date, end_date)
                    dict_hotel_deals[hotel_name].append(hotel_deal)
            except ValueError as err:
                print "Row number", row_number, "has invalid number of columns in file", file_name
                print err
                sys.exit(0)
            return dict_hotel_deals

    except IOError as e:
        print "Check the file path or file exists."
        print "I/O error({0}): {1}".format(e.errno, e.strerror)





def populate_list_promo_text(list_hotel_deals, list_promo_text, reservation):
    for number, hotel_deal in enumerate(list_hotel_deals):
        if reservation.get_checkin_date() >=hotel_deal.get_start_date():
            if reservation.get_checkin_date() <hotel_deal.get_end_date():
                if hotel_deal.get_deal_type() == Constants.REBATE_3PLUS:
                    #This rebate is only applicable if stay is for more than three days
                    if reservation.get_num_stay_days() >= 3:
                        list_promo_text.append(hotel_deal.get_promo_txt())
                else:
                    list_promo_text.append(hotel_deal.get_promo_txt())


def print_list_of_promos(dict_hotel_deals, reservation):
    reservation_hotel_name = reservation.get_hotel_name()
    list_promo_text = []
    if reservation_hotel_name in dict_hotel_deals:
        list_hotel_deals = dict_hotel_deals[reservation_hotel_name]
        if list_hotel_deals:
            populate_list_promo_text(list_hotel_deals, list_promo_text, reservation)

    if not list_promo_text:
        print "no deal available"
    else:
        for promo_text in list_promo_text:
            print promo_text

def main():
    file_name, reservation = process_command_line_args(sys.argv)
    dict_hotel_deals = defaultdict(list)
    populate_hotel_deals_from_file(file_name, dict_hotel_deals)
    print_list_of_promos(dict_hotel_deals, reservation)

if __name__ == "__main__":
    main()