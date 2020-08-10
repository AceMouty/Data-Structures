
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_val):
        self.next = next_val

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head is None

    def add_node(self, value):

        new_node = Node(value)

        # Will insert to our list no matter if its null or not
        if self.head is None and self.tail is None:
            self.tail = new_node
        
        new_node.set_next(self.head)
        self.head = new_node
    
    def get_size(self):
        current = self.head
        count = 0

        while current is not None:
            current = current.get_next()
            count += 1
        return count

    def add_to_tail(self, value):
        
        # 1. Create the Node from value passed
        new_node = Node(value)

        # check if the list is empty
        if self.tail == None and self.head == None:
            # Set new node to be the tail and the head
            self.head = new_node
            self.tail = new_node
        else:
            # 2. Set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)

            # 3. Reassign  self.tail to refer to the new Node
            self.tail = new_node
    
    def remove_from_tail(self):

       # if list is empty
        if self.head is None and self.tail is None:
           return
        
        # Else if not empty traverse the list
        current_node = self.head
        
        while current_node.next is not self.tail:
            current_node = current_node.get_next()
        
        self.tail = None
        self.tail = current_node
        

    def add_to_head(self, value):
        new_node = Node(value)

        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = new_node
            new_node.next = old_head
    
    def remove_head(self):

        # Is the list empty
        if self.head is None and self.tail is None:
            return

        # what if we only have a single value in the list?
        value = self.head.get_value()

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            
        return value
    
    def contains(self, value):
        current_node = self.head
        found = False
        found_value = None

        while current_node is not None and found is not False:
            if current_node.get_value() == value:
                found = True
                found_value = current_node.get_value()
            else:
                current_node = current_node.get_next()
        
        if found_value is not None:
            return found_value
        
        return found
    
    def get_max(self):
        current = self.head
        max_value = 0

        while current != None:
            if current.get_value() > max_value:
                max_value = current.get_value()
            else:
                current = current.get_next()

        if max_value != 0:
            return max_value

        return None


    
ll = LinkedList()
print(ll.isEmpty())
ll.add_node(23)
ll.add_to_tail(24)
ll.add_to_tail(25)
ll.add_to_tail(26)
print(ll.contains(24))
print(ll.get_max())