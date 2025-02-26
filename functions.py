# functions are named blocks of code designed to do specifically one job 
# A function is a block of reusable code designed to perform a specific task.
def greet_user():
    """Display a simple greeting"""
    print(f"Goodmorning Eria")

greet_user()


# Passing Information to a Function
def greet_user(name):
    """Display a simple greeting"""
    print(f"Goodmorning {name}")

greet_user("Kamwada")
greet_user("Opio")


# Arguments and Parameters
# in the preious function name is a parameter and opio, kamwada are the arguments
# eople sometimes speak of arguments and parameters interchangeably. 
# Don’t be surprised if you see the variables in a function definition referred to as arguments or the
# variables in a function call referred to as parameters.

# Try it yourself
# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
#  Call the function, and make sure the message displays correctly.
def display_message():
    """Tell people what am learning about"""
    print(f"Hey everyone, am learning about Functions")

display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.
def favorite_book(title):
    """Print my favorite book"""
    print(f"One of my favorite books is {title}")

favorite_book("Harry Potter")
favorite_book("Dune")



# Passing Arguments
# We can pass as many arguments as is the number of parameters
# 1. Positional arguments 
# These need to be in the same order the parameters were written 
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet("Dog", "Max")
describe_pet("Cat", "Doug")
# order matters in positonal arguments 

# 2. Keyword arguments 
# This is a name-value pair that we pass as arguments 
# when you use keyword arguments, be sure to use the exact names of the parameters in
# the function’s definition.
describe_pet(pet_name="Jack", animal_type="Human")


# Default Values
# When writing a function, you can define a default value for each parameter.
# If an argument for a parameter is provided in the function call, Python uses the argument value. 
# If not, it uses the parameter’s default value. 
def describe_pet(pet_name, animal_type="dog" ):
    """Display information about a pet"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet("Max")
describe_pet("Cat", "Doug")
# when you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values.


# TRY IT YOURSELF 
# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
def make_shirt(size, shirt_message):
    """Displays about the shirts to be printed"""
    print(f"A {size} shirt is to be made with a '{shirt_message}' message")

make_shirt("Large", "You cant see me")
make_shirt(shirt_message="The big Dog", size="Medium")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
def make_shirt(size="Large", shirt_message="I love Python"):
    """Displays about the shirts to be printed"""
    print(f"A {size} shirt is to be made with a '{shirt_message}' message")

make_shirt()
make_shirt(size="Medium")
make_shirt(size="Small", shirt_message="I hate C++")

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country
def describe_city(city, country="Uganda"):
    """Display location of cities"""
    print(f"{city} is in {country}")
describe_city("Kampala")
describe_city("Nairobi", "Kenya")
describe_city("Naguru")


# Return Values 
# A function doesnt have to always print out something 
# Instead, it can process some data and then return a value or set of values.
# The value the function returns is called a return value
def get_formatted_name(first_name, last_name):
    """Return neatly formatted fullname"""
    return(f"{first_name} {last_name}")

musician = get_formatted_name(first_name="Alien", last_name="Skin")
print(musician)
musician = get_formatted_name("Bobi", "Wine")
print(musician)


# Making an argument optional 
# Sometimes it makes sense to make an argument optional so that people
# using the function can choose to provide extra information only if they
# want to
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return neatly formatted fullname"""
    if middle_name:
        return(f"{first_name} {middle_name} {last_name}")
    else:
        return(f"{first_name} {last_name}")
    
print(get_formatted_name(first_name="Doctor", middle_name="Jose", last_name="Chameleone"))
print(get_formatted_name(first_name="Kendrick", last_name="Lamar"))


# Using a Function with a while Loop
# while True:
#     first_name = input("\nEnter first name: ")
#     if first_name.strip().lower() == "q":
#         break
#     middle_name = input("Enter middle name: ")
#     if middle_name.strip().lower() == "q":
#         break
#     last_name = input("Enter last name: ")
#     if last_name.strip().lower() == "q":
#         break


#     print(get_formatted_name(first_name=first_name, middle_name=middle_name, last_name=last_name))


# TRY IT YOURSELF 
# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.
def city_country(city, country):
    """Display city and their country"""
    return(f"{city.title()}, {country.title()}")

print(city_country(city="Kampala", country="Uganda"))
print(city_country(city="Paris", country="France"))
print(city_country(city="Nairobi", country="Kenya"))

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.
def make_album(artist_name, album_title, number_of_songs=None):
    """Describe a music album"""
    album = {"Name of artist": artist_name, "Title of album": album_title}
    
    if number_of_songs:
        album["Number of songs"] = number_of_songs

    return(album)

print(make_album(artist_name="Bobiwine", album_title="Revolutionary"))
print(make_album(artist_name="Alien Skin", album_title="Nkoola Festival", number_of_songs=5))
print(make_album(artist_name="A Pass", album_title="Blend of Quality"))

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.
# while True:
#     artist_name = input("\nEnter the name of artist: ")
#     if artist_name.strip().lower() == "q":
#         break

#     album_title = input("Enter the title of Album: ")
#     if album_title.strip().lower() == "q":
#         break

#     number_of_songs = input("Enter the number of songs in album: ")
#     if number_of_songs.strip().lower() == "q":
#         break

#     print(make_album(artist_name=artist_name, album_title=album_title, number_of_songs=number_of_songs))


# TRY IT YOURSELF 
# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.
def show_messages(messages):
    """Displays messages"""
    for message in messages:
        print(message)

messages = ["Hey there", "Good night", "Have a great day", "Have you eaten lunch already"]
show_messages(messages)


# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
print()
print(messages)
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
    # for message in messages:
    #     print(message)
    #     sent_messages.append(message)
    #     messages.remove(message)

sent_messages = []
print(sent_messages)
send_messages(messages, sent_messages)
print(messages)
print(sent_messages)

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.
print()
sent_messages = []
messages = ["Hey there", "Good night", "Have a great day", "Have you eaten lunch already"]
print(sent_messages)
print(messages)
print(sent_messages)
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)


# Passing an Arbitrary Number of Arguments
# sometimes you wont know how many arguments a function may need 
# thats where arbitrary arguments come in 
# consider a function for ordering a pizza but dont know how many toppings a person may need 
def make_pizza(*toppings):
    """Display a list of toppings"""
    print(toppings)

make_pizza("Mushrooms")
make_pizza("Pineapple", "Pepperoni", "Burger")

# The asterisk in the parameter name *toppings tells Python to make an
# empty tuple called toppings and pack whatever values it receives into this tuple.

# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the
# parameter that accepts an arbitrary number of arguments must be placed
# last in the function definition
def make_pizza(size, type, *toppings):
    """Display a list of toppings"""
    print(f"Making a {size} pizza of {type} with the following toppings")
    for topping in toppings:
        print(f" - {topping}")

make_pizza("Large", "Chicken", "Mushrooms")
make_pizza("Small", "Beef", "Pineapple", "Pepperoni", "Burger")


# Using Arbitrary Keyword Arguments
def build_profile(first_name, last_name, **user_info):
    """Displaying user info"""
    user_info["First name"] = first_name
    user_info["Last name"] = last_name
    return user_info

user1 = build_profile("Talemwa", "Eria", age=30, location="Kampala")
print(user1)
# The double asterisks before the parameter **user_info cause Python to create
# an empty dictionary called user_info and pack whatever name-value pairs
# it receives into this dictionary



# TRY IT YOURSELF 
# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the 
# sandwich that’s being ordered. Call the function three times, using a different
#  number of arguments each time
def make_sandwich(*toppings):
    """Summary of the ordered sandwich"""
    print("\nBelow is a summary of the ordered sandwich")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich("Katogo", "Beef")
make_sandwich("Onions", "pepperoni", "Oranges")


# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
# profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.
def build_profile(first_name, last_name, **other_info):
    other_info["First name"] = first_name
    other_info["Last name"] = last_name
    print(f"\nBelow is my profile")
    for key, value in other_info.items():
        print(f"{key}:\t{value}")
    # return other_info

build_profile("Talemwa", "Jackson")
build_profile("Wabwiire", "Jackson", age=63, location="Arua")


# 8-14. Cars: Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.
def car_information(manufacturer, model, **kwargs):
    """Stores information about a car"""
    kwargs["Manufacturer"] = manufacturer
    kwargs["Model"] = model

    print("Below is information about my car")
    for key, value in kwargs.items():
        print(f"{key}:\t{value}")

car_information('subaru', 'outback', color='blue', tow_package=True)


# Storing Your Functions in Modules


