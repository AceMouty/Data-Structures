class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        # return de-refd node
        return self


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if type(value) == ListNode:
            new_node = value
        else:
            new_node = ListNode(value, None, None)

        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return new_node

    def add_to_tail(self, value):
        if type(value) is ListNode:
            new_node = value
        else:
            new_node = ListNode(value, None, None)

        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return new_node

    def remove_from_head(self):
        old_node = self.delete(self.head)
        return old_node

    def remove_from_tail(self):
        old_node = self.delete(self.tail)
        return old_node

    def move_to_front(self, node):
        old_node = self.delete(node)
        new_head = self.add_to_head(old_node)
        return new_head

    def move_to_end(self, node):
        old_node = self.delete(node)
        new_tail = self.add_to_tail(old_node)
        return new_tail

    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return node
        elif self.head == node:
            self.head = self.head.next
            return node.delete()
        elif self.tail == node:
            self.tail = self.tail.prev
            return node.delete()
        else:
            return node.delete()

    def get_max(self):
        if self.head is None:
            return None

        max_vlaue = self.head.value
        current = self.head
        while current:
            if current.value > max_vlaue:
                max_vlaue = current.value
            current = current.next
        return max_vlaue
