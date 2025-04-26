shop_items = {}

ch = input("Do you want to update the shop's database? (y/n): ")
ch = ch.lower()

while ch != 'n':
    product = input("Enter the product's name: ")
    price = float(input("Enter the price: "))
    shop_items[product] = price
    ch = input("Do you want to continue? (y/n): ")
    ch = ch.lower()

while True:
    search = input("Enter the product's name to find its price: ")

    if search in shop_items:
        print("The price of", search, "is", shop_items[search])
    else:
        print("Sorry, the product does not exist")

    a = input("Do you want to search for another product? (y/n): ")
    a = a.lower()
    if a == 'n':
        print("Thank you")
        break
