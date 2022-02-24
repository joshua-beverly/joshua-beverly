temperature = 55
forecast = "rain"

if temperature > 80 and forecast != "rain":
    print("It's too hot!")
    print("Stay inside.")
elif temperature < 60:
    print("It's too cold!")
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")
