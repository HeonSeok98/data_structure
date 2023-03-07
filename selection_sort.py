def selection_sort(a):
    for i in range(0,len(a)-1):
        minimum = i
        for j in range(i,len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]

a = [54,88,77,93,17,49,10,17,77,11,31,22,44,17,20]
print(a)
selection_sort(a)
print(a)
