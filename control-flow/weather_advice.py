enquire = input("What's the weather like today? (sunny/rainy/cold):").lower()

if enquire == 'sunny':
    print('Wear a t-shirt and sunglasses.')

elif enquire == 'rainy':
    print("Don't forget your umbrella and a raincoat.")

elif enquire == 'cold':
    print('Make sure to wear a warm coat and a scarf.')

else:
    print("Sorry, I don't have recommendations for this weather.")