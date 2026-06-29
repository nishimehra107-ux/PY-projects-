unit=input("is this temperature in celsius or fahrenheit?(c/f):")
temp=float(input("enter the temoperature:"))

if unit=="c":
    fahrenheit=round((temp*9/5)+32,1)
    print(f"the temperature in fahrenheit is: {fahrenheit}°F")
elif unit=="f":
    celsius=round((temp-32)*5/9,1)
    print(f"the temperature in celsius is: {celsius}°C")
else:
    print("invalid input")