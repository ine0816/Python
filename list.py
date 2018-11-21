list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

print('list1:',list1)
print('list2:',list2)
print('list3:',list3,'\n')

print ("list1[0]: ", list1[0])

print("list2[1:5]: ", list2[1:5])

print("Print list3:",list3)

print("Print list3 last number(list3[-1]): ",list3[-1],'\n')
del list3[-1]
print("Del list3 last number",list3,'\n')
list1.append('Baidu')
print("list1 增加Baidu 更新后的列表 : ", list1)
