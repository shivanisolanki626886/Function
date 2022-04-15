def fun(num):
    i=0
    d=[]
    while i<len(num):
        if num[i] not in d:
            d.append(num[i])
        i=i+1
    print(d)
fun([1,2,3,3,3,3,4,5])