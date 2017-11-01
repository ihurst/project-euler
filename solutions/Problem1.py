def attempt1(n):
    total = 0

    for i in range(n):
        if i%3==0 or i%5==0:
            total+=i

    return total

print(attempt1(10) == 23)
print(attempt1(1000))