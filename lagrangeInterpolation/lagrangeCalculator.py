import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lagrange Interpolation", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #FFFDF6;
        color: #262730;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Neumorphic-style button */
    div.stButton > button {
        background: #FFFDF6;
        border: none;
        border-radius: 60px;
        box-shadow: 6px 6px 12px #bebebe, -6px -6px 12px #ffffff;
        color: #333;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #ffffff;  /* Change hover background color to white */
        box-shadow: inset 6px 6px 12px #bebebe, inset -6px -6px 12px #ffffff;
    }

    /* Neumorphic Subheader Styling */
    .neumorphic-subheader {
        background: #FFFDF6;
        padding: 12px 24px;
        border-radius: 60px;
        box-shadow: 6px 6px 12px #bebebe, -6px -6px 12px #ffffff;
        color: #333;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        display: inline-block;
        margin-bottom: 10px;
    }

    /* Align button to the right */
    .stButton {
        display: flex;
        justify-content: flex-end;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background: #FFFDF6;
    padding: 25px;
    border-radius: 60px;
    box-shadow: inset 6px 6px 12px #bebebe, inset -6px -6px 12px #ffffff;
    text-align: center;
    margin-bottom: 30px;">
    <h1 style='color: #333333; font-size: 36px;'>Lagrange Interpolation Calculator</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Built and Designed by **Rhiane Miguel Veron S. Dalumpines**. Use Light Mode for best experience.

This app allows you to:

1. Input a set of known data points  
2. Enter an X-value to interpolate  
3. Compute the estimated Y-value using the **Lagrange Polynomial**  
4. Visualize the resulting curve and interpolation point

---
""")

st.markdown('<div class="neumorphic-subheader">Number of Data Points</div>', unsafe_allow_html=True)
n = st.number_input("Specify the data set size:", min_value=2, step=1, value=3)

st.markdown('<div class="neumorphic-subheader">Enter Data Points</div>', unsafe_allow_html=True)
x_values = []
y_values = []

for i in range(n):
    col1, col2 = st.columns(2)
    with col1:
        x_val = st.number_input(f"x[{i}]", key=f"x_{i}")
    with col2:
        y_val = st.number_input(f"y[{i}]", key=f"y_{i}")
    x_values.append(x_val)
    y_values.append(y_val)

# ---------- Input: Value to Interpolate ----------
t = st.number_input("📍 Enter the X value to interpolate at", key="t_val")

# ---------- Lagrange Interpolation Logic ----------
def lagrange_interpolation(x, y, t):
    total = 0
    n = len(x)
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (t - x[j]) / (x[i] - x[j])
        total += term
    return total

# ---------- Compute and Display Result ----------
if st.button("⌨️Compute Interpolation"):
    try:
        result = lagrange_interpolation(x_values, y_values, t)
        st.success(f"✅ Interpolated value at x = {t} is **{result:.4f}**")

        # Plotting the interpolation
        x_plot = np.linspace(min(x_values), max(x_values), 500)
        y_plot = [lagrange_interpolation(x_values, y_values, xi) for xi in x_plot]

        plt.figure(figsize=(10, 5))
        plt.plot(x_plot, y_plot, label="Lagrange Polynomial", color="blue")
        plt.scatter(x_values, y_values, color="red", label="Data Points")
        plt.scatter(t, result, color="green", label=f"Interpolated Point ({t}, {result:.4f})")
        plt.title("Lagrange Interpolation Curve")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")
