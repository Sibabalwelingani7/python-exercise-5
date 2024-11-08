# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple", "banana", "grape", "strawberry", "blueberry"]
# TODO: Add a fruit to the end of the list
fruits.append("pineapple")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"kiwi")
# TODO: Remove a fruit from the list
fruits.remove("grape")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1,2,3,4,5]

# TODO: Create a new list with each number squared
squared_numbers = [x**2 for x in numbers]
# TODO: Find the sum and average of the original numbers
total_sum = sum(numbers)
average = total_sum / len(numbers) if numbers else 0
# TODO: Print the results
print(numbers)
print(squared_numbers)
print(average)
#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_and_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

# TODO: Add a new country-capital pair
countries_and_capitals["Italy"] = "Rome"
# TODO: Update the capital of an existing country
countries_and_capitals["Germany"] = "Berlin (updated)"
# TODO: Remove a country-capital pair
del countries_and_capitals["France"]
# TODO: Print the modified dictionary
print(countries_and_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
colors = {
    "apple": "green",
    "banana": "yellow",
    "strawberry": "red",
    "grape": "purple"
}
# TODO: Print all the fruits (keys)

for fruit in colors:
    print(fruit)
# TODO: Print all the colors (values)
# print("Colors:")
# for color in fruits.values():
#     print(color)
print(colors.values())
# TODO: Print each fruit and its color
print("Fruits and their colors:")
# for fruit, color in fruits.items():
#     print(f"{fruit}: {color}")

# TODO: Check if a fruit is in the dictionary and print its color

key = fruit_colors.keys()
values = fruit_colors.get("pineapple")
print(values)