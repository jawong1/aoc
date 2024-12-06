import math

# Initialize a list
list1 = []
running_sum = 0
is_decreasing = 789
temp = 987
good_flag = 1

# Open the file for reading
with open('input_day2.txt', 'r') as file:
    for line in file:
        # Split the line into two parts and convert to numbers
        list1 = list(map(int, line.split()))
        print(list1)

        for i in range(len(list1) - 1):

            temp = is_decreasing
            good_flag = 1

            # if difference is not equal or between 1 to 3 then not safe
            if not (1 <= abs(list1[i] - list1[i+1]) <= 3):
                good_flag = 0
                break
            
            # check if decrease
            if list1[i] - list1[i+1] > 0:
                is_decreasing = 1
                # if is_decreasing not equal to previous state, then not good
                if is_decreasing != temp and i != 0:
                    good_flag = 0
                    break
            # check if increase
            else: 
                is_decreasing = 0
                # if is_decreasing not equal to previous state, then not good
                if is_decreasing != temp and i != 0:
                    good_flag = 0
                    break
        # if all is well (safe), add 1 to running sum
        if good_flag == 1:
            running_sum += 1    
        
    print(running_sum)


