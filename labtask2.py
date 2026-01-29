# 1. Tuple with 10 elements (Int, Float, String)
my_tuple = (1, 2.5, "hello", 42, 3.14, "world", 7, 8.8, "python", 100)
print("1. Tuple:", my_tuple)

# 2. Count specific element in tuple
count_element = my_tuple.count(2.5)
print("2. Count of 2.5:", count_element)

# 3. Convert tuple to list, modify, convert back to tuple
tuple_list = list(my_tuple)
tuple_list[0] = 999
modified_tuple = tuple(tuple_list)
print("3. Modified tuple:", modified_tuple)

# 4. Nested tuple and access inner elements
nested_tuple = (1, 2, (10, 20, 30), 4)
print("4. Inner tuple element:", nested_tuple[2][1])

# 5. Set with 7 elements (Int, Float, String)
my_set = {1, 2.5, "apple", 42, 3.14, "banana", 7}
print("5. Set:", my_set)

# 6. Add single and multiple elements to set
my_set.add(100)
my_set.update([200, 3.5, "orange"])
print("6. Set after add and update:", my_set)

# 7. Remove elements using remove() and discard()
my_set.remove(100)
my_set.discard(200)
print("7. Set after remove and discard:", my_set)

# 8. Union of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
print("8. Union:", union_set)

# 9. Intersection of two sets
intersection_set = set1.intersection(set2)
print("9. Intersection:", intersection_set)

# 10. Dictionary of 3 students with marks
students = {"Alice": 85, "Bob": 92, "Charlie": 78}
print("10. Students:", students)
for key, value in students.items():
    print(f"   {key}: {value}")

# 11. Add new key-value pair
students["Diana"] = 88
print("11. After adding Diana:", students)

# 12. Access value using key
print("12. Alice's marks:", students["Alice"])

# 13. Add new key-value pair using assignment
students["Eve"] = 95
print("13. After adding Eve:", students)

# 14. Update existing value
students["Bob"] = 94
print("14. After updating Bob:", students)

# 15. Remove key-value pair using pop() and del
students.pop("Charlie")
del students["Diana"]
print("15. After removing Charlie and Diana:", students)

# 16. Print keys and values using .items()
print("16. All students and marks:")
for key, value in students.items():
    print(f"   {key}: {value}")

# 17. Number of items in dictionary
print("17. Number of students:", len(students))

# 18. Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print("18. Merged dictionary:", dict1)

