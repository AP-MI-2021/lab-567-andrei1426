from Logic.CRUD import adauga_obiect, get_by_id


def test_undoredo():
#1
    undo_list = []
    redo_list = []
    lista = []
#2
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_obiect("1", "carte", "desc1", 12, "arad", lista)
#3
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_obiect("2", "caiet", "desc2", 100, "arad", lista)
#4
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_obiect("3", "creion", "desc3", 34, "cluj", lista)

#5
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 2
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is not None
    assert get_by_id("3", lista) is None
#6
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
#7
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert get_by_id("1", lista) is None
#8
    if len(undo_list) > 0:
         redo_list.append(lista)
         lista = undo_list.pop()
         assert len(lista) == 0
#9
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_obiect("1", "carte", "desc1", 12, "arad", lista)
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_obiect("2", "caiet", "desc2", 100, "arad", lista)
    undo_list.append(lista)
    redo_list.clear()

    lista = adauga_obiect("3", "creion", "desc3", 34, "cluj", lista)
#10
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 3
#11
    redo_list.append(lista)
    lista = undo_list.pop()

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
#12
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2
    assert get_by_id("2", lista) is not None
#13
    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 3
    assert get_by_id("3", lista) is not None
#14
    redo_list.append(lista)
    lista = undo_list.pop()

    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
#15
    undo_list.append(lista)
    redo_list.clear()
    lista = adauga_obiect("4", "stilou", "desc4", 192, "cluj", lista)
#16
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
#17
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 1
    assert get_by_id("1", lista) is not None
    assert get_by_id("4", lista) is None
#18
    redo_list.append(lista)
    lista = undo_list.pop()
    assert len(lista) == 0
    assert get_by_id("1", lista) is None
#19
    undo_list.append(lista)
    lista = redo_list.pop()

    undo_list.append(lista)
    lista = redo_list.pop()
    assert len(lista) == 2
#20
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2