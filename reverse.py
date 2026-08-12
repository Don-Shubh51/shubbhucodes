n = input("Enter your number to be reversed: ")
length = len(n)
n = int(n)

def mechanism(n):
    final = 0
    for i in range(length):
        r = n % 10
        final = final*10 + r
        n = n//10

    return final

print(f"The number after being reversed is {mechanism(n)}")