from myModules import *

display_instructions()

while tub_num not in range(1, 11):
    tub_num = get_tub_num("Enter the number of ice cream tubs (1 - 10): ")

# The loop asks for the size of the tubs and extra topping
# for as many times as the number of ice cream tubs.
for count in range(1, tub_num + 1):
    while tub_size not in size_list:
        tub_size = get_tub_size("Enter the ice cream tub size (Small/Regular/Party): ")

    while extra_topping not in topping_list:
        extra_topping = get_extra_topping("Do you need extra topping (Y/N): ")
    # The parameters, for the bellow function and the
    # the variables inside of it could be changed in
    # myModules.py
    order_cost += get_order_cost(tub_size, extra_topping)

    # After the cost for one ice cream tub is calculated,
    # the variables bellow will be reset to zero, so the
    # loop starts calculating the price for the next tub.
    tub_size, extra_topping = 0, 0

while coupon_code not in coupon_list:
    coupon_code = get_coupon_code("Please, enter your coupon code here (Press enter key for no code): ")
    if coupon_code in coupon_list:
        order_cost -= 2
    elif coupon_code == '':
        break
    else:
        print("The code entered does not exist! Please, try again.")

print("The cost of the ice cream is $", order_cost)

# The third version of the code was submitted for project 2 assignment.
