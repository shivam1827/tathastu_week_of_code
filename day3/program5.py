n1=int(input('Enter size of list1'))
print('Enter element of first list seprating by space')
a1=list(map(int,input().split()))

n2=int(input('Enter size of list2'))
print('Enter element of second list seprating by space')
a2=list(map(int,input().split()))

l3=[]

for i in a1:
    if i  in a2:
        l3.append(i)
print(l3)
  
