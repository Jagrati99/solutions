a = 0
while True:
    s = input()
    if not s:
        break
    i = s.split(" ")
    #print(i)
    st = i[0]
    #print(st)
    amount = int(i[1])
    #print(amount)
    if st=="D":
        a+=amount
    elif st=="W":
        a-=amount
    else:
        pass
print(a)
