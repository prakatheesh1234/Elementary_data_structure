

class stack:

    def __init__(self):
        self.items=[]
    def push(self,data):
#        print(self.items)
        self.items.append(data)
        return self.items
    def pop(self):
        return self.items.pop()
    
    def isempty(self):
        if self.items == []:
            return True
        else:
            return False
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
    
a=stack()


#to push the elements into stack
a.push(2)

a.push(3)

a.push(4)
a.push(5)

a.push(6)

print(a.push(7))

#to pop the elemnet out
print(a.pop())
print(a.pop())

#to cheak the element is empty or not
print(a.isempty())

#to cheak the size of stack

print(a.size())

#to access the last element


print(a.peek())
