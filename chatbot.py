import streamlit as st

st.title("🧮 Calculator")

col1, col2 = st.columns(2)
num1 = col1.number_input("First number", value=0.0)
num2 = col2.number_input("Second number", value=0.0)

operation = st.selectbox("Operation", ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)", "Power (^)", "Modulus (%)"])

if st.button("Calculate"):
    if operation == "Add (+)":
        result = num1 + num2
    elif operation == "Subtract (-)":
        result = num1 - num2
    elif operation == "Multiply (×)":
        result = num1 * num2
    elif operation == "Divide (÷)":
        if num2 == 0:
            st.error("Cannot divide by zero!")
            st.stop()
        result = num1 / num2
    elif operation == "Power (^)":
        result = num1 ** num2
    else:
        if num2 == 0:
            st.error("Cannot use modulus with zero!")
            st.stop()
        result = num1 % num2

    st.success(f"Result: {result}")