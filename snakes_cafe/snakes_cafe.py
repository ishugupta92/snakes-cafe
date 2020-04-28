WELCOME_MESSAGE = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************"""

ORDER_PROMPT = """***********************************
** What would you like to order? **
***********************************"""

ORDER_TEXT = """***********************************
********** Your order is **********
***********************************"""

MENU = {
    "Appetizers": ("Wings", "Cookies", "Spring Rolls"),
    "Entrees": ("Salmon", "Steak", "Meat Tornado", "A Literal Garden"),
    "Desserts": ("Ice Cream", "Cake", "Pie"),
    "Drinks": ("Coffee", "Tea", "Unicorn Tears")
}

ORDER = {}


def print_order():
    print(ORDER_TEXT)
    for item, count in ORDER.items():
        print(count, item)


def valid_menu_item(item):
    for category, items in MENU.items():
        if item in items:
            return True
    return False


def inform_of_invalid_item(item):
    print(f"** Sorry! We do not have {item}")


def ask_for_order():
    print(ORDER_PROMPT)
    return input("> ")


def check_for_quit(order):
    if order.capitalize() == "Quit":
        print_order()
        exit(0)


def add_item(item):
    if item in ORDER:
        ORDER[item] += 1
        order_text = "orders"
    else:
        ORDER[item] = 1
        order_text = "order"

    print(f"** {ORDER[item]} {order_text} of {item} have been added to your meal ")


def print_menu():
    for category, items in MENU.items():
        print(f"{category}\n{'-' * len(category)}")
        for item in items:
            print(item)
        print()


def welcome():
    print(WELCOME_MESSAGE)
    print()
    print_menu()


def main():
    welcome()

    while True:
        order = ask_for_order()
        check_for_quit(order)
        if not valid_menu_item(order.title()):
            inform_of_invalid_item(order)
            continue
        add_item(order.title())


if __name__ == "__main__":
    main()
