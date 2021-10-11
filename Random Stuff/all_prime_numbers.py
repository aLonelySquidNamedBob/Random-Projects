import time

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

starttime = time.time()
numcount = 0
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            numcount += 1
print(numcount)
elapsedtime = time.time() - starttime
print(elapsedtime)