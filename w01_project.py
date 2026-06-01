# I added an extra color input and additional sentence to make the story more creative and detailed.
print("please enter the following information:")
print()

# Collect words from the user

adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclamation: ")
second_verb = input("Second Verb: ")
third_verb = input("Third Verb: ")
color = input("color: ")

# Leave space before showing the final story

print()
print("Your story is:")
print()

# Create the story using f-strings
# capitalize() makes the exclamation start with a capital letter

print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective} {animal} {verb} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all")
print(f"I could think to do was to {second_verb} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {third_verb}")
print(f"right in front of my family.")
print(f"It was even wearing a bright {color} backpack!")