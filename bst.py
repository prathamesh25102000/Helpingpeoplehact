# cook your dish here
class Bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key==None:
            self.key=data
        else:
            if data>self.key:
                if self.rchild:
                    self.rchild.insert(data)
                else:
                    self.rchild=Bst(data)
            else:
                if data < self.key:
                    if self.lchild:
                        self.lchild.insert(data)
                    else:
                        self.lchild = Bst(data)
    def search(self,data):
        if self.key==data:
            return 1
        else:
            if data>self.key:
                if self.rchild:
                    self.rchild.search(data)
                else:
                    return -1
            else:
                if self.lchild:
                    self.lchild.search(data)
                else:
                    return -1
root=Bst(None)
root.insert(10)
root.insert(5)
root.insert(11)
print(root.search(11))
print(root.key)
