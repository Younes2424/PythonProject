small_pack_price, regular_pack_price, party_pack_price = float(5.50), float(15.00), float(35.00)

xtopping_small_price, xtopping_regular_price, xtopping_party_price = float(2.00), float(4.50), float(8.50)
# The next four lines are variables and lists, required
# to enter the loops, and verify the user's input
tub_num, tub_size, extra_topping, order_cost, count, coupon_code = 0, 0, 0, 0, 0, 0
size_list = ["Small", "Regular", "Party"]
topping_list = ["Y", "N"]
coupon_list = ["VIP"]


def display_instructions():
    print("This program calculates the cost of an order based on standard Gelato prices.\nTub sizes are 250 mL for a small pack, 1 Litre for a regular pack, and 3.5 Litre for a party pack.\nExtra topping includes diced almonds, mini marshmallows, and 100s & 1000s.\nTo calculate the cost of your order please answer below statements.\n")


def get_tub_num(question):
    # Asks for the number of tubs, and shows an
    # error message for invalid inputs.
    try:
        tub_num = int(input(question))
        if tub_num not in range(1, 11):
            print("Out of range value! Please, try again.")
    except ValueError:
        print("Value error! Please, try again with an integer.")
    else:
        return tub_num


def get_tub_size(question):
    # Asks for the ice cream tub size, and shows an
    # error message for invalid inputs.
    tub_size = input(question)
    if tub_size not in size_list:
        print("Incorrect input! Please, specify the tub size again.")
    return tub_size


def get_extra_topping(question):
    # A boolean function that asks whether the user
    # wants any extra toppings.
    extra_topping = input(question)
    if extra_topping not in topping_list:
        print("Incorrect input! Please, state the topping again.")
    return extra_topping


def get_order_cost(tub_size, extra_topping):
    # The parametres and variables were kept the same.
    # To change parametres the variables should be changed
    # as well.
    if tub_size == "Small" and extra_topping == "Y":
        order_cost = small_pack_price + xtopping_small_price
    elif tub_size == "Small" and extra_topping == "N":
        order_cost = small_pack_price
    elif tub_size == "Regular" and extra_topping == "Y":
        order_cost = regular_pack_price + xtopping_regular_price
    elif tub_size == "Regular" and extra_topping == "N":
        order_cost = regular_pack_price
    elif tub_size == "Party" and extra_topping == "Y":
        order_cost = party_pack_price + xtopping_party_price
    else:
        order_cost += party_pack_price
    return order_cost


def get_coupon_code(question):
    coupon_code = input(question)
    return coupon_code
