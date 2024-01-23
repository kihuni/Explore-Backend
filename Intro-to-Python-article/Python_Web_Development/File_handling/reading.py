# Open the file in read mode
file_path = "Intro-to-Python-article/Python_Web_Development/File_handling/file.txt"
file = open(file_path, "r")

# Read the contents of the file
file_contents = file.read()

# Print the contents of the file
print(file_contents)

# Close the file
file.close()
