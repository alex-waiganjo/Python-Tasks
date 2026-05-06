subjects = ["Math", "English", "Biology"]

# Insert
# Replace

subjects.insert(1, "Kiswahili")
subjects[0] = 'Cre'

# Question 9
"""
Add 4 tasks
Mark one task as done (remove it)
Print remaining tasks with their index using enumerate()"""

tasks = ["Coding", "Reading", "Swimming", "Dancing"]
tasks[0] = "Done"
print(tasks)
tasks.remove("Done")

print(tasks)

for a, b in enumerate(tasks):
    tasks[a] = b.upper()
# print(tasks)

# print(tasks[0])

# for index, rem_tasks in enumerate(tasks):
#     print(index,rem_tasks)

# You track expenses in a list:

# expenses = [120, 450, 300, 150]
# # Calculate total spending
# # Add a new expense
# # Remove the highest expense
# # enumerate()

# total_spending = sum(expenses)
# expenses.append("380")
# max_expense = max(expenses)
# print(max_expense)

list1 = ["abc", 34, True, 40, "male"]
list2 = ["Alex", True]

print(type(list1))

# Accesing Items in a List
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

# Using the Slicing Method
print(list1[3:])
print(list1[1:3])
print(list1[:3])

# Check if an item exists in a List
if "male" not in list1:
    print("Item Not Found")
else:
    print("Item Found")

# Insert Items
list1.insert(2, "Guava")
print(list1)
list1.append("Kelvin")
print(list1)

# Fruits
fruit_a = ["Mango", "Avocado", "Orange", "Pears"]
fruit_b = ["Banana", "Kiwi", "Pineapple", "Tomatoes"]
fruit_c = ["Potatoes", "Ginger", "Cabbage", "Spinach"]

fruit_a.extend(fruit_b)
fruit_a.extend(fruit_c)
print(fruit_a)

print(fruit_a.index("Mango"))
print(fruit_a.index("Avocado"))
print(fruit_a.index("Cabbage"))

# Remove an Item from a list
initial_length = len(fruit_a)
print(f"Items in our List are {initial_length}")

fruit_a.remove("Mango")
print(f"Items after removal are {len(fruit_a)}")

fruit_a.remove("Avocado")
fruit_a.remove("Spinach")
print(f"Items after removal are {len(fruit_a)}")

print(fruit_a)
print(f"Items are {len(fruit_a)}")

# Remove an Item by Index
fruit_a.pop(7)
print(fruit_a)
print(f"Items are {len(fruit_a)}")

# Delete an Item using del
print(fruit_a)
del fruit_a[3]
print(fruit_a)

if "Kiwi" not in list1:
    print("Item Not Found")
else:
    print("Item Found")

# Clear Items in a list
# fruit_a.clear()
print(fruit_a)


# print(len(fruit_a))

# Using a for Loop
if not fruit_a:
    print("No Items in the List")
else:
    for index, fruit in enumerate(fruit_a, start=2):
        print(f"Index {index}, {fruit}")

# List Comprehensions
get_fruit = [fruit for fruit in fruit_a]
print(get_fruit)
sorted(get_fruit)
print(f"Using sorted {sorted(get_fruit)}")
get_fruit.sort()
print(f"Using .sort {get_fruit}")
# print(get_fruit.sort())
print(sorted(get_fruit))
print(get_fruit)

# get_fruit.reverse()
# reversed(get_fruit)
get_subs = ["Eng", "Kisw", "Chem", "Math", "Anthro", "Busi"]
marks = [30, 33, 22, 55, 7, 9, 0, -9, 5]
print(get_subs)
reversed(get_subs)
print(get_subs)
# reversed(get_subs)
# print(reversed(get_subs))
reversed([30, 33, 22, 55, 7, 9, 0, -9, 5])
marks.sort()
print(marks)
marks.reverse()
print(marks)
print(reversed(marks))

# print(marks)

print(reversed(get_subs))
# print(reversed(get_subs).next())
