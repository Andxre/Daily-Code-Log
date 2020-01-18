'''
1/17/2020
Simple Linked List implementation in python
'''

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
       node = Node(data)
       if (self.head == None):
           self.head = node
       else:
          tmp = self.head
          while (tmp.next != None):
              tmp = tmp.next
          tmp.next = node



    def print(self):
        if (self.head == None):
            print("The list is empty")
            return
        tmp = self.head
        while (tmp != None):
            print(tmp.val, end="->")
            tmp = tmp.next


def main():
  ll = LinkedList()
  for i in range(1, 100):
    ll.add(i)
  ll.print()


main()




