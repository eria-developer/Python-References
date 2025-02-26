my_list = ['John', 'Peter', 'Debbie', 'Charles']

# Getting values with indexes
my_list = ['John', 'Peter', 'Debbie', 'Charles']
print(my_list[2])


# Negative indexes
my_list = ['John', 'Peter', 'Debbie', 'Charles']
print(my_list[-2])


# Getting sublists with Slices
my_list = ['John', 'Peter', 'Debora', 'Charles']
new_list = my_list[1:3]
another_list = my_list[0:-1]
to_the_end_list = my_list[1:]
from_the_beginning_list = my_list[:-2]
new_exact_list = my_list[:]
print(new_list)
print(another_list)
print(to_the_end_list)
print(from_the_beginning_list)


# Getting a list length with len()
my_list = ['John', 'Peter', 'Debora', 'Charles']
print(len(my_list))


# Changing values with indexes
my_list = ['John', 'Peter', 'Debora', 'Charles']
print(f"My list is {my_list}")
my_list[1] = "Jack"
print(f"My new list is {my_list}")


# Concatenation and Replication
list_a = ["hey", "you", "there"]
list_b = [2, 5, "Ayabas"]
print(list_a + list_b)
print(list_a * 2)
new_list = list_a + list_b + ["Jack"]
print(new_list)


# Using for loops with Lists
my_list = ['John', 'Peter', 'Debora', 'Charles']
for name in my_list:
    print(name)


# Getting the index in a loop with enumerate()
print()
for index,name in enumerate(my_list):
    print(f"Name {index + 1}: {name}")
print()


# Loop in Multiple Lists with zip()
names = ['John', 'Peter', 'Debora', 'Charles']
ages = [19, 23, 18, 12]
for name, age in zip(names, ages):
    print(f"{name.title()} is {age} years old")
print()


# The in and not in operators
names = ['John', 'Peter', 'Debora', 'Charles']
print("john".title() in names)
print()


# The Multiple Assignment Trick
names = ['John', 'Peter', 'Debora', 'Charles']
first_name, last_name = names[0], names[-1]
print(first_name, last_name)

first_name, last_name, middle_name = ["Talemwa", "eria", "Jackson"]
print(f"Firstname: {first_name.title()}")
print(f"Lastname: {last_name.title()}")
print(f"Middlename: {middle_name.title()}")
print()


# The index Method
# The index method allows you to find the index of a value by passing its name:
names = ['John', 'Peter', 'Debora', 'Charles']
print(names.index("John"))
print()


# ADDING VALUES 
# Append Method
# It adds an element to the end of the list 
names = ['John', 'Peter', 'Debora', 'Charles']
names.append("Kajumba")
print(names)
print()


#insert()
# Adds an element to a list at a certain index
names = ['John', 'Peter', 'Debora', 'Charles']
names.insert(1, "Frank")
print(names)
print()


# REMOVING VALUES 
# del() => Removes an item using the index
names = ['John', 'Peter', 'Debora', 'Charles']
del(names[1])
print(names)
del names[1]
print(names)
print()

# remove()  => This removes an item using its actual value
# If the value appears multiple times in the list, only the first instance of the value will be removed.
names = ['John', 'Peter', 'Debora', 'John', 'Charles']
names.remove("John")
print(names)
print()

# pop()
# pop removes and returns the last item of the list. You can also pass the index of the element as an optional parameter:
names = ['John', 'Peter', 'Debora', 'John', 'Charles']
popped_element = names.pop()
print(f"Pooped Element: {popped_element}")
print(f"New List: {names}")
popped_element = names.pop(0)
print(f"Pooped Element: {popped_element}")
print(f"New List: {names}\n")

# clear() => This one clears the entire list


# Sorting values with sort()
numbers = [5, 2, -6, 4, 0, -9]
numbers.sort()
print(numbers)
names = ['John', 'Peter', 'Debora', 'john', 'Charles']
names.sort()
print(names)
# You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order:
numbers.sort(reverse=True)
print(numbers)
# If you need to sort the values in regular alphabetical order, pass str.lower for the key keyword argument in the sort() method call:
letters = ['a', 'z', 'A', 'Z']
letters.sort()
print(letters)
letters.sort(key=str.lower)
print(letters)

# You can use the built-in function sorted to return a new list:
numbers = [5, 2, -6, 4, 0, -9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

