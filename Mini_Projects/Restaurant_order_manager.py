#import modules
import sys

#list containing costs
cost_list = [12.99, 6.99, 4.99, 10.99]
menu_items = ["Spaghetti", "Salad", "Cheesecake", "Pizza"]
customer_billing_list = []
total_cost = []

#Welcome message
print("\n..........Welcome to the order management..........\n")

#Display the menu:
print(".....Select one of the following options......")
choice = int(input("1. Display Menu \n2. Place an Order \n3. End Session \ntype your choice here: "))

#logic for overall functioning.
#when user choose 3
if choice == 3:
    sys.exit()
    
#when user choose 1 or 2
elif choice == 1 or choice == 2:
    print(".....Below are the menu items..... \n1. Spaghetti - $12.99 (Main Course) \n2. Salad - $6.99 (Starter) "
          "\n3. Cheesecake - $4.99 (Dessert) \n4. Pizza - $10.99 (Main Course)")
    order = input("\nWhat would you like to order? type numeric values as appears in front of menu item separated by space (example: 1 for Spaghetti): ").split()

#convert the string values in the order list into int values
    int_order = [int(value) for value in order]
    print("....You have selected the following items....")

#for-loop to iterate through each value in the int_order list and display the value against it from menu_items list and print the values to 
#show the customer what he is ordering
    for value in int_order:
#store the food choices in a list customer_billing_list
        customer_billing_list.append(menu_items[value-1])
        print(menu_items[value-1])
#compare the customer_billing_list with list menu_items and findout the position and then using the position in cost_list and then ammend the cost in new list called total_cost.

                

#Confirming if the customer is happy with the order:
    order_confirm = input("\nDo you want to confirm the order? y/n: ").lower()
    if order_confirm == 'n' or order_confirm == 'no':
        final_call = input("We understand sometimes you wanna take time to order right, Do you wanna revisit the menu??? y/n: ").lower()
        if final_call == "n" or final_call == "no":
            sys.exit()
        else:
            sys.exit()
            # print("Restarting the Order Manager app.....")
            # ("call function to restart the program here")
    else:
        for item in customer_billing_list:
            if item in menu_items:
                index = menu_items.index(item)
                total_cost.append(cost_list[index])
                total = sum(total_cost)
                
        print(f"Your total is ${total}")

elif choice >= 4:
    print("Invalid request: please enter the right option")
