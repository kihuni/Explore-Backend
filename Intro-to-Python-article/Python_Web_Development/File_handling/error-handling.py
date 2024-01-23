try:
    # Attempting to open a file that may not exist
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("File read successfully.")
finally:
    print("File handling process completed.")
