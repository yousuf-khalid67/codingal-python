def findcube(n):

    return n*n*n



list_div3=[i for i in list1 if i % 3==0]

print(list_div3)

maped1=list(map(findcube, list1))

maped2=list(map(findcube, list_div3))

print(maped1,maped2)list1=[2, 3, 6, 7, 4, 1]

ziped=list(zip(list_div3,maped2))

print(ziped)