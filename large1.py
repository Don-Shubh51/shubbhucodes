arr =[]
def array():
    count = int(input("Enter the number of numbers u wanna compare: "))
    for i in range(count):
        arr.append(int(input("Enter the number:")))

    return arr

print(max(array()))
    