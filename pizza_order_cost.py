'''
This program calculates the cost of a pizza order based on the size of the pizza, the number of toppings, and the distance for delivery.

Get the inputs from the user. if any value is invalid, print an error message and exit the program. if all values are valid, calculate the 
cost of the pizza order and print it to the user.
'''

# only accept "small" or "large" in lower or uppercase for pizza size.
pizza_size = input("What is the size of the pizza? Small or large? ").lower()
if (pizza_size != "small" and pizza_size != "large"):
    print("Invalid pizza size. Please enter 'small' or 'large'.")
else:
    while True: 
        #if number_of_toppings and distance are integers, this block of code will execute.
        try:
            number_of_toppings = int(input("How many toppings would you like? "))
            distance = int(input("What is the distance for delivery in miles? "))

            # calculate the cost based on the size of the pizza.
            if pizza_size == "small":
                cost = 8.00
            elif pizza_size == "large":
                cost = 12.00

            # calculate the cost based on the number of toppings.
            cost += number_of_toppings * 1

            # calculate the cost based on the distance for delivery.
            if distance <= 5:
                cost += 2.00
            elif distance > 5:
                cost += (distance - 5) + 2.00

            # print the total cost of the pizza order to the user.
            print(f"The total cost of your pizza order is: ${cost:.2f}")
            break
        
        except ValueError:
            # if the user enters a non-integer value for number_of_toppings or distance, print an error message and exit the program.
            print("Invalid input. Please enter a number.")
            break
       
