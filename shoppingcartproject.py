#shopping cart stock project example
customer_items = ["blue_eyeliner", "eyeshadow", "mascarra", "pink_lipstick"]
store_inventory = {"blue_eyeliner": 10, "eyeshadow": 5, "mascarra": 4, "pink_lipstick": 3}

for item in customer_items:
    if store_inve203ntory.get(item, 0) == 0:
        print(f"Sorry, {item} is out of stock.")

else:
    print("Your item is in stock!")