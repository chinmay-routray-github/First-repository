class stack:
    def __init__(self):
        self.l=[]

    def show(self):
        print(*self.l,sep='-->')

    def push(self,val):
        self.l.append(val)
        print(val)
        return 
    
    def fof(self):
        print(self.l[-1])
        self.l.pop()
        return

    def stack_len(self):
        print(f'length={len(self.l)}')

    def indx(self,val):
        if val not in self.l:
            print('Value not in stack')
        else:
            print(f'Index is {self.l.index(val)}')

class que:
    def __init__(self):
        self.l=[]

    def show(self):
        print(*self.l,sep='-->')

    def push(self,val):
        self.l.insert(0,val)
        print(val)
        return 
    
    def fof(self):
        print(self.l[-1])
        self.l.pop()
        return

    def stack_len(self):
        print(f'length={len(self.l)}')

    def indx(self,val):
        if val not in self.l:
            print('Value not in queue')
        else:
            print(f'Index is {self.l.index(val)}')
           

s=stack()
s.push(5)
s.push(15)
s.push(25)
s.push(35)
s.push(45)
s.fof()
s.show()
s.stack_len()
s.indx(250)

q=que()
q.push(5)
q.push(15)
q.push(25)
q.push(35)
q.push(45)
q.fof()
q.show()
q.stack_len()
q.indx(250)
