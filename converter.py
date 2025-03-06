# Project 01: Unit Convertor
# Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: #0e1015;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .description {
        color: #6c757d;
        text-align: center;
        font-size: 1rem;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }
    .stButton button {
        background: #2c3e50;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: #34495e;
        transform: translateY(-1px);
    }
    .result-box {
        background: #2c3e50;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 1rem;
        position: relative;
    }
    .error-box {
        background: #ff4444;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 1rem;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #2c3e50;
        color: #6c757d;
        font-size: 0.9rem;
    }
    .stSelectbox > div > div {
        border-radius: 10px;
    }
    .stNumberInput > div > div > input {
        border-radius: 10px;
    }
    .copy-button {
        position: absolute;
        right: 10px;
        top: 50%;
        transform: translateY(-50%);
        background: transparent;
        border: 1px solid white;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 8px;
        cursor: pointer;
        font-size: 0.8rem;
    }
    .copy-button:hover {
        background: rgba(255, 255, 255, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class='description'>
        A versatile unit conversion tool that helps you convert between different units of Length, Weight, Temperature, and Volume. 
        Simply select your unit type, choose the source and target units, enter your value, and get instant conversions.
    </div>
    """, unsafe_allow_html=True)

# Unit type selection
unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature", "Volume"])

# Unit selection
col1, col2 = st.columns(2)

if unit_type == "Length":
    units = ["Meter", "Kilometers", "feet", "Centimeters", "Millimeters", "Miles", "Yards", "Inches"]
elif unit_type == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Milligrams", "Ounces"]
elif unit_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
else:  # Volume
    units = ["Liters", "Gallons", "Cups", "Tablespoons", "Teaspoons"]

with col1:
    from_unit = st.selectbox("From", units)
with col2:
    to_unit = st.selectbox("To", units)

# Value input
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)

# Convert button
if st.button("Convert"):
    if value == 0:
        st.markdown("<div class='error-box'>Please enter a value to convert!</div>", unsafe_allow_html=True)
    else:
        if unit_type == "Length":
            length_conversion = {
                "Meter": 1, "Kilometers": 0.001, "feet": 3.28, "Centimeters": 100,
                "Millimeters": 1000, "Miles": 0.000621371, "Yards": 3.28, "Inches": 39.37
            }
            result = value / length_conversion[from_unit] * length_conversion[to_unit]
        
        elif unit_type == "Weight":
            weight_conversion = {
                "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462,
                "Milligrams": 1000000, "Ounces": 35.274
            }
            result = value / weight_conversion[from_unit] * weight_conversion[to_unit]
        
        elif unit_type == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
        
        else:  # Volume
            volume_conversion = {
                "Liters": 1, "Gallons": 0.264172, "Cups": 4.22675,
                "Tablespoons": 67.628, "Teaspoons": 202.884
            }
            result = value / volume_conversion[from_unit] * volume_conversion[to_unit]

        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>© 2024 Unit Converter | Developed by Ghulam Ahmad</div>", unsafe_allow_html=True)

