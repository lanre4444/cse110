# W06 Milestone - Life Expectancy Data Analysis

lowest_life = float("inf")
highest_life = float("-inf")

with open("life-expectancy.csv") as file:

    # Skip header row
    next(file)

    for line in file:
        parts = line.strip().split(",")

        life_expectancy = float(parts[3])

        if life_expectancy < lowest_life:
            lowest_life = life_expectancy

        if life_expectancy > highest_life:
            highest_life = life_expectancy

print(f"The lowest life expectancy is: {lowest_life}")
print(f"The highest life expectancy is: {highest_life}")