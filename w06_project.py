# Creativity: In addition to the required analysis by year,
# this program allows the user to enter a country and view its minimum,
# maximum, and average life expectancy across the dataset.

lowest_life = float("inf")
highest_life = float("-inf")

min_country = ""
min_year = ""

max_country = ""
max_year = ""

# Ask the user for a year
year_of_interest = input("Enter the year of interest: ")

year_total = 0
year_count = 0

year_min = float("inf")
year_max = float("-inf")

year_min_country = ""
year_max_country = ""

with open("life-expectancy.csv") as file:

    # Skip the header
    next(file)

    for line in file:
        parts = line.strip().split(",")

        country = parts[0]
        year = parts[2]
        life_expectancy = float(parts[3])

        # Overall minimum
        if life_expectancy < lowest_life:
            lowest_life = life_expectancy
            min_country = country
            min_year = year

        # Overall maximum
        if life_expectancy > highest_life:
            highest_life = life_expectancy
            max_country = country
            max_year = year

        # Statistics for the chosen year
        if year == year_of_interest:
            year_total += life_expectancy
            year_count += 1

            if life_expectancy < year_min:
                year_min = life_expectancy
                year_min_country = country

            if life_expectancy > year_max:
                year_max = life_expectancy
                year_max_country = country

# Compute average
if year_count > 0:
    year_average = year_total / year_count
else:
    year_average = 0
print()
print(f"The overall max life expectancy is: {highest_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {lowest_life} from {min_country} in {min_year}")

print()
print(f"For the year {year_of_interest}:")
print(f"The average life expectancy across all countries was {year_average:.2f}")
print(f"The max life expectancy was in {year_max_country} with {year_max}")
print(f"The min life expectancy was in {year_min_country} with {year_min}")

# ----------------------------
# Creativity section
# ----------------------------

country_interest = input("\nEnter a country to analyze: ")

country_total = 0
country_count = 0
country_min = float("inf")
country_max = float("-inf")

with open("life-expectancy.csv") as file:

    next(file)

    for line in file:
        parts = line.strip().split(",")

        country = parts[0]
        life_expectancy = float(parts[3])

        if country.lower() == country_interest.lower():
            country_total += life_expectancy
            country_count += 1

            if life_expectancy < country_min:
                country_min = life_expectancy

            if life_expectancy > country_max:
                country_max = life_expectancy

if country_count > 0:
    country_average = country_total / country_count

    print(f"\nStatistics for {country_interest}:")
    print(f"Average life expectancy: {country_average:.2f}")
    print(f"Minimum life expectancy: {country_min}")
    print(f"Maximum life expectancy: {country_max}")
else:
    print(f"\nNo data found for {country_interest}.")