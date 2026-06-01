# Adventure Game Project
# I added extra creative paths, hidden treasure outcomes, and multiple endings.
# I also tested this game with friends to make sure different choices worked correctly.

print("Welcome to the Lost Island Adventure Game!")
print("You wake up on a mysterious island after a shipwreck.\n")

choice1 = input(
    "You see a CAVE, a FOREST, and a RIVER. "
    "Where do you want to go? "
).lower()

# FIRST LEVEL
if choice1 == "cave":

    print("\nYou enter the dark cave and hear strange noises.")

    choice2 = input(
        "Do you want to LIGHT a torch, EXPLORE deeper, or LEAVE the cave? "
    ).lower()

    # SECOND LEVEL
    if choice2 == "light":

        print("\nThe torch reveals ancient drawings on the wall.")

        choice3 = input(
            "Do you want to TOUCH the wall or KEEP WALKING? "
        ).lower()

        # THIRD LEVEL
        if choice3 == "touch":
            print("\nA secret door opens and you discover hidden treasure!")
            print("YOU WIN!")

        elif choice3 == "keep walking":
            print("\nYou fall into a hidden pit.")
            print("GAME OVER!")

        else:
            print("\nInvalid choice. The cave collapses.")
            print("GAME OVER!")

    elif choice2 == "explore":

        print("\nYou walk deeper and meet a giant sleeping bear.")

        choice3 = input(
            "Do you want to RUN or HIDE? "
        ).lower()

        if choice3 == "run":
            print("\nYou escape safely from the cave!")
            print("YOU SURVIVED!")

        elif choice3 == "hide":
            print("\nThe bear wakes up and finds you.")
            print("GAME OVER!")

        else:
            print("\nInvalid choice. The bear wakes up.")
            print("GAME OVER!")

    elif choice2 == "leave":

        print("\nYou safely leave the cave and find a rescue boat.")

        choice3 = input(
            "Do you want to BOARD the boat or WAIT on the shore? "
        ).lower()

        if choice3 == "board":
            print("\nThe boat takes you home safely.")
            print("YOU WIN!")

        elif choice3 == "wait":
            print("\nA storm arrives and you are stranded.")
            print("GAME OVER!")

        else:
            print("\nInvalid choice. You miss your chance to escape.")
            print("GAME OVER!")

    else:
        print("\nInvalid choice. You get lost in the cave.")
        print("GAME OVER!")

# FOREST PATH
elif choice1 == "forest":

    print("\nYou walk into the thick forest.")

    choice2 = input(
        "Do you want to CLIMB a tree or FOLLOW a sound? "
    ).lower()

    if choice2 == "climb":

        print("\nFrom the top of the tree, you spot smoke nearby.")

        choice3 = input(
            "Do you want to GO to the smoke or STAY in the tree? "
        ).lower()

        if choice3 == "go":
            print("\nYou find friendly villagers who help you.")
            print("YOU WIN!")

        elif choice3 == "stay":
            print("\nYou fall asleep and fall from the tree.")
            print("GAME OVER!")

        else:
            print("\nInvalid choice. Wild animals attack.")
            print("GAME OVER!")

    elif choice2 == "follow":

        print("\nYou discover an abandoned camp.")

        choice3 = input(
            "Do you want to SEARCH the camp or LEAVE quickly? "
        ).lower()

        if choice3 == "search":
            print("\nYou find food and a map to safety.")
            print("YOU WIN!")

        elif choice3 == "leave":
            print("\nYou get lost in the forest forever.")
            print("GAME OVER!")

        else:
            print("\nInvalid choice. You wander aimlessly.")
            print("GAME OVER!")

    else:
        print("\nInvalid choice. You are trapped in the forest.")
        print("GAME OVER!")

# RIVER PATH
elif choice1 == "river":

    print("\nYou arrive at a fast-flowing river.")

    choice2 = input(
        "Do you want to SWIM across or BUILD a raft? "
    ).lower()

    if choice2 == "swim":

        print("\nThe water current is very strong.")

        choice3 = input(
            "Do you want to KEEP SWIMMING or RETURN to shore? "
        ).lower()

        if choice3 == "keep swimming":
            print("\nYou safely reach the other side.")
            print("YOU SURVIVED!")

        elif choice3 == "return":
            print("\nA crocodile attacks near the shore.")
            print("GAME OVER!")

        else:
            print("\nInvalid choice. You drown in the river.")
            print("GAME OVER!")

    elif choice2 == "build":

        print("\nYou build a strong raft.")

        choice3 = input(
            "Do you want to SAIL downstream or TIE the raft first? "
        ).lower()

        if choice3 == "sail":
            print("\nYou discover a nearby rescue station.")
            print("YOU WIN!")

        elif choice3 == "tie":
            print("\nThe raft floats away without you.")
            print("GAME OVER!")

        else:
            print("\nInvalid choice. Your raft breaks apart.")
            print("GAME OVER!")

    else:
        print("\nInvalid choice. You slip into the river.")
        print("GAME OVER!")

# INVALID FIRST INPUT
else:
    print("\nInvalid choice. You remain stranded on the island.")
    print("GAME OVER!")