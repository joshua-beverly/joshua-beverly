## Celsius to Fahrenheit converter

prompt = input('What is the current temperature in degrees Celsius? ') ## ask for temp in Celsius
tempC = int(prompt)             ## convert to integer
tempF = (tempC * 9/5) + 32      ## calculate for F

print("The temperature is " + str(tempF) + " degrees Fahrenheit")  