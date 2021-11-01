from Logic.CRUD import adauga_obiect
from Tests.test_all import run_all_tests
from UI.console import run_menu
from UI.command_line_console import main_line


def main():
    run_all_tests()
    lista = []
    main_line(lista)

main()