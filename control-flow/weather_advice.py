
weather = input("What's the weather like today? (cold / rainy / sunny): \n").lower()
print("Today's weather is: ", str(weather))

if weather == "cold":
    print("Make sure to wear a warm coat and a scarf. ")

elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat. ")

elif weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

else:
    print("Sorry, I don't have recommendations for this weather. ")