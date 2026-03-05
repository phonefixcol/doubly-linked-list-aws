from app.dll import DoublyLinkedList


def test_remove_duplicates():

    dll = DoublyLinkedList()

    dll.insert_tail(1)
    dll.insert_tail(2)
    dll.insert_tail(2)
    dll.insert_tail(3)

    dll.remove_duplicates()

    assert dll.size() == 3
    assert dll.search(2) == 1