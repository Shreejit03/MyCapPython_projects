inp=input("Enter the list items : ")
if inp.count(',')==0:
    list = [int(item) for item in inp.split()]
else:
    list = [item for item in inp.split(',')]
    if list[0].find('['):     
        list[0] = list[0][list[0].index('[')+1:]
        list[-1] = list[-1][:-1]
        list=[int(item)for item in list]
list1=[]
for item in list:
    if(item>0):
        list1.append(item)
print(list1)