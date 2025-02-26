# # # Student Grade Calculator
# # # ----------------------------------
# # # You are a teacher with the following student test scores:
# # # student_grades = {
# # #     "Alice": [85, 92, 78],
# # #     "Bob": [88, 86, 92],
# # #     "Charlie": [75, 82, 79]
# # # }

# # # Tasks:
# # # a) Calculate and return the average grade for each student
# # # b) Add a new test score of 90 for Alice
# # # c) Find and return the name of the student with the highest average

# # student_grades = {
# #     "Alice": [85, 92, 78],
# #     "Bob": [88, 86, 92],
# #     "Charlie": [75, 82, 79]
# # }

# # averages = {}

# # # (a)
# # for key, value in student_grades.items():
# #     sum = 0
# #     for num in value:
# #         sum = sum + num
# #         average = sum / len(value)
# #         averages[key] = average
# #     print(f"{key}: Average={average:.2f}")

# # # (b)
# # student_grades["Alice"].append(90)

# # print(student_grades)
# # print(averages)
# # max_average = 0
# # best_student = ""
# # for key, value in averages.items():
# #     if value > max_average:
# #         max_average = value
# #         best_student = key
    
# # print(f"Best student is {best_student} with an average of {max_average}\n\n")



# # # Store Inventory Manager
# # # ---------------------------------
# # # You manage a small grocery store with this inventory:
# # # inventory = {
# # #     "apple": {"price": 0.50, "quantity": 100},
# # #     "banana": {"price": 0.75, "quantity": 150},
# # #     "orange": {"price": 0.60, "quantity": 75}
# # # }

# # # Tasks:
# # # a) Return all products with quantity less than 80
# # # b) Calculate the total value of your inventory (price * quantity for each item)
# # # c) Update the price of bananas to $0.80

# # # Example output for part a):
# # # {"orange": 75}

# # inventory = {
# #     "apple": {"price": 0.50, "quantity": 100},
# #     "banana": {"price": 0.75, "quantity": 150},
# #     "orange": {"price": 0.60, "quantity": 75}
# # }

# # # (a)
# # low_stock_items = {}
# # for key, value in inventory.items():
# #     if value["quantity"] < 80:
# #         low_stock_items[key] = value["quantity"]

# # print(low_stock_items) 

# # # (b)
# # sum = 0
# # for key, value in inventory.items():
# #     amount = value["quantity"] * value["price"]
# #     sum += amount
# # print(sum)

# # # (c)
# # inventory["banana"]["price"] = 0.8
# # print(inventory)



# # Word Frequency Analyzer
# # ---------------------------------
# # Given this sentence: "the quick brown fox jumps over the lazy dog"

# # Tasks:
# # a) Returns a dictionary with the count of each word
# # b) Find the most frequently used word
# # c) Add functionality to ignore common words like "the" and "and"

# # Example output for part a):
# # {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}


# sentence = "the quick brown fox jumps over the lazy dog"
# sentence = sentence.split()
# print(sentence)
# word_count_dict = {}

# # for word in sentence:
# #     word_count = sentence.count(word)
# #     word_count_dict[word] = word_count

# # print(word_count_dict)


# for word in sentence:
#     if word in word_count_dict.keys():
#         word_count_dict[word] += 1
#     else:
#         word_count_dict[word] = 1
# print(word_count_dict)

# # most frequently used word 
# highest_count = 0
# frequently_used_word = ""
# for word, word_count in word_count_dict.items():
#     if word_count > highest_count:
#         highest_count = word_count
#         frequently_used_word = word
# print(f"Frequently used word is {frequently_used_word}")



# Contact Manager
# --------------------------
# Start with this phone directory:
# phone_directory = {
#     "John Smith": "555-0123",
#     "Mary Johnson": "555-4567",
#     "David Wilson": "555-8901"
# }

# Tasks:
# a) add a new contact, making sure you don't duplicate entries
# b) delete a contact
# c) update an existing contact's number
# d) find all contacts that start with a given letter

# Example output for part d) with letter "M":
# {"Mary Johnson": "555-4567"}


phone_directory = {
    "John Smith": "555-0123",
    "Mary Johnson": "555-4567",
    "David Wilson": "555-8901"
}