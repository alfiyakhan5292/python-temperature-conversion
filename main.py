# temperature converision  (Window : Alt + 0176 = °)

unit = input("Is this temperature in  Celsius or Fahrenheit (C/F):")
temp = float(input("Enter the temperature:"))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)    #formula of celsius to fahrenheit (C * 9/5) + 32 = F
    print(f"The temperature in fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp -32) * 5 / 9, 1)                #formula of fahrenheit to celsius (°F - 32) * 5 / 9 = C
    print(f"The temperature in celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")