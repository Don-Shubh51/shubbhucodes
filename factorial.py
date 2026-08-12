import streamlit as st
st.title("Factorial finder")

number = int(input("Enter the number: "))

def fact():
    product = 1
    for i in range(1, number+1):
        product = product * i

    return product

if number > 0:
    print(f"The factorial of {number} is {fact()}")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    print("Not possible as it is a negative number... negro")
