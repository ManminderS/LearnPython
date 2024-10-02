import art

#print on the screen
print("\n ........................WELCOME TO TREASURE ISLAND QUEST.....................")
print(art.welcome)
your_name = input("Whats your name: ")
stat = input(f"Hi! {your_name}, are you ready, 'yes' or 'no': ").lower()

#logic for accepting yes for proceeding further
if stat == "yes":
    print(f"{your_name}, You showed up at Waterfront station and to reach the mystery island you have 3 options(Skytrain, Bus, or Seabus) \n")
    transit = input("How you want to proceed, choose 'SkyTrain', 'SeaBus', or 'Bus': ").lower()
    if transit == "skytrain":
        print("You were attacked by zombies in the train that took you to other side of city")
        print(art.train)
        print(art.game_over)
    elif transit == "bus":
        print(art.bus)
    elif transit == "seabus":
        seabus_yes_or_no = input("Next SeaBus is 30 minutes later, rather wanna swim across the channel? yes or no: ")
        if seabus_yes_or_no == "no":
            print(art.seabus)
            print(art.castle)
            door = input("Which door do you want to open? 'Red', 'Yellow', or 'Blue': ").lower()
            if door == "red":
                print(art.red_door)
            elif door == "blue":
                print(art.beast)
            elif door == "yellow":
                print(art.treasure)
            else:
                print(f"there isn't any {door} door")

        else:
            print(art.shark)
else:
    print(art.game_over)
