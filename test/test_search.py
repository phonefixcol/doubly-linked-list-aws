from app.dll import DoublyLinkedList


def test_search_existing():
    dll = DoublyLinkedList()

    dll.insert_tail(1)
    dll.insert_tail(2)
    dll.insert_tail(3)

    assert dll.search(2) == 1


def test_search_non_existing():
    dll = DoublyLinkedList()

    dll.insert_tail(1)
    dll.insert_tail(2)

    assert dll.search(5) == -1