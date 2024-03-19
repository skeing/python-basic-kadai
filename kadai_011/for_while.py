# -*- coding: utf-8 -*-

array = ["水","金","地","火","木","土","天","海","冥"]

# for文
for _ in array:
    print(_)

# while文
#print(len(array))
num: int = 0

while(num != len(array)):
    print(array[num])
    num += 1
