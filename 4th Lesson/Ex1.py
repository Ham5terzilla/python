from random import *
lst = [random()*100 for i in range(1000)]
lst.sort()
print(lst[::1])
print(lst[::-1])
print(lst[2::-1])
llst = tuple(lst)
print(llst)
print(lst.__sizeof__()/1024/1024)
print(llst.__sizeof__()/1024/1024)
print(lst.__sizeof__()/llst.__sizeof__())
