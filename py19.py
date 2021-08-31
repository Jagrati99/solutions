p=[]
while True:
	i=input()
	if i:
		p.append(i.split(","))


	else:
		break


print(sorted(p,key=lambda x:(x[0],x[1],x[2])))

