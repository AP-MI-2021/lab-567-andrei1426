from Domain.obiect import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect, get_by_id, sterge_obiect, modifica_obiect


def test_adauga_obiect():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)

    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_nume(get_by_id("1", lista)) == "carte"
    assert get_descriere(get_by_id("1", lista)) == "verde"
    assert get_pret(get_by_id("1", lista)) == 100
    assert get_locatie(get_by_id("1", lista)) == "cluj"


def test_sterge_obiect():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    lista = adauga_obiect("2", "caiet", "rosu", 500, "cluj", lista)

    lista = sterge_obiect("1", lista)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

    lista = sterge_obiect("3", lista)

    assert len(lista) == 1
    assert get_by_id("2", lista) is not None


def test_modifica_obiect():
    lista = []
    lista = adauga_obiect("1", "carte", "verde", 100, "cluj", lista)
    lista = adauga_obiect("2", "caiet", "rosu", 500, "cluj", lista)

    lista = modifica_obiect("1", "pix", "albastru", 2, "arad", lista)

    obiect_modificat = get_by_id("1", lista)
    assert get_id(obiect_modificat) == "1"
    assert get_nume(obiect_modificat) == "pix"
    assert get_descriere(obiect_modificat) == "albastru"
    assert get_pret(obiect_modificat) == 2
    assert get_locatie(obiect_modificat) == "arad"
