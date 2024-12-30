#import modules
import sys

#list containing costs
cost_list = [12.99, 6.99, 4.99, 10.99]
menu_items = ["Spaghetti", "Salad", "Cheesecake", "Pizza"]
customer_billing_list = []

#Welcome message
print("\n..........Welcome to the order management..........\n")

#Display the menu:
print(".....Select one of the following options......")
choice = int(input("1. Display Menu \n2. Place an Order \n3. End Session \ntype your choice here: "))

#logic for overall functioning.
if choice == 3:
    sys.exit()
    
elif choice == 1 or 2:
    print(".....Below are the menu items..... \n1. Spaghetti - $12.99 (Main Course) \n2. Salad - $6.99 (Starter) "
          "\n3. Cheesecake - $4.99 (Dessert) \n4. Pizza - $10.99 (Main Course)")
    order = input("\nWhat would you like to order? type numeric values as appears in front of menu item separated by space (example: 1 for Spaghetti): ").split()
    int_order = [int(value) for value in order]
    print("....You have selected the following items....")
    for value in int_order:
        print(menu_items[value-1])
    order_confirm = input("\nDo you want to confirm the order? y/n: ")
    if order_confirms == "y" or "Y" or "YES" or "yes":
        print("Your total is $$")
    else:
        final_call = input("We understand sometimes you wanna take time to order right, Do you wanna revisit the menu??? y/n: ")
        if final_call == "n" or "No" or "NO" or "no":
            sys.exit()
        else:
            print("Restarting the Order Manager app.....")
            ("call function to restart the program here")
        
        
    
else:
    print("You haven't selected any option to go further")
    
