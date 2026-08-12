n = int(input("Enter the number u want to check: "))
count = True

for i in range(2, n):
    if (n % i) == 0:
        count = False

if count:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")