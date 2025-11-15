menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total=0.00
while True:
     try:
        text = input("Item: ").title()
     except EOFError:
        break
     else:
        if text in menu:
            total+=menu[text]
            print(f"Total: ${total:.2f}")
        else:
            continue


