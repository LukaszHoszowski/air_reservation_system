from pprint import pprint

from planes import *
from flight import Flight
from helpers import *


def make_flights():
    f = Flight('BA123', Boeing737())
    # print(f.get_airlines())
    # print(f.get_number())
    # print(f.get_airplane_model())
    #
    # b = Boeing737()
    # print(b.num_seats())
    #
    # a = AirbusA370()
    # print(a.num_seats())

    f.allocate_passenger('Lech K', '1A')
    f.allocate_passenger('Jarosław K', '1B')
    f.allocate_passenger('Pawel K', '1C')
    f.relocate_passenger('1C', '24G')

    print(f.num_empty_seats())

    f.print_cards(card_printer)

    # pprint(f.seating_plan)


if __name__ == '__main__':
    make_flights()
