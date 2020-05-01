

class stack:

    def __init__(self):
        self.items=[]
    def enqueue(self,data):
#        print(self.items)
        self.items.append(data)
        return self.items
    def dequeue(self):
        return self.items.pop(0)
    
    def isempty(self):
        if self.items == []:
            return True
        else:
            return False
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
    
    
a=stack()


#to enqueue the elements into queue
a.enqueue(2)

a.enqueue(3)

a.enqueue(4)
a.enqueue(5)

a.enqueue(6)

print(a.enqueue(7))


#to dequeue the elemnet out
print(a.dequeue())
print(a.dequeue())

#to cheak the queue is empty or not
print(a.isempty())

#to cheak the size of queue

print(a.size())

#to access the last element of queue


print(a.peek())
