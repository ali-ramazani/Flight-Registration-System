


def make_flights():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319",
    num_rows=22, num_seats_per_row=6))
    f.allocate_seat("12A", "Ali Ramazani")
    f.allocate_seat("1B", "Zaki Ayoubi")
    pp(f._seating)
    f.make_boarding_cards(console_card_printer)