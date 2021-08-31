n=input()
upper=0
lower=0
for i in n:
	if ord(i)>=65 and ord(i)<=90:
		upper=upper+1
	if ord(i)>=97 and ord(i)<=122:
		lower=lower+1

print("upper case letters",upper)
print("lower case letters",lower)
