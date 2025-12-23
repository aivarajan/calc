# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 13:33:06 2025

@author: GITAA029
"""

import streamlit as st

# ------------------------------
# Title
# ------------------------------
st.title("🧮 Basic Calculator App")

st.write("Enter two numbers and select an operator")

# ------------------------------
# User Inputs
# ------------------------------
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operator = st.selectbox(
    "Select Operation",
    ("+", "-", "*", "/")
)

# ------------------------------
# Calculation Function
# ------------------------------
def calculate(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        if n2 == 0:
            return "Error: Division by zero"
        return n1 / n2

# ------------------------------
# Button Action
# ------------------------------
if st.button("Calculate"):
    result = calculate(num1, num2, operator)
    st.success(f"Result: {result}")


