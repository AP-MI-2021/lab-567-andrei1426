from Tests.test_CRUD import test_adauga_obiect, test_sterge_obiect, test_modifica_obiect
from Tests.test_domain import test_obiect
from Tests.test_functionalitati import test_schimbare_locatie, test_schimbare_descriere_dupa_pret,test_max_pret_fiecare_locatie,test_sum_pret_fiecare_locatie
from Tests.test__undo_redo import test_undoredo

def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_sterge_obiect()
    test_modifica_obiect()
    test_schimbare_locatie()
    test_schimbare_descriere_dupa_pret()
    test_max_pret_fiecare_locatie()
    test_sum_pret_fiecare_locatie()
    test_undoredo()
