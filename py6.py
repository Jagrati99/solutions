import math
l=[]
i=[x for x in input().split(",")]
for y in i:
	l.append(str(math.floor(math.sqrt((2*50*int(y))//30))))

print(','.join(l))

