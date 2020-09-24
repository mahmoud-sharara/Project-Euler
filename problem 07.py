#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

number =[]
for i in range (1,110000):
        for x in range (2,i):
            if i%x==0:
                break
        else:
          number.append(i)
number.sort()
print(number[10001])

