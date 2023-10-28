n=int(input("Enter the number of elements of the fibonnaci series that has to be displayed:"))
i=0
j=1
c=2
sum=[0,1]
while(c<n):
    sum.append(i+j)
    i=j
    j=sum[c]
    c+=1
print(sum)