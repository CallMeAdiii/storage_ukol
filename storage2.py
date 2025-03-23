products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "price": 30,
        "name": "BMW",
    }
]


def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}, cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu:")
    product_price = input("Název cenu:")
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)


def search_product():
    """
    This function is used to search for product in the list of products by product name.
    """

    name = input("Chci vyhledat: ")

    for product in products:
        if product['name'].lower().startswith(name.lower()):
            print(f"Název produktu: {product['name']}, cena: {product['price']}$")


def price_sum():
    """
    This function is used to calculate price of all products.
    """

    sum_price = 0

    for product in products:
        sum_price += product['price']

    print(f"Celková cena produktů je {sum_price}")


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání položky")
    print("4. Celková cena produktů")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("Vyhledání položky")
        search_product()
        menu()

    elif choice == 4:
        price_sum()
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
