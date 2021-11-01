from Domain.obiect import get_nume, creeaza_obiect, get_id, get_descriere, get_pret, get_locatie


def schimbare_locatie(locatie_initiala, locatie_noua, lista):
    """
    muta toate obiectele dintr-o locatie in alta
    :param locatie_initiala: locatia initiala
    :param locatie_noua:  locatia unde o sa punem obiectele
    :param lista: lista de obiecte
    :return: lista in care obiectele din locatia initial o sa se afle in noua locatie
    """
    lista_noua = []
    for obiect in lista:
        if locatie_initiala in get_locatie(obiect):
            obiect_nou = creeaza_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect),
                get_pret(obiect),
                locatie_noua
            )
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def schimbare_descriere_dupa_pret(pret_comparat, str_concat, lista):
    """
    schimba descrierea la toate obiectele cu pret mai mare decat pret_comparat
    :param pret_comparat: valoarea cu care sunt comparate toate preturile
    :param str_concat:  stringul concatenat
    :param lista: lista de obiecte
    :return: lista in care descrierea obiectelor cu prețul mai mare decât o valoare citită este modificata
    """
    lista_noua = []
    for obiect in lista:
        if pret_comparat < get_pret(obiect):
            obiect_nou = creeaza_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect)+str_concat,
                get_pret(obiect),
                get_locatie(obiect)
            )
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua