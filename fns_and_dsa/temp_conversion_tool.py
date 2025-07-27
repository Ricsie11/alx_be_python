# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# --- Main Program ---
temp = input("Enter the temperature to convert: ")

# Try to convert input to a float
try:
    temp = float(temp)
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "F":
    converted = convert_to_celsius(temp)
    print(f"{temp}°F is {converted}°C")
elif unit == "C":
    converted = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {converted}°F")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
# --- End of Main Program ---
# This code provides a simple temperature conversion tool that converts between Celsius and Fahrenheit.
# It prompts the user for a temperature and its unit, performs the conversion, and displays the result.