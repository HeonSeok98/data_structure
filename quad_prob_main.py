from quad_prob import QuadProbing
if __name__ == '__main__':
    t = QuadProbing(13)
    t.put(25,'grape')
    t.put(37,'apple')
    t.put(18,'banana')
    t.put(55,'cherry')
    t.put(22,'mango')
    t.put(35,'lime')
    t.put(50,'orange')
    t.put(63,'watermalon')
    print('탐색결과')
    print('50의 data = ',t.get(50))
    print('63의 data = ',t.get(63))
    print('해시테이블')
    t.print_table()    



