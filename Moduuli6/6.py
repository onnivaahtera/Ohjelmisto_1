
def pizza_calc(price, diameter):
    diameter_m = diameter / 100
    area = 3.14 * (diameter_m / 2) ** 2
    return price / area


diameter1 = float(input("diameter of the first pizza: "))
price1 = float(input("price of the first pizza: "))

diameter2 = float(input("diameter of the second pizza: "))
price2 = float(input("price of the second pizza: "))

unit_price1 = pizza_calc(diameter1, price1)
unit_price2 = pizza_calc(diameter2, price2)

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price1 > unit_price2:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas offer the same value for money.")
