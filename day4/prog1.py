n=int(input('enter the size of tuple'))

tu=tuple(map(int,input('enter element of tuple seprated by space:').split()))

e=int(input('enter the element to find it occurence:'))

print(tu.count(e))
