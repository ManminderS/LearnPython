#import modules


#Welcome message
print("\n..........Welcome to the order management..........\n")

#Display the master page:
print("Please select one of the following options:")
choice = int(input("1. Display Menu \n2. Place an Order \n3. End Session \ntype your choice here: "))

#logic to display the menu.
if choice == 1:
    print("\n1. Spaghetti - $12.99 (Main Course \n2. Salad - $6.99 (Starter) "
          "\n3. Cheesecake - $4.99 (Dessert) \n4. Pizza - $10.99 (Main Course)")
else:
    print("You haven't selected any option to go further")

