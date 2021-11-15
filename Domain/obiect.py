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
    return {
         "id": id,
         "nume": nume,
         "descriere": descriere,
         "pret": pret,
        "locatie": locatie
    }

def get_id(obiect):
    '''
    da id-ul unei prajituri
    :param prajitura: dictionar ce contine o prajitura
    :return: id-ul prajiturii
    '''
    return obiect["id"]

def get_nume(obiect):
    return obiect["nume"]

def get_descriere(obiect):
    return obiect["descriere"]

def get_pret(obiect):
    return obiect["pret"]

def get_locatie(obiect):
    return obiect["locatie"]


def toString(obiect):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret(obiect),
        get_locatie(obiect)
    )