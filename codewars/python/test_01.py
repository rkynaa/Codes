# x = str(input("Enter 4 digit number: "))
# x1 = int(x[0:2])
# x2 = int(x[2:4])

# res = x1+x2
# res = str(res**2)
# res01 = int(res[0:2]) is x1
# res02 = int(res[2:4]) is x2

# if ((res01) and (res02)):
#     print("The number entered is a semi-square number")
# else:
#     print("The number entered is not a semi-square number")

# age = int(input("Enter your age: "))
# weight = int(input("Enter your weight: "))
# height = float(input("Enter your height: "))

# bmi = weight / (height ** 2)

# if (age >= 13 and age <= 17):
#     if (bmi >= 18.50 and bmi <= 24.99):
#         print("Congratulations you can enter military high school")
#     else: 
#         print("You are not qualified to enter military high school")
# else: 
#     print("You are not qualified to enter military high school")

# ales = float(input("Enter ALES score: "))
# foreign = float(input("Enter the foreign language score: "))
# gpa = float(input("Graduation GPA: "))

# res = (ales * 0.5) + (foreign * 0.25) + (gpa * 0.25)

# print("Your ranking score: ", res)
# if (res >= 60):
#     print("May enter the rankings")
# else:
#     print("May not enter the rankings")

# first_num = int(input("Enter your first number: "))
# second_num = int(input("Enter your second number: "))

# number = first_num
# result_list = []
# separator = ', '
# result = ''

# while (number <= second_num):
#     if (number % 4 == 0 and number % 7 == 0):
#         result_list.append(str(number))
#     number += 1

# result = separator.join(result_list)
# print('-----------------------------')
# print(result)
# print(len(result_list), "pieces in total")

# first_num = 100
# last_num = 999

# number = first_num
# result_list = []
# separator = ', '
# result = ''

# while (number <= last_num):
#     first_digit = int(str(number)[0:1])
#     second_digit = int(str(number)[1:2])
#     third_digit = int(str(number)[2:3])

#     temp = (first_digit * second_digit * third_digit) * (first_digit + second_digit + third_digit)
#     if (temp == number):
#         result_list.append(str(number))
#     number += 1

# result = separator.join(result_list)
# print('Numbers searched:', result)
# print('There are', len(result_list), 'three-digit numbers with this feature.')

# def gcd(first_num, second_num):
#     if (first_num == second_num):
#         return first_num
#     else:
#         if (first_num > second_num):
#             return gcd((first_num - second_num), second_num)
#         elif (first_num < second_num): 
#             return gcd(first_num, (second_num - first_num))
        

# def lcm(first_num, second_num):
#     multiply = first_num * second_num
#     result = multiply / gcd(first_num, second_num)
#     return int(result)

# first_num = int(input("Enter your first number: "))
# second_num = int(input("Enter your second number: "))

# print("LCM:", lcm(first_num, second_num))

# def combination(n, r):
#     if (n < r) :
#         return "ERROR!"

#     n_r = n-r

#     if (n != 0):
#         temp = n
#         while (temp != 1):
#             temp -= 1
#             n *= temp
#     else:
#         n = 1

#     if (r != 0):
#         temp = r
#         while (temp != 1):
#             temp -= 1
#             r *= temp
#     else: 
#         r = 1

#     if (n_r != 0):
#         temp = n_r
#         while (temp != 1):
#             temp -= 1
#             n_r *= temp
#     else:
#         n_r = 1

#     result = n / (n_r * r)

#     return (int(result))


# first_num = int(input("Enter your first number: "))
# second_num = int(input("Enter your second number: "))

# print("Combination result:", combination(first_num, second_num))

# import random

# def writeAction(typeOfOperation, digits):
#     if (typeOfOperation == '*'):
#         if (digits == 1):        
#             random_first = random.randint(0,9)
#             random_second = random.randint(0,9)
#         elif (digits == 2):
#             random_first = random.randint(10,99)
#             random_second = random.randint(10,99)
#         elif (digits == 3):
#             random_first = random.randint(100, 999)
#             random_second = random.randint(100, 999)
#         print(random_first, typeOfOperation, random_second, '= ?')
#     elif (typeOfOperation == '/'):
#         random_first = 0
#         if (digits == 1):
#             random_second = random.randint(0,9)
#             while (random_first == 0 or random_first % random_second != 0):
#                 random_first = random.randint(0,9)
#         elif (digits == 2):
#             random_second = random.randint(10,99)
#             while (random_first == 0 or random_first % random_second != 0):
#                 random_first = random.randint(10,99)
#         elif (digits == 3):
#             random_second = random.randint(100, 999)
#             while (random_first == 0 or random_first % random_second != 0):
#                 random_first = random.randint(100,999)
#         print(random_first, typeOfOperation, random_second, '= ?')

# # for multipication
# writeAction('*',2)

# # for division
# writeAction('/',3)


# array = []
# while True:
#     rand_num = random.randint(1, 5)
#     if len(array) == 50:
#         break
#     if array.count(rand_num) == 10:
#         continue
#     array.append(rand_num)

# count = 0
# print("\t Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# for row in range(1, 11):
#     print("Interval", str(row), end=":\t")
#     for col in range(1, 6):
#         print(array[count], end="\t")
#     count = count + 1
#     print("\n")

import random

schedule = []
def row_schedule(schedule):
    temp = []
    count = 0
    while (count != 5):
        rand_num = random.randint(1, 5)
        temp.append(rand_num)
        count += 1
    schedule.append(temp)

def col_schedule(schedule):
    count = 0
    while (count != 10):
        row_schedule(schedule)
        count += 1

def print_schedule(schedule):
    print("\t Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    for row in range(1, 11):
        print("Interval", str(row), end=":\t")
        for col in range(1, 6):
            print(schedule[row - 1][col - 1], end="\t")
        print("")

def swap_workers(schedule):
    input1, input2 = input("Please enter the code of two emoplyees: ").split()
    input1 = int(input1)
    input2 = int(input2)
    for row in range(1, 11):
        for col in range(0, 6):
            if (schedule[row-1][col-1] == input1):
                schedule[row-1][col-1] = input2
            elif (schedule[row-1][col-1] == input2):
                schedule[row-1][col-1] = input1
    print("Completed. . . ")
    print_schedule(schedule)

def print_weekly(schedule): 
    input_worker = int(input("Worker? "))
    for row in range(1, 11):
        for col in range(1, 6):
            if (schedule[row-1][col-1] == input_worker):
                print("Interval", str(row), ":\t", day_system(col))

def day_system(day):
    if (day == 1):
        return "Monday"
    elif (day == 2):
        return "Tuesday"
    elif (day == 3):
        return "Wednesday"
    elif (day == 4):
        return "Thursday"
    elif(day == 5):
        return "Friday"

def run_application(schedule):
    col_schedule(schedule)
    option_main = None
    while (option_main != '0'):
        print("____________MENU____________")
        print("0- Terminate Application")
        print("1- Print Weekly Schedule")
        print("2- Swap Two Workers")
        print("3- Worker Weekly Schedule")
        print("____________________________")
        option_main = input("Your choice: ")
        print("")
        if (option_main == '0'):
            return
        elif (option_main == '1'):
            print_schedule(schedule)
        elif (option_main == '2'):
            swap_workers(schedule)
        elif (option_main == '3'):
            print_weekly(schedule)
        print("")

run_application(schedule)

        
# test = {"test1": 120, "test2": 130}
# test_x = {"test1": 12, "test2": 10, "test3": 140}
# def test_func(test_x, test):
#     for key in test_x:
#         if (key not in test):
#             return 0
#     mod_lowest = None
#     for key in test_x: 
#         if (key in test):
#             temp = test[key] % test_x[key]
#             if (mod_lowest == None or temp < mod_lowest):
#                 mod_lowest = temp
#     return mod_lowest

# print(test_func(test, test_x))

# def score(dice):
#     temp_list = []
#     score_list = [1000, 200, 300, 400, 500, 600]
#     score_list_one = [100, 0, 0, 0, 50, 0]
#     for count in range(1, 7):
#         temp_list.append(dice.count(count))
        
#     temp_var = 0
#     count = 0
#     while (count != 6):
#         if (temp_list[count] >= 3):
#             temp_var += score_list[count]
#             temp_list[count] -= 3
#         temp_var += score_list_one[count] * temp_list[count]
#         count += 1
#     return temp_var

# print(score([1, 1, 1, 1, 4]))

# def first_non_repeating_letter(string):
#     #your code here
#     list_word = [i.lower() for i in string]
#     for i in range(len(list_word)):
#         if list_word.count(list_word[i]) == 1:
#             return string[i]
#     return ""

# print(first_non_repeating_letter("sTreSS"))