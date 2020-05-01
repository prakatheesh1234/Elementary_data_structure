#using linkedlist



class node:
   def __init__(self,data) :
    self.data=data
    self.next=None


class stack_list:
    def __init__(self):
        self.head=None
    
    def push(self,data):
        if self.head == None:
            self.head=node(data)
        else:
            new_node=node(data)
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        if self.head == None:
            return None
        else:
            pop = self.head.data
            
            self.head=self.head.next
            return pop
        
        
        
        
        
s=stack_list()
s.push(1)
s.push(2)
s.push(3)
s.push(5)
s.push(7)
s.push(8)
s.push(9)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
