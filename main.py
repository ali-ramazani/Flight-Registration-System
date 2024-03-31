from flight import *
from aircraft import * 
from pprint import pprint as pp
from boarding_pass_printer import console_card_printer 

def main():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319",
    num_rows=22, num_seats_per_row=6))
    f.allocate_seat("12A", "Ali Ramazani")
    f.allocate_seat("1B", "Zaki Ayoubi")
    pp(f._seating)
    f.make_boarding_cards(console_card_printer)   

if __name__ == "__main__":
    main()