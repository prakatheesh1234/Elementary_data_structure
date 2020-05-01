#using linkedlist



class node:
   def __init__(self,data) :
    self.data=data
    self.next=None
    self.pre=None


class queue_list:
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self,data):
        if self.head == None:
            self.head=node(data)
            self.tail=self.head
        else:
            self.tail.next=node(data)
            self.tail.next.pre=self.tail
            self.tail =self.tail.next
    def dequeue(self):
        if self.head == None:
            return False
        else:
            enqueue=self.head.data
            self.head= self.head.next
            return enqueue
    def print_lst(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
            
            
            

        
        
        
s=queue_list()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(5)
s.enqueue(7)
a=s.enqueue(8)
#s.printqueue()
#print(s.enqueue(9))
#
#print(s.dequeue())
#print(s.dequeue())
#print(s.dequeue())
#print(s.dequeue())
#print(s.dequeue())
#print(s.dequeue())
s.print_lst()