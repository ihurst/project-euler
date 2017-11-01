def isPalindrome(str):
    if len(str)%2 != 0:
        return False
    mid=int(len(str)/2)
    mid2=mid-1
    while(mid2 >= 0):
        if str[mid] != str[mid2]:
            return False
        mid2=mid2-1
        mid=mid+1
    return True

def palindromeProduct(digits):
    answer =(0,0,0)
    for x in range(pow(10,digits-1),pow(10,digits)):
        for y in range(pow(10,digits-1),pow(10,digits)):
            z = x*y
            if isPalindrome(str(z)) and z > answer[2]:
                answer = (x,y,z)

    print("%s x %s = %s" % answer)

print(isPalindrome("101"))
print(isPalindrome("1001"))
print(isPalindrome("11"))
#print(isPalindrome("3744"))

print(palindromeProduct(3))