class LinearProbing:
    def __init__(self,size):
        self.M = size            # M = 테이블크기
        self.a = [None] * size   # a = 해시테이블
        self.d = [None] * size   # d = 데이터 저장용 

    def hash(self,key):
        return key % self.M

    def put(self,key,data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                return                  # while문에서 return을 받으면 탈출할 수 있다
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j) % self.M
            if i == initial_position:
                break
    
    def get(self,key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + j) % self.M
            j += 1
            if i == initial_position:    # 한바퀴 돌았음(실패)
                return None
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)),' ',end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ',end='')
        print()
