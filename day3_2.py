import re

file_path = './aoc-2024/input_day3.txt'  # Replace with your actual file path
with open(file_path, 'r') as file:
    text = file.read()

# text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))" # hardcoded for debugging. answer is 48.

running_sum = 0

num_pattern = r"mul\((\d+),\s*(\d+)\)"  # Matches mul(number1, number2)

state_pattern = r"do\(\)|don't\(\)" # Matches do() or don't()

split_text = re.split(state_pattern, text)
segment_indicators = re.findall(state_pattern, text)
segment_indicators.insert(0, "do()")
split_text_with_indicators = zip(segment_indicators, split_text) # need to insert a "do()" for the first element to get to indicators to line up correct since default state is True
# print(list(split_text_with_indicators))

for indication, segment in split_text_with_indicators:
    if 'do()' in indication:
        # print(indication)
        # print(segment)
        num_matches = re.findall(num_pattern, segment)
        # print(num_matches)
        for match in num_matches:
                num1 = int(match[0])  # Convert first number to integer
                num2 = int(match[1])  # Convert second number to integer
                prod = num1*num2
                running_sum += prod
    
print(running_sum)