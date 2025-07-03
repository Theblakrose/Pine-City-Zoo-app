
#Create a shopping cart programe that will continuosly ask for a food product and the wprice of the product
#Have an exit clause if the user wishe to stop adding more things to their cart
#At the end show the food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the (food)= R"))
        foods.append(food)
        prices.append(price)

        print("----YOUR CART----")

        for food in foods:
            print(food, end = "")

            for price in prices:
                total += price

print("\n")
print(f"YOUR total is: R{total}")

30