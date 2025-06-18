
# Press the green button in the gutter to run the script.
class Stack:
   def __init__(self,size):
       self.size=size
       self.container = [None]*size #[None, None, None, None, None]
       self.topIndex= -1   # topIndex =  -1

   def push(self,item):
       if self.isFull():
           print("Stack Overflow! Cannot push the item in the stack!")
       else:
           self.topIndex += 1
           self.container[self.topIndex] = item
   def pop(self):
       if self.isEmpty():
           print("Stack Underflow! Cannot pop the item in the stack!")
           return None
       else:
           item = self.container[self.topIndex]
           self.topIndex -= 1
           return item

   def isFull(self):
       return self.topIndex == self.size-1

   def isEmpty(self):
       return self.topIndex == -1

   def getTopIndex(self):
       return self.topIndex
   def getContainer(self):
       return self.container


if __name__ == '__main__':
    s=Stack(5)
    s.push("A")
    s.push("B")
    s.pop()
    s.push("C")
    s.push("D")
    s.pop()
    s.push("E")

    print("The value of topIndex is "+str(s.getTopIndex()))
    print(s.getContainer())



