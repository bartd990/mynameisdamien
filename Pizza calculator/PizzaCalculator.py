class PizzaCalculator:
    # 1. ask manager: what is the unit of a pizza
    pepperoni_price = input("What is the price of a pepperoni pizza tonight? $")
    pepperoni_price = eval(pepperoni_price)
    hawiian_price = input("What is the price of a hawaiian pizza tonight? $")
    hawiian_price = eval(hawiian_price)
    meat_lovers_price = input("What is the price of a meat lovers pizza tonight? $")
    meat_lovers_price = eval(meat_lovers_price)
    # 2. ask costomer: which pizzas do they want?
    number_of_pepperonies = 0
    number_of_hawaiians = 0
    number_of_meat_lovers = 0
    pizzas_selected = input("Customer, which pizzas do you want to order? (1. pepperoni, 2.hawaiian, 3.meat lover's)")

    if("1" in pizzas_selected or "pepperoni" in pizzas_selected):
    # 1. ask how many of each
        number_of_pepperonies = input("How many pepperoni pizzas whould you like to order")
        # this eval converts
        number_of_pepperonies = eval (number_of_pepperonies)
    if("2" in pizzas_selected):
        number_of_hawaiians = input("How many hawaiian pizzas whould you like to order?")
        number_of_hawaiians = eval (number_of_hawaiians)
    if("3" in pizzas_selected):
        number_of_meat_lovers = input("How many meat lover's pizza would you like to order?")
        number_of_meat_lovers = eval (number_of_meat_lovers)

    # 3. calculate order before tax = (order = price * quanity)
    pepperoni_order = number_of_pepperonies * pepperoni_price
    hawiian_order = number_of_hawaiians * hawiian_price
    meat_lovers_order = number_of_meat_lovers * meat_lovers_price
    total_order = pepperoni_order + hawiian_order + meat_lovers_order
    print("Here's your order before tax: ", total_order)
    # 4. calculate tax
    tax_rate = .0775
    sales_tax_amount = total_order * tax_rate
    print("Your sales tax amounts to ",sales_tax_amount, " at ",str(tax_rate))
    # 5. grand total caculates
    grand_total = total_order + sales_tax_amount
    print("your grand total comes to ", grand_total)
    