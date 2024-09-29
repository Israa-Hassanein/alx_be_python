# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_IN_FAHRENHEIT = 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - FREEZING_POINT_IN_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_IN_FAHRENHEIT

# User Interaction
def main():
    temp_input = input("Enter the temperature to convert: ")
    temp = float(temp_input)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Perform the appropriate conversion
    if unit == "F":
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    elif unit == "C":
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Call the main function
main()
       
