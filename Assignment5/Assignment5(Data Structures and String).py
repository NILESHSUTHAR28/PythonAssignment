# Task 1
marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

name = input("Enter the student's name: ")

if name in marks:
    print(f"{name} is {marks[name]}")
else:
    print(f"Student not found.")


# Task 2
number = [1,2,3,4,5,6,7,8,9,10]


first_five = number[:5]

reverse_number = first_five[::-1]

print(f"Original List: {number}")
print(f"Extracted first five elements: {first_five}")
print(f"Reversed extracted elements: {reverse_number}")
