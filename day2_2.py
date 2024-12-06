import math

# Initialize a list
list1 = []
running_sum = 0

# let's check if da list is safe
def check_if_safe(some_list):

    # vars 
    is_decreasing = 789
    temp = 987
    good_flag = 1

    # start loopin through list
    for i in range(len(some_list) - 1):

        # set up vars
        temp = is_decreasing
        good_flag = 1

        # if difference is not equal or between 1 to 3 then not safe
        if not (1 <= abs(some_list[i] - some_list[i+1]) <= 3):
            good_flag = 0
            break

        # check if decreasing
        if some_list[i] - some_list[i+1] > 0:
            is_decreasing = 1
            # if is_decreasing not equal to previous state, then not good
            if is_decreasing != temp and i != 0:
                good_flag = 0
                break

        # check if increasin
        else: 
            is_decreasing = 0
            # if is_decreasing not equal to previous state, then not good
            if is_decreasing != temp and i != 0:
                good_flag = 0
                break
    
    # show if safe or not
    return True if good_flag == 1 else False

# Open the file for reading
with open('input_day2.txt', 'r') as file:
    for line in file:
        # Split the line into two parts and convert to numbers
        list1 = list(map(int, line.split()))
        print(list1)

        # if all is well (safe), add 1 to running sum
        if check_if_safe(list1) == True:
            running_sum += 1    

        # let do sum extra checkity if not safey safe
        else:
            list1_mod = []
            i = 0
            safe_or_nah = False
            while safe_or_nah == False and i < len(list1):
                list1_mod = list1.copy()
                list1_mod.pop(i)
                safe_or_nah = check_if_safe(list1_mod)
                if safe_or_nah == True:
                    running_sum += 1
                    break
                i += 1
        
    print(running_sum)


