from Logic.CRUD import adauga_obiect
from Tests.test_all import run_all_tests
from UI.console import run_menu
from UI.command_line_console import main_line


def main():
    run_all_tests()
    lista = []
    lista = adauga_obiect("1", "carte", "desc1", 12, "arad", lista)
    lista = adauga_obiect("2", "caiet", "desc2", 100, "arad", lista)
    lista = adauga_obiect("3", "creion", "desc3", 34, "cluj", lista)
    run_menu(lista)

main()