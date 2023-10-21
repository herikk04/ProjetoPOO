import agenda, court, reservation, user
import pandas as pd


def main():
    courtTest = court.Court("Basquete", "São Paulo", "100", "1 1 1 1 1 1 1 1 1 1", "1 1 1 1 1 1 1 1 1 1")
    a = int(input())

    match a:
        case 1:
            print(courtTest.getDetails())
            print(courtTest.courtID)
            courtTest.bookCourt("João", 1, 3, 5)
            print(courtTest.checkAvailability(3, 4, 6))
            print(courtTest.agenda.getAgenda(courtTest.courtID)) #### FALTA CORRIGIR PROBLEMA NA GRAVAÇÃO DE DADOS NA AGENDA


if __name__ == '__main__':
    main()
