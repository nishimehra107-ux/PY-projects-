menu={"pizza":4.00,
      "popcorn":5.90,
      "chips":2.50,
      "coke":1.68,
      "chocolate":2.36}

cart=[]
total=0
print("------MENU------")
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("----------------")

while True:
    food=input("select an item (q to quit):  ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("======YOUR ORDER======")
for food in cart:
    total+=menu[food]
    print(food, end=" ")
print()
print(f"total is : ${total:.2f}")
