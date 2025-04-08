class DoublyLinkedNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        newNode = DoublyLinkedNode(value)

        if self.head:
            self.head.previous = newNode
        self.head = newNode

        if not self.tail:
            self.tail = newNode

        return

    def apppend(self, value):
        newNode = DoublyLinkedNode(value)

        if not self.head:
            self.head = newNode
            self.tail = newNode

            return
        
        self.tail.next = newNode

        newNode.prev = self.tail

        self.tail = newNode

        return
    
    def delete(self, value):
        if not self.head:
            return None
        
        deletedNode = None
        currentNode = self.head

        while currentNode:
            if currentNode.value == value:
                deletedNode = currentNode

                if deletedNode == self.head:
                    self.head = deletedNode

                    if self.head:
                        self.head.prev = None

                    if deletedNode == self.tail:
                        self.tail = None
                elif deletedNode == self.tail:
                    self.tail = deletedNode.prev
                    self.tail.next = None
                else:
                    prevNode = deletedNode.prev
                    nextNode = deletedNode.next

                    prevNode.next = nextNode
                    nextNode.prev = prevNode

            currentNode = currentNode.next

        return deletedNode
    
    def find(self, value):
        if not self.head:
            return None
        
        currentNode = self.head

        while currentNode:
            if currentNode.value == value:
                return currentNode
            
            currentNode = currentNode.next

        return None