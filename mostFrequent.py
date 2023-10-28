def most_frequent(str):
    dict={}
    for i in str:
        if(dict.get(i)):
            dict[i]=dict.get(i)+1
        else:
            dict[i]=1
    dictcp=dict.copy()
    for i in dictcp:
        c=i
        for j in dictcp:
            if dictcp.get(c)<dictcp.get(j):
                c=j
        print(c,":",dictcp.get(c))
        dictcp[c]=0
    del dictcp

str=input("Please enter a string:")
most_frequent(str)
