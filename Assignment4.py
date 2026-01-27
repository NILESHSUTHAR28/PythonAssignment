# Module 5: Files, Exceptions, and Errors in Python

# Task 1

try:
    file = open("sample.txt", "r")
    print("Reading file content: ")

    line_no = 1
    for line in file:
        print(f"Line {line_no}: {line.strip()}")
        line_no += 1

    file.close()

except FileNotFoundError:
    print("Error: The file 'Sample.txt' was not found")




# Task 2

text1 = input("Enter text to write to the file: ")

file = open("output.txt", 'w')
file.write(text1 +"\n")
file.close()

print("Data Successfully written to 'output.txt'. ")

text2 = input("Enter additional text to append: ")

file = open("output.txt",'a')
file.write(text2 + "\n")
file.close()

print("Data successfully append to 'output.txt'. ")

print("\nFinal content of 'output.txt'")

file = open("output.txt",'r')
print(file.read())
file.close()