prev=None
current=None

def fib(n):
    global prev
    global prev2

    if n == 1:
        prev = 1
        return 1
    elif n == 2:
        prev2 = 2
        return 2
    else:
        if prev1 is None and prev2 is None:
            return fib(n - 2) + fib(n - 1)

        val = prev1 + prev2
        prev1 = prev2
        prev2 = val

        return val

def calculate():
    MAX = 4000000
    i = 1
    val = 0
    total = 0
    while val <= MAX:
        val = fib(i)
        i+=1
        if val%2 == 0:
            total += val
    return total

def calculate2():
    data = [1,2]
    while data[-2] + data[-1] <= 4000000:
        data.append(data[-2] + data[-1])
    return sum([e for e in data if not e%2])

print("Total: " + str(calculate2()))

