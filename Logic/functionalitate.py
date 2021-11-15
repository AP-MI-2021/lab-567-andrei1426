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


def max_pret_fiecare_locatie(lista):
    """
    determina cel mai mare pret pr fiecare locatie din lista
    Args:
        lista: lista din care determinam preturile cele mai mari pt fiecare locatie

    Returns: un dictionare care cintine preturile maxime pt fiecare locatie din lista

    """
    rezultat={}
    for obiect in lista:
        locatie=get_locatie(obiect)
        pret=get_pret(obiect)
        if locatie not in rezultat or pret>rezultat[locatie]:
            rezultat[locatie] = pret
    return rezultat


def sum_pret_fiecare_locatie(lista):
    """
    determina suma preturilor pt fiecare locatie  din lista
    Args:
        lista: lista din care determinam suma pt fiecare locatie

    Returns: un dictionare care contine suma preturilor pt fiecare locatie din lista

    """
    rezultat={}
    for obiect in lista:
        locatie=get_locatie(obiect)
        pret=get_pret(obiect)
        if locatie not in rezultat:
            rezultat[locatie]=pret
        else:
            rezultat[locatie] += pret
    return rezultat


def sortare_dupa_pret(lista):
    """
    sorteaza lista dupa pret
    Args:
        lista: lista data

    Returns: lista sortata

    """
    return sorted(lista, key=lambda obiect: get_pret(obiect))