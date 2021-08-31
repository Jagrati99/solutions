'''def func(n):
	for i in range(1,n):
		if(i%7==0):
			print(i)


k=int(input())
func(k)
'''
#use of generator function
'''
The generator is called just like a normal function. However, its execution is paused on encountering the yield keyword. This sends the first value of the iterator stream to the calling environment. However, local variables and their states are saved internally.
We should use yield when we want to iterate over a sequence but don't want to store the entire sequence in memory. yield is used in Python generators. A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return
'''
def numbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in numbers(100):
    print(i)
