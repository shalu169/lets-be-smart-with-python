# Linked list implemented using class and objects

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def __str__(self):
        return ('(' + str(self.data) + ')')


class LinkedList:

    def __init__(self):
        self.root = None
# traversing list
    def print_list(self):
        temp = self.root
        print(type(temp))
        while temp is not None:
            print(temp.data)
            temp = temp.next
#insert at begning
    def insert_at_begning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.root
        self.root = new_node
# insert at last
    def insert_at_last(self, new_data):
        new_node = Node(new_data)
        temp = self.root
        while temp:
            temp1 = temp
            temp = temp.next
        temp1.next = new_node
#delete from begning
    def delete_from_begning(self):
        self.root = self.root.next
# delete form last
    def delete_from_last(self):
        temp = temp1 = self.root
        while temp:
            temp2 = temp1
            temp1 = temp
            temp = temp.next
        temp2.next = temp1.next
# searching
    def searching(self, data):
        temp = self.root
        while temp:
            if temp.data == data:
                return "successful"
            temp = temp.next
        else:
            return "unsuccessful"
llist = LinkedList()
llist.root = Node(12)
node2 = Node(13)
node3 = Node(24)
node4 = Node(34)
llist.root.next = node2
node2.next = node3
node3.next = node4
#print(llist.root)
#print(node2.data, node2.next)
#print(node3.data, node3.next)
#print(node4.data, node4.next)

# traverse
llist.print_list()

llist.insert_at_begning(90)
llist.print_list()
llist.insert_at_last(5)
llist.print_list()
llist.delete_from_begning()
llist.print_list()
llist.delete_from_last()
llist.print_list()
print(llist.searching(12))
print(llist.searching(112))
#print(str(node2))  # just to see use if __str__() function in class Node


