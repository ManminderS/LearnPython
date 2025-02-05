#Welcome Screen
print("..............Welcome to password strenth Checker Software................\n")

#Asking user if they want to learn how to set a strong password & Logic for Strong password information
start = input("DO you want to learn, What are the attributes of a strong password?(yes/no): ")

if start == "yes":
    print("\nThe general rule of thumb while setting up a strong password is that it should include the below items: \n 1. The password must be at least 8 characters long. \n 2. The password must contain at least one uppercase letter. \n 3. The password must contain at least one lowercase letter. \n 4. The password must contain at least one digit. \n 5. The password must contain at least one special character (e.g., !, @, #, $, %, etc.).")
