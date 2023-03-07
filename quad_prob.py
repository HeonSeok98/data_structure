class QuadProbing:
    def __init__(self,size):
        self.M = size
        self.a = [None] * size
        self.d = [None] * size
        self.N = 0                       # N은 저장된 항목의 수

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
                self.N += 1
                return                  # while문에서 return을 받으면 탈출할 수 있다
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j*j) % self.M
            if i == initial_position:
                break
    
    def get(self,key):
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + j*j) % self.M
            j += 1
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)),' ',end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ',end='')
        print()