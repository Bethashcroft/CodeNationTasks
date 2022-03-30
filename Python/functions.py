# def press_grind_beans(): 
#     print("Grinding for 20 seconds")
    
# press_grind_beans()

# def say_hello():
#     print("Hello")

# say_hello()

# def cash_withdrawal(amount, accnum):
#     print("Withdrawing {} from account {}".format(amount, accnum))
    
# cash_withdrawal(300, 50449921)

# def coffee_order(size, drink):
#     print("Can I have a {} {} please?".format(size, drink))
    
# coffee_order("large", "tea")


# def add_up(num1, num2):
#     return num1 + num2

# add_up(5, 10)
# print(add_up(5, 10))

# def multiply_by_nine_fifths(celsius):
#     return celsius * (9/5)

# def get_fahrenheit(celsius):
#     return multiply_by_nine_fifths(celsius) + 32

# print("The temperature is {} F".format(get_fahrenheit(15)))

order_count = 0

def pizza_order(topping1,topping2,topping3):
    global order_count
    print(f"Your pizza got {topping1}, {topping2} and {topping3} on it")
    order_count += 1
    print(f"order number: {order_count}")
    
pizza_order("pepperoni","onion","pepper")
pizza_order("ham", "sweetcorn", "beef")

