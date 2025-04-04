class LinkedNode:
    def __init__(self,value):
        self.value = value
        self.next = None





class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    


    def append(self,value):
        new_node = LinkedNode(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    


    def prepend(self,value):
        new_node = LinkedNode(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    


    
    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        
        new_node = LinkedNode(value)
        temp = self.head

        for i in range(index -1):
            if temp is None:
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        if new_node.next is None:
            self.tail = new_node

    



    def search(self,value):
        temp = self.head

        while temp:
            if temp.value == value:
                return True
            temp = temp.next

        return False
    
    



    def delete(self, value):
        if not self.head:
            return
        
        if self.head.value == value:
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            return
        
        temp = self.head
        while temp.next and temp.next.value != value:
            temp = temp.next

        if temp.next:
            if temp.next == self.tail:
                self.tail = temp
            temp.next = temp.next.next





    
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.insert(1, 15)  # Insert 15 at index 1
ll.traverse()  # Output: 5 -> 15 -> 10 -> 20 -> None
ll.delete(10)
ll.traverse()  # Output: 5 -> 15 -> 20 -> None
print(ll.search(15))  # Output: True
print(ll.search(100))  # Output: False