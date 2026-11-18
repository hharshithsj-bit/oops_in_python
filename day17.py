


file = open("student.txt", "w")
file.write("Welcome to Python Day 17!\n")
file.write("I am learning File Handling.\n")
file.write("My goal is to become a software engineer.")
file.close()

print("File created successfully!")


file = open("student.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()


file = open("student.txt", "a")
file.write("\nI practice Python every day.")
file.close()

print("\nNew information added!")


with open("student.txt", "r") as file:
    print("\nUpdated File Content:")
    print(file.read())
