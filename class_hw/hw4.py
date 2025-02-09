# compare high numbers in different lists

list1 = [1,4,88,3]
list2 = [1,4,66,7,3,4]

l1=0
l2=0
for n in list1 :
    if n in list1 == n in list2:
        continue
    if (n in list1) > (n in list2):
        l1+=1
        print(l1)
    else:
        l2+=1

if l1 > l2 :
    print("list 1 has more volume numbers")
else:
    print('list 2 has more volume numbers')
