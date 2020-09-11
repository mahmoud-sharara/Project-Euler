#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

palin=[]
for a in (range(1,1000)):
    for b in (range(1,1000)):
        d = a*b
        d=str(d)
        if len(d)>5:
            if d[0]==d[5]:
                    if d[1]==d[4]:
                        if d[2]==d[3]:
                            palin.append(d)
palin.sort()
print(palin[len(palin)-1])
