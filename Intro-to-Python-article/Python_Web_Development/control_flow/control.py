# if-else statement
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

# for loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# break statement
for num in numbers:
    if num == 3:
        break
    print(num)

# continue statement
for num in numbers:
    if num == 3:
        continue
    print(num)

# nested if-else statement
y = 5
if x > 0:
    if y > 0:
        print("Both x and y are positive")
    else:
        print("x is positive but y is non-positive")
else:
    print("x is non-positive")

# try-except statement
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# switch-case statement (using dictionary)
def switch_case(case):
    switch = {
        1: "Case 1",
        2: "Case 2",
        3: "Case 3"
    }
    return switch.get(case, "Invalid case")

print(switch_case(2))
