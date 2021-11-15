from Domain.obiect import get_locatie, get_pret, get_descriere,get_id
from Logic.CRUD import adauga_obiect, get_by_id
from Logic.functionalitate import schimbare_locatie, schimbare_descriere_dupa_pret, max_pret_fiecare_locatie,sum_pret_fiecare_locatie,sortare_dupa_pret


def test_schimbare_locatie():
    lista = []
    lista = adauga_obiect("1", "carte", "desc1", 12, "arad", lista)
    lista = adauga_obiect("2", "caiet", "desc2", 12, "alba", lista)
    lista = adauga_obiect("3", "creion", "desc3", 12, "cluj", lista)

    lista = schimbare_locatie("alba", "cluj", lista)

    assert get_locatie(get_by_id("1", lista)) == "arad"
    assert get_locatie(get_by_id("2", lista)) == "cluj"
    assert get_locatie(get_by_id("3", lista)) == "cluj"


def test_schimbare_descriere_dupa_pret():
    lista = []
    lista = adauga_obiect("1", "carte", "desc1", 12, "arad", lista)
    lista = adauga_obiect("2", "caiet", "desc2", 100, "alba", lista)
    lista = adauga_obiect("3", "creion", "desc3", 34, "cluj", lista)

    lista = schimbare_descriere_dupa_pret(50, "_concatenat", lista)

    assert get_descriere(get_by_id("1", lista)) == "desc1"
    assert get_descriere(get_by_id("2", lista)) == "desc2_concatenat"
    assert get_descriere(get_by_id("3", lista)) == "desc3"


def test_max_pret_fiecare_locatie():
    lista = []
    lista = adauga_obiect("1", "carte", "desc1", 12, "arad", lista)
    lista = adauga_obiect("2", "caiet", "desc2", 100, "arad", lista)
    lista = adauga_obiect("3", "creion", "desc3", 34, "cluj", lista)
    rezultat = max_pret_fiecare_locatie(lista)

    assert rezultat["arad"] == 100
    assert rezultat["cluj"] == 34


def test_sum_pret_fiecare_locatie():
    lista = []
    lista = adauga_obiect("1", "carte", "desc1", 12, "arad", lista)
    lista = adauga_obiect("2", "caiet", "desc2", 100, "arad", lista)
    lista = adauga_obiect("3", "creion", "desc3", 34, "cluj", lista)
    rezultat = sum_pret_fiecare_locatie(lista)

    assert rezultat["arad"] == 112
    assert rezultat["cluj"] == 34


def test_undo_redo():
    undo_list = []
    redo_list = []
    lista = []
    lista = adauga_obiect("1", "carte", "desc1", 12, "arad", lista)
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_obiect("2", "caiet", "desc2", 100, "arad", lista)
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_obiect("3", "creion", "desc3", 34, "cluj", lista)
    undo_list.append(lista)
    redo_list.clear()

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is  None

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert get_by_id("1", lista) is None

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0

    lista = adauga_obiect("1", "carte", "desc1", 12, "arad", lista)
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_obiect("2", "caiet", "desc2", 100, "arad", lista)
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_obiect("3", "creion", "desc3", 34, "cluj", lista)
    undo_list.append(lista)
    redo_list.clear()

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 3

    redo_list.append(lista)
    lista = undo_list.pop()

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2
    assert get_by_id("2", lista) is not None

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 3
    assert get_by_id("3", lista) is not None

    redo_list.append(lista)
    lista = undo_list.pop()

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None

    lista = adauga_obiect("4", "stilou", "desc4", 192, "cluj", lista)
    undo_list.append(lista)
    redo_list.clear()

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("4", lista) is None

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert get_by_id("1", lista) is None

    undo_list.append(lista)
    lista = redo_list.pop()

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2