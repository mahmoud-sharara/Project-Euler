#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
num = 2520
i = 2
while i < 21:
  if num%i == 0:
    check = 'good'
    i = i+1
  else:
    num = num +1
    i = 2

print(num)


