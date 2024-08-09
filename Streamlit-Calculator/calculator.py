import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Subheading with your name
st.subheader("Designed by M. Abbas")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Dropdown to select the operation
operation = st.selectbox("Choose the operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation based on the selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display the result
st.write("### Result:", result)
