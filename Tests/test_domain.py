from Domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie


def test_obiect():
    obiect = creeaza_obiect("1", "carte", "verde", 200, "cluj")

    assert get_id(obiect) == "1"
    assert get_nume(obiect) == "carte"
    assert get_descriere(obiect) == "verde"
    assert get_pret(obiect) == 200
    assert get_locatie(obiect) == "cluj"
