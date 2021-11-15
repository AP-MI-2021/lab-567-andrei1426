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


