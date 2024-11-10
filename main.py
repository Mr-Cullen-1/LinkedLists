from functions import Node, LinkedList

llist = LinkedList()

llist.head = Node('Monday')
second = Node("Tuesday")
third = Node("Wednesday")

llist.head.next = second
second.next = third

# llist.printList()

llist.push("Sunday")
# llist.printList()

llist.insertAfter(llist.head.next.next, "Another Tuesday")
llist.printList()