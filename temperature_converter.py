def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temp = float(input("Enter temperature value: "))
unit = input("Enter unit (C/F): ").upper()

if unit == 'C':
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(temp))
elif unit == 'F':
    print("Temperature in Celsius:", fahrenheit_to_celsius(temp))
else:
    print("Invalid unit! Please enter C or F.")