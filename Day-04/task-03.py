temperatures = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda celsius: (celsius * 9/5) + 32, temperatures))

print("Celsius:", temperatures)
print("Fahrenheit:", fahrenheit)