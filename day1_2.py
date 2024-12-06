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

# Get the running sum of the similarity scores
running_sum = 0
for i in range(len(column1)):
    running_sum += (column1[i] * column2.count(column1[i]))
print(running_sum)

