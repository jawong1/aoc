import math

# Initialize for the two columns
column1 = []
column2 = []

# Open the file for reading
with open('input_day1.txt', 'r') as file:
    for line in file:
        # Split the line into two parts and convert to numbers
        num1, num2 = map(int, line.split())  
        # Append each number to its respective column
        column1.append(num1)
        column2.append(num2)

    # Sort columns 1 & 2
    column1.sort()
    column2.sort()

# Get the running sum of the differences
running_sum = 0
for i in range(len(column1)):
    running_sum += abs(column1[i] - column2[i])
print(running_sum)

