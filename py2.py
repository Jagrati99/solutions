'''n=int(input())
fact=1
for i in range(1,n+1):
	fact=fact*i
	
print(fact)'''
#recursive method
def fact(x):
	if x==0:
		return 1
	else:
		return x*fact(x-1)

x=8
print(fact(x))




