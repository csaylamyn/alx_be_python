
weather = input("What's the weather like today? (cold / rainy / sunny): \n").lower()
print("Today's weather is: ", str(weather_today))

if weather == "cold":
    cold = " coat and a scarf."
    print("Make sure to wear a warm ", cold)

elif weather == "rainy":
    rainy = "umbrella and raincoat."
    print("Dont forget your ", rainy)

elif weather == "sunny":
    sunny = "shirt and sunglasses."
    print("wear a ", sunny)

else:
    print("Sorry, I don't have recommendations for this weather. ")