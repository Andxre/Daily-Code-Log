'''
1/17/2020
Simple Linked List implementation in python~
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

    def remove(self, data):
        if (self.head == None):
            return
        temp = self.head
        prev = None

        while (temp.val != data):
            prev = temp
            temp = temp.next
        if (temp.val == None):
            return
        else:
            prev.next = temp.next

    def print(self):
        if (self.head == None):
            print("The list is empty")
            return
        tmp = self.head
        while (tmp != None):
            print(tmp.val, end=" ")
            tmp = tmp.next
        print("\n")


def main():
  ll = LinkedList()
  for i in range(1, 10):
    ll.add(i)
  ll.print()
  ll.remove(2)
  ll.remove(3)
  ll.print()


main()




