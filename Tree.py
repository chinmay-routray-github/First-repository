class Treenode:
    def __init__(self,val):
        self.val=val
        self.parent=None
        self.child=[]

    def add_child(self,val):
        val.parent=self
        self.child.append(val)

    def show(self):
        x=self.get_level()
        if(self.parent==None):
            print(x*'  ',self.val)
        else:
            print(x*'  ','|__',self.val)
        for ch in self.child:
            ch.show()
        return

    def get_level(self):
        lev=0
        tmp=self
        while(tmp.parent!=None):
            tmp=tmp.parent
            lev+=1
        return lev

t=Treenode(100)
a=Treenode(95)
b=Treenode(90)
c=Treenode(80)
t.add_child(a)
t.add_child(b)
t.add_child(c)
a.add_child(Treenode(1))
a.add_child(Treenode(2))
a.add_child(Treenode(3))
b.add_child(Treenode(11))
b.add_child(Treenode(22))
b.add_child(Treenode(33))
c.add_child(Treenode(41))
c.add_child(Treenode(31))
c.add_child(Treenode(51))
print(a.parent)
t.show()

