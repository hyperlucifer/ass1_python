# write a program to implement the concept to implement queue using list
# last in first out

class queue:
    def __init__(self) -> None:
        self.q=[]
    def insert(self,data):
        return self.q.append()
    def pop1(self):
        if(len(self.q)<=0):
            print("the queue is empty")
        else:
            return self.q.pop(0)
    def peek(self):
        if(len(self.q)<=0):
            print("the queue is empty")
        else:
            print(self.q[0])

q=queue()
