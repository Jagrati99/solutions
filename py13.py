i=input()
alpha=0
digits=0
for k in i:
	if ord(k)<=57 and ord(k)>=46:
		digits=digits+1
	if ord(k)>=65 and ord(k)<=122:
		alpha=alpha+1
print("number of aphabets are",alpha)
print("number of digits are",digits)
