import agenda, court, reservation, user
import pandas as pd


def main():
    courtTest = court.Court("Basquete", "São Paulo", "100","0 1 0 0 1 1 0 1", "0 1 0 0 0 0 1 1")
    a = int(input())

    match a:
        case 1:
            print(courtTest.getDetails())
            print(courtTest.id)
        case 2:
            courtTest.bookCourt("João", 3, 4, 5)
            print(courtTest.checkAvailability(3, 4, 6))


if __name__ == '__main__':
    main()
