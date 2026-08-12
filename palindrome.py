n = int(input("Enter the number: "))
n = abs(n)
length = len(str(n))

#if u dont want to use function, better store the number in a variable that would store it's og value

def reversal(n):
    final = 0
    for i in range(length):
        r = n % 10
        final = final*10 + r
        n = n//10
    return final

if reversal(n) == n:
    print(f"{n} is a palindrome number")
else:
    print("Not a palindrome number")