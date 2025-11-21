FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    temperature =  fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature

def convert_to_fahrenheit(celcius):
    temperature = celcius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return temperature



temperature = input('Enter the temperature to convert: ')
try:
    temperature = int(temperature)
except:
    raise ValueError(f'Invalid temperature. Please enter an integer value')


verify = input('Is the temperature in Celcius or Fahrenheit? (C/F): ')
verify = verify.upper()

if verify == 'C':
    converted = convert_to_fahrenheit(temperature)
    print(f'{temperature}\u00b0C is {converted}\u00b0F')
elif verify == 'F':
    converted = convert_to_celcius(temperature)
    print(f'{temperature}\u00b0F is {converted}\u00b0C')
else:
    print('Invalid Choice')