from character import Enemy 

# Create an Enemy instance
dave = Enemy("Dave", "A smelly zombie")
dave.describe()

# Set conversation and have Dave talk
dave.set_conversation("Hi, I'm Dave, and I will bite.")
dave.talk()

# Set Dave's weakness
dave.set_weakness("cheese")

# Ask the user what they want to fight with
print("What will you fight with?")
fight_with = input("Enter item here: ")

# Fight Dave and handle the result
if dave.fight(fight_with):
    print("You won the fight!")
else:
    print("You lost the fight!")

                 