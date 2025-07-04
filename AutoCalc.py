import streamlit as st
import random

# 🎨 Random background color themes
themes = ["#ffcccc", "#ccffcc", "#ccccff", "#ffffcc", "#e0ccff", "#ffe0cc"]
bg_color = random.choice(themes)

# 🌈 Set page and background style
st.set_page_config(page_title="Auto Calc", page_icon="🧮", layout="centered")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        padding: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 📌 Title and instruction
st.title("🧮 Auto Calc")
st.markdown("Enter **multiple numbers** and choose the operation to perform.")

# 🧾 User input
number_input = st.text_input("Enter numbers separated by commas")
operation = st.selectbox("Choose Operator", ["+", "-", "*", "/"])

# ⚙️ Process input
try:
    numbers = [float(x.strip()) for x in number_input.split(",") if x.strip()]
    
    if numbers:
        if operation == "+":
            result = sum(numbers)
        elif operation == "-":
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
        elif operation == "*":
            result = 1
            for num in numbers:
                result *= num
        elif operation == "/":
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    raise ZeroDivisionError
                result /= num
        
        st.success(f"✅ Result: {result}")
    else:
        st.warning("⚠️ Please enter at least one number.")

except ZeroDivisionError:
    st.error("🚨 Division by zero is not allowed!")

except:
    st.error("⚠️ Invalid Input!")
                    
        