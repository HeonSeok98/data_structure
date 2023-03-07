# 단순 연결 리스트
class SList:
    class Node:
        def __init__(self,item,link): # 노드 생성
            self.item = item
            self.next = link

    def __init__(self): # s (단순연결 리스트 자체)
        self.head = None # 리스트의 맨 앞자리를 의미 한다
        self.size = 0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_front(self,item):
        if self.is_empty():
            self.head = self.Node(item,None) # 빈 리스트 일 경우
        else:
            self.head = self.Node(item,self.head) # 뭔가 있는 리스트 일 경우
        self.size += 1
    
    def insert_after(self,item,p): # p 다음 칸에 삽입을 한다
        p.next = SList.Node(item,p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self,p):
        if self.is_empty():
            raise EmptyError('Underflow')
        t = p.next                          # p > t
        p.next = t.next
        self.size -= 1

    def search(self,target):
        p = self.head
        for k in range(self.size):
            if target == p.item: return k   # 검사단계
            p = p.next                      # 아닐 경우 다음거 호출
        return None

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item,'> ',end='')
            else:
                print(p.item)
            p = p.next

class EmptyError(Exception):
    pass
