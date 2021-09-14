class Node:
    def __init__(self,data):
        self.data=data
        self.nxt=None


class Linked_list:
    def __init__(self):
        self.head=None

    def show(self):
        if(self.head==None):
            print('List is empty')
        else:
            l=[]
            point=self.head
            while(point.nxt!=None):
                l.append(point.data)
                point=point.nxt
            l.append(point.data)
            print(*l,sep='-->')

    def add_at_end(self,val):
        if(self.head==None):
            self.head=val
        else:
            temp=self.head
            while(temp.nxt!=None):
                temp=temp.nxt
            temp.nxt=val

    def add_at_start(self,val):
        if(self.head==None):
            self.head=val
        else:
            temp=self.head
            self.head=val
            val.nxt=temp

    def remove_last(self):
        if(self.head==None):
            print('List is empty')
        else:
            temp=self.head
            while(temp.nxt!=None):
                prev=temp
                temp=temp.nxt
            prev.nxt=None

    def remove_first(self):
        if(self.head==None):
            print('List is empty')
        else:
            temp=self.head
            self.head=temp.nxt
            temp.nxt=None

    def find (self,val):
        if(self.head==None):
            print('List is empty')
        else:
            temp=self.head
            i=0
            while(temp):
                if(temp.data==val):
                    print(i)
                    return True
                    break
                temp=temp.nxt
                i+=1
            return False

    def list_len(self):
        k=0
        temp=self.head
        while(temp):
            temp=temp.nxt
            k+=1
        return k

    def insert(self,indx,val):
        if (self.head==None):
            Linked_list.add_at_start(self,val)
        elif(indx<Linked_list.list_len(self)):
            k=0
            temp=self.head
            while(k!=indx-1):
                temp=temp.nxt
                k+=1
            key=temp.nxt
            temp.nxt=val
            val.nxt=key
        else:
            print('Index out of bound')

    def delete(self,indx):
        if(self.head==None):
            print('List is already empty')
        elif(indx<Linked_list.list_len(self)and indx!=0):
            k=0
            temp=self.head
            while(k!=indx):
                prev=temp
                temp=temp.nxt
                k+=1
            key=temp.nxt
            prev.nxt=key
            temp.nxt
        elif(indx==0):
            Linked_list.remove_first(self)
        else:
            print('Index out of bound')

        
l_list=Linked_list()
l_list.add_at_end(Node(5))
l_list.add_at_end(Node(15))
l_list.add_at_end(Node(25))
l_list.add_at_end(Node(35))
l_list.add_at_start(Node(25))
l_list.add_at_start(Node(15))
l_list.add_at_start(Node(5))
l_list.remove_last()
l_list.remove_first()
l_list.remove_last()
l_list.remove_first()
a=l_list.find(5)
print(a)
print(l_list.list_len())
l_list.show()
l_list.insert(2,Node(20))
l_list.delete(0)
l_list.remove_first()
l_list.remove_first()
l_list.remove_first()
l_list.insert(50,Node(47))
l_list.insert(50,Node(47))
l_list.show()




        

        
