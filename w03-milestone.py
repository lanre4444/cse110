# Creativity Addition:
# I added a mystery cave adventure where the player can choose
# different survival tools and face different situations.

print("You are trapped inside a mysterious cave.")
print("You find two items: a ROPE and a TORCH.")

choice = input("Which one do you pick? ").lower()

if choice == "rope":
    print("You grab the rope and climb down safely.")
    print("You discover an underground river.")

elif choice == "torch":
    print("You light the torch and walk deeper into the cave.")
    print("You suddenly hear strange footsteps nearby.")

else:
    print("That is not a valid choice.")