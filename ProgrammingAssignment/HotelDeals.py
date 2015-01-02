__author__ = 'pratik'
import sys
import re
import csv

class HotelDeals:

    def __init__(self):
        pass

    def input(self, args):
        print "take input"
        if len(args) >= 4:
            print str(args)



def process_command_line_args(args):
    print 'Number of arguments:', len(args), 'arguments.'
    print 'Argument List:', str(args)
    print args




def process_input(input_string):
    hotel_name = re.findall(r'\"(.+?)\"', input_string)
    date_value = re.findall("([0-9]{4}\-[0-9]{2}\-[0-9]{2})", input_string)
    print "Hotel Name: ", hotel_name, "Date: ", date_value
    if not hotel_name:
        print "Hotel name incorrect. Please enter as \"<hotel_name>\". " \
              "Quotation marks are required around the hotel name"

    if not date_value:
        print "Date format incorrect. Please enter in form <YYYY-MM-DD>"

    return hotel_name, date_value

def read_csv_file(file_name):
    with open('filename', 'rb') as deals_file:
        dealreader = csv.reader(deals_file, delimiter=' ', quotechar='|')
        for row in dealreader:
            print ','.join(row)








def main():
    print "in main"

    process_command_line_args(sys.argv)
    hm = HotelDeals()









if __name__ == "__main__": main()