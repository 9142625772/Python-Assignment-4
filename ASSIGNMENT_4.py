#Module 5: Files, Exceptions, and Errors in Python
#Task 1: Read a File and Handle Errors
'''
1. Opens and reads a text file named sample.txt.
2. Prints its content line by line.

'''
file1=open("sample.txt","r")
reading=file1.read()
print(reading)
file1.close()

#3. Handles errors gracefully if the file does not exist.

try:
    file1=open("sample.txt","r")
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
    
'''
Task 2: Write and Append Data to a File


1. Takes user input and writes it to a file named output.txt.

2. Appends additional data to the same file.

3. Reads and displays the final content of the file.
'''
user=input("Enter text to write to the file:")

file1=open("output.txt","w")
writing=file1.write(user +"\n")
print(writing)
file1.close()
print("Data successfully written to output.txt.")

user1=input("Enter additional text to append:")
file1=open("output.txt","a")
appending=file1.write(user1 +"\n")
print(appending)
file1.close()
print("Data successfully appended")

file1=open("output.txt","r")
reading=file1.read()
print("Final content of output.txt:\n",reading)
file1.close()