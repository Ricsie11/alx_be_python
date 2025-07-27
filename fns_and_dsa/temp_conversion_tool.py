# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # ← must be exactly like this

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# --- Main Program ---
temp = input("Enter the temperature to convert: ")

try:
    temp = float(temp)
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "F":
    result = convert_to_celsius(temp)
    print(f"{temp}°F is {result}°C")
elif unit == "C":
    result = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {result}°F")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
