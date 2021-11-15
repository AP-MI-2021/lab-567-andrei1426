def creeaza_obiect(id, nume, descriere , pret, locatie):
    '''
    creaza un dictiionar ce reprezinta un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param preț: float
    :param locatie: string
    :return: un dictionar ce contine un obiect
    '''
    return [
         id,
         nume,
         descriere,
         pret,
        locatie
    ]

def get_id(obiect):
    '''
    da id-ul unei prajituri
    :param prajitura: dictionar ce contine o prajitura
    :return: id-ul prajiturii
    '''
    return obiect[0]

def get_nume(obiect):
    return obiect[1]

def get_descriere(obiect):
    return obiect[2]

def get_pret(obiect):
    return obiect[3]

def get_locatie(obiect):
    return obiect[4]


def toString(obiect):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret(obiect),
        get_locatie(obiect)
    )