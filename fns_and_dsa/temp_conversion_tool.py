FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temperature =  (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature

def convert_to_fahrenheit(celsius):
    temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temperature



try:
    temp_input = input("Enter the temperature to convert: ")

    # Validate temperature input
    if not temp_input.replace('.', '', 1).isdigit() and not (
        temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()
    ):
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temp_value = float(temp_input)

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is equal to {result:.2f}°F")

    elif unit == 'F':
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is equal to {result:.2f}°C")

    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

except ValueError as error:
    print(error)