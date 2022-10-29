#SinglyLinkedList

class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None

class LL:
  def __init__(self):
    self.head = None
    self.tail = None

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
    
  def insertBetter(self,numb):
    #O(1)
    if(self.tail is not None):
      self.tail.next=Node(numb)
      self.tail = self.tail.next
    elif(self.head is None):
      self.head=Node(numb)
      self.tail=self.head
    else:
      addval = self.head
      while addval.next is not None:
        addval = addval.next
      addval.next = Node(numb)
      self.tail=addval.next
    

  def deleteEnd(self):
    #O(n)
    delval = self.head
    while delval.next is not None:
      if(delval.next.next is None):
        delval.next = None
        self.tail=delval
      else:
        delval = delval.next
  #def deleteEndBetter(self):
    
  def deleteStart(self):
    #O(1)
    self.head = self.head.next

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
      else:
        getval.next = None
      
    
        

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

l1 = LL()
l1.head = n1
#l1.insert(20)
#l1.insert(30)
#l1.insert(40)
#l1.insert(50)
#l1.deleteEnd()
#l1.deleteStart()
#n1.next = n2
#n2.next = n3
l1.insertBetter(60)
l1.insertBetter(70)
l1.insertBetter(80)
#l1.deleteEnd()
#l1.deleteEnd()
l1.insertBetter(200)
l1.insertBetter(85)
l1.insertBetter(90)
l1.insertBetter(110)
l1.insertBetter(120)
l1.deleteAtPos(19)
l1.deleteAtPos(2)
l1.listprint()
k= l1.lengthOfList()
print(k)
