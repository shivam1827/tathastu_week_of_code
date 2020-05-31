n=int(input())
for i in range(2*n):
    if(i<n):
        k=str(n-i)
        print(k+('*'+k)*(n-1-i))
    else:
        k=str(i-n+1)
        print(k+('*'+k)*(i-n))
