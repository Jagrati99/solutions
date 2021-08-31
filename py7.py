X=int(input())
Y=int(input())
list=[[1 for i in range(Y)] for j in range(X)]
#print(list)
for a in range(0,X):
	for b in range(0,Y):
		list[a][b]=a*b

print(list)
