
sq = 0
sum = 0

for i in range(1, 101):
    sq =sq+ i**2
    sum =sum+ i

sum = sum**2

print(sum - sq)