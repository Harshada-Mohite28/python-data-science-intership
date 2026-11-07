# Python File Handling

# Writing data into a file
file = open("student.txt", "w")
file.write("Hello Harshada!\n")
file.write("I am learning Python and Data Science.")
file.close()

# Reading data from a file
file = open("student.txt", "r")
data = file.read()

print("File Content:")
print(data)

file.close()
