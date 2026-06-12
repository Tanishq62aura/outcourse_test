with open("employee.txt", 'w') as f:
    f.write("tom\n")
    f.write("sam\n")
    f.write("tobey\n")

with open("employee.txt", 'r') as f:
    
    print(f.read())

with open("employee.txt", 'w') as f:
    f.write("ravi\n")
    f.write("charles\n")

    print("updated")

with open("employee.txt", 'r') as f:

    print(f.read())