n=[x for x in input().split(",")]
l=[]
for i in n: 
	if(int(i)%2!=0):
		l.append(i)

print(','.join(l))
