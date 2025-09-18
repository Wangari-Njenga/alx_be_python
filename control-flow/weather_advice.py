#This code suggests outfits to wear according to the weather

def get_weather_advice():
#Asks user about the weather
    weather = input("What's the weather like today? (sunny/rainy/cold): ")

    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather condition."

advice = get_weather_advice()
print(advice)
