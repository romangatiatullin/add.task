result = ""
n = int(input("Number: "))
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result += str(i) + str(j)
print(result)