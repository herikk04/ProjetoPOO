import agenda, court, reservation, user
import pandas as pd


def main():

    ## INICIALIZAR LOCATÁRIO --> COM SUAS QUADRAS
    locator = user.Locator("Robson", "robson@email.com", "62989898989", 3)

    ## INICIALIZAR USUÁRIO

    ## FAZER RESERVA

    ## CANCELAR RESERVA
    print(pd.DataFrame(agenda.Agenda.courtAgendaData))
    print(pd.DataFrame(court.Court.courtReservationData))
    print(pd.DataFrame(user.User.userData))



if __name__ == '__main__':
    main()
