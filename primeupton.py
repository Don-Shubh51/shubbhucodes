n = int(input("Enter the n: "))
#isPrime = True should not be kept here as it is outside the loop
#hence once the inside loop gets to false, it wont recover and would remain false only
prime = [1]

for i in range(2, n+1):
    isPrime = True
    for j in range(2, i):
        if i%j == 0:
            isPrime = False
            break

    if isPrime:
        prime.append(i)

print(f"Prime numbers upto {n} are {prime}")