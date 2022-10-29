#DoublyLinkedList

class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None
    self.prev = None

class LL:
  def __init__(self):
    self.head = None


  def listprint(self):
    #O(n)
    printval = self.head
    while printval is not None:
      print(printval.data)
      printval = printval.next

  def insert(self,numb):
    #O(n)
    addval = self.head
    while addval.next is not None:
      addval = addval.next
    addval.next = Node(numb)
    addval.next.prev=addval

  def insertLeft(self,numb):
    #O(1)
    addval = self.head
    addval.prev=Node(numb)
    addval.prev.next=addval
    self.head=addval.prev
  

  def lengthOfList(self):
    #O(n)
    a=0
    addval = self.head
    while addval.next is not None:
      addval = addval.next
      a=a+1
    return a+1

  def deleteAtPos(self,pos):
    #O(n)
    lenn = self.lengthOfList()
    if(pos>lenn):
      print("The given position is bigger than the length of List")
    else:
      c = 0
      getval = self.head
      while(c is not pos):
        getval=getval.next
        c=c+1
      if(getval.next.next is not None):
        getval.next = getval.next.next
        getval.next.next.prev=getval
      else:
        getval.next = None
      
    
        

n1 = Node(0)
n2 = Node(20)
n3 = Node(30)

l1 = LL()
l1.head = n1
l1.insert(5)
l1.insert(10)
l1.insert(15)
l1.insertLeft(-5)
l1.insertLeft(-10)
l1.insertLeft(-15)
l1.deleteAtPos(1)
l1.listprint()
