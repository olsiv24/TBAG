from room import Room
from character import Enemy, Friend
from item import Item

# Initialize rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
garden = Room("Garden")
locked_room = Room("Locked Room")  # Locked room that needs a key

# Initialize enemies
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi, I'm Dave, and I will bite!")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

# Initialize a friendly character (Friend)
lucy = Friend("Lucy", "A kind-hearted gardener.")
lucy.set_conversation("Hello! I love tending to the flowers in the garden.")
garden.set_character(lucy)

# Initialize items
key = Item()
key.set_name("key")
key.set_description("A small rusty key.")
ballroom.set_item(key)  # Place the key in the ballroom

# Set room descriptions
kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom.set_description("A vast room with a polished wooden floor.")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")
garden.set_description("A peaceful garden with blooming flowers.")
locked_room.set_description("A room that is locked. You need a key to enter.")

# Link rooms
kitchen.link_rooms(dining_hall, "south")
dining_hall.link_rooms(kitchen, "north")
dining_hall.link_rooms(ballroom, "west")
ballroom.link_rooms(dining_hall, "east")
ballroom.link_rooms(garden, "south")
garden.link_rooms(ballroom, "north")
garden.link_rooms(locked_room, "west")  # Linking garden to locked room

# Set the initial room and inventory
current_room = kitchen
inventory = []

# Game loop
while True:
    print("\n")
    current_room.get_details()

    # Get the inhabitant of the room (if any)
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    # Check if there is an item in the room
    item = current_room.get_item()
    if item is not None:
        print(f"You see a {item.get_name()} here.")

    # Get user input for their next action
    command = input("> ").lower()

    # Check whether a direction was typed and move the player
    if command in ["north", "south", "east", "west"]:
        if current_room == garden and command == "west" and "key" not in inventory:
            print("The door is locked. You need a key to enter.")
        else:
            current_room = current_room.move(command)

    # If the user types 'talk', talk to the inhabitant if there is one
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There's no one here to talk to.")

    # If the user types 'fight', attempt to fight with the inhabitant
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input("Enter item here: ").lower()
            if inhabitant.fight(fight_with):
                print(f"You defeated {inhabitant.name}!")
                current_room.set_character(None)  # Remove defeated enemy
            else:
                print(f"{inhabitant.name} has defeated you. Game over.")
                break  # End the game if the player loses the fight
        else:
            print("There's no one here to fight.")

    # If the user types 'hug', hug the friend
    elif command == "hug":
        if inhabitant is not None and isinstance(inhabitant, Friend):
            inhabitant.hug()
        else:
            print("There's no one here to hug.")

    # If the user types 'gift', offer a gift to the friend
    elif command == "gift":
        if inhabitant is not None and isinstance(inhabitant, Friend):
            gift = input("What would you like to offer as a gift? ")
            inhabitant.offer_gift(gift)
        else:
            print("There's no one here to give a gift to.")

    # If the user types 'take', collect the item if there is one
    elif command == "take":
        if item is not None:
            print(f"You put the {item.get_name()} in your inventory.")
            inventory.append(item.get_name())  # Add item to inventory
            current_room.set_item(None)  # Remove the item from the room
        else:
            print("There's nothing to take here.")

    # Unrecognized command
    else:
        print("I don't understand that command.")

print("Thank you for playing!")