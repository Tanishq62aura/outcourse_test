with open("test.txt", "w") as f:
    f.write("tom:43\n")
    f.write("sam:83\n")
    f.write("tobey:52\n")
    f.write("peter:43\n")
    f.write("charles:43\n")

with open('test.txt')as f:
    print("student above 80:")

    for i in f:
        name, marks = i.strip().split(":")

        if int(marks) > 80:
            print(name, marks)

