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


def most_expensive_product():
    """
    This function is used to find the most expensive product in the list of products.
    """

    print("Nejdražší položkou na skladě je:")

    max_price = max(product["price"] for product in products)

    for product in products:
        if product["price"] == max_price:
            print(f"Název produktu: {product['name']}, cena: {product['price']}$")


def cheapest_product():
    """
    This function is used to find least expensive product in the list of products.
    """

    print("Nejlevnější položkou na skladě je:")

    min_price = min(product["price"] for product in products)

    for product in products:
        if product["price"] == min_price:
            print(f"Název produktu: {product['name']}, cena: {product['price']}$")


def avarage_price():
    """
    This function is used to calculate average price of all products.
    """

    price_list = [product["price"] for product in products]
    print(f"Průměrná cena produktů: {sum(price_list)/len(price_list)}")


def edit_product():
    """
    This function is used to edit product in the list of products.
    """
    for index, product in enumerate(products):
        print(f"Číslo produktu: {index} jméno produktu: {product['name']}, cena: {product['price']}$")

    print("řekni mi číslo produktu, který chceš editovat")

    product_index = int(input("Číslo produktu: "))

    print(f"Číslo produktu: {product_index} jméno produktu: {products[product_index]['name']}, cena: {products[product_index]['price']}$")
    print("Pro editaci jména zadej 1 a pro editaci ceny 2")

    product_action = int(input("akce: "))

    if product_action == 1:
        new_name = input("Nové jméno produktu: ")
        products[product_index]['name'] = new_name
    elif product_action == 2:
        new_price = int(input("Nová cena produktu: "))
        products[product_index]['price'] = new_price

    print(f"Upravená položka vypadá takto: cena: {products[product_index]['price']}$, jméno produktu: {products[product_index]['name']}$")


def delete_product():
    """
    This function is used to delete product in the list of products.
    """
    for index, product in enumerate(products):
        print(f"Číslo produktu: {index} jméno produktu: {product['name']}, cena: {product['price']}$")

    print("Zadej mi číslo produktu který chceš smazat")
    product_index = int(input("Číslo produktu: "))

    if product_index < len(products):
        products.pop(product_index)

    print(f"produkt číslo {product_index} byl smazán")

def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Vyhledání položky")
    print("4. Celková cena produktů")
    print("5. Nejdražší položka na skladě")
    print("6. Nejlevnější položka na skladě ")
    print("7. Průměrná cena produktů")
    print("8. Editovat položku")
    print("9. Smazání produktu")

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

    elif choice == 5:
        most_expensive_product()
        menu()

    elif choice == 6:
        cheapest_product()
        menu()

    elif choice == 7:
        avarage_price()
        menu()

    elif choice == 8:
        edit_product()
        menu()

    elif choice == 9:
        delete_product()
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
