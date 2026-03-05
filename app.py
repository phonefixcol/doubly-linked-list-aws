from fastapi import FastAPI

app = FastAPI()

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_head(self, value):
        node = Node(value)

        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.length += 1

    def insert_tail(self, value):
        node = Node(value)

        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1

    def search(self, value):
        current = self.head
        index = 0

        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1

    def size(self):
        return self.length

    def remove_duplicates(self):
        seen = set()
        current = self.head

        while current:
            if current.value in seen:
                prev = current.prev
                nxt = current.next

                if prev:
                    prev.next = nxt
                if nxt:
                    nxt.prev = prev

                if current == self.tail:
                    self.tail = prev

                self.length -= 1
            else:
                seen.add(current.value)

            current = current.next


dll = DoublyLinkedList()

@app.post("/insert-head/{value}")
def insert_head(value:int):
    dll.insert_head(value)
    return {"size": dll.size()}

@app.post("/insert-tail/{value}")
def insert_tail(value:int):
    dll.insert_tail(value)
    return {"size": dll.size()}

@app.get("/search/{value}")
def search(value:int):
    return {"index": dll.search(value)}

@app.post("/remove-duplicates")
def remove_duplicates():
    dll.remove_duplicates()
    return {"size": dll.size()}

@app.get("/size")
def size():
    return {"size": dll.size()}