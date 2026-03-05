from app.dll import DoublyLinkedList


def test_insert_head():
    dll = DoublyLinkedList()

    dll.insert_head(10)
    dll.insert_head(20)

    assert dll.head.value == 20
    assert dll.tail.value == 10
    assert dll.size() == 2


def test_insert_tail():
    dll = DoublyLinkedList()

    dll.insert_tail(1)
    dll.insert_tail(2)

    assert dll.head.value == 1
    assert dll.tail.value == 2
    assert dll.size() == 2