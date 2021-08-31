n=[x for x in input().split(",")]
li=[]
for y in n:
	if(int(y)%5==0):
		li.append(y)

print(",".join(li))
