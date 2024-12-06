import re

file_path = 'input_day3.txt'  # Replace with your actual file path
with open(file_path, 'r') as file:
    text = file.read()

pattern = r"mul\((\d+),\s*(\d+)\)"  # Matches mul(number1, number2)

matches = re.findall(pattern, text)  # Returns a list of tuples [(num1, num2), ...]

running_sum = 0
for match in matches:
    num1 = int(match[0])  # Convert first number to integer
    num2 = int(match[1])  # Convert second number to integer
    prod = num1*num2
    running_sum += prod

print(running_sum)