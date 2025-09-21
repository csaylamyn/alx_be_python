
weather_today = input("What is the weather Today? cold / rainy / sunny \n")
print("Today's weather is: ", str(weather_today))
weather_today = weather_today.lower()
if weather_today == "cold":
    cold = " coat and a scarf."
    print("Make sure to wear a warm ", cold)

elif weather_today == "rainy":
    rainy = "umbrella and raincoat."
    print("Dont forget your ", rainy)

elif weather_today == "sunny":
    sunny = "shirt and sunglasses."
    print("wear a ", sunny)

else:
    print("Sorry, I don't have recommendations for this weather. ")