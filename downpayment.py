cost_of_house = 1000000
good_credit = False

if good_credit:
    down_payment = .1 * cost_of_house
    print(f"You have good credit. Your down payment is: ${down_payment}")
else:
    down_payment = .2 * cost_of_house
    print(f"You have poor credit. Your down payment is: ${down_payment}")