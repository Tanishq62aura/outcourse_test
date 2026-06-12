students = ["Rahul", "Priya", "Rohan", "Sneha", "Amit"]

print("Original List:", students)

students.append("Ravi")
students.insert(2, "Neha")
print("After Adding:", students)

students.remove("Amit")
students.pop(1)
print("After Removing:", students)

students.sort()
print("Sorted List:", students)
print("Reverse Order:", students[::-1])
print("First 3 Elements:", students[:3])