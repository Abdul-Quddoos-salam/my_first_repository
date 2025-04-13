
import streamlit as st

def convert_unit(value: float, unit_from: str, unit_to: str):
    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:
        return "Conversion not supported"

def main():
    st.title("Welcome to Basic Unit Converter")

    value = st.number_input("Enter the value you want to convert:")
    
    unit_from = st.text_input("Enter the unit to convert from (e.g., meters, kilometers, grams, kilograms):")
    unit_to = st.text_input("Enter the unit to convert to (e.g., meters, kilometers, grams, kilograms):")

    if st.button("Convert"):
        result = convert_unit(value, unit_from, unit_to)
        print("your converted value is: {result}")
main()
      
