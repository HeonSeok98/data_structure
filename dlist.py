# 이중 연결 리스트
class DList:
    class Node:
        def __init__(self,item,prev,link):
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,self.head,None)   # tail 에서 next 연결
        self.head.next = self.tail                   # next 에서 tail 연결 
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_before(self,p,item):  # t > n > p
        t = p.prev
        n = self.Node(item,t,p)
        p.prev = n                   # p > n
        t.next = n                   # t > n
        self.size += 1

    def insert_after(self,p,item):   # p > n > t
        t = p.next
        n = self.Node(item,p,t)
        t.prev = n                   # n > t
        p.next = n                   # p > n
        self.size += 1

    def delete(self,x):         # x 삭제  f > x > r
        f = x.prev              # f > x
        r = x.next              # x > r
        f.next = r              # f > r
        r.prev = f              # f > r
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")

        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item,"<> ",end="")

                else:
                    print(p.item)
                p = p.next

class EmptyError(Exception):
    pass

