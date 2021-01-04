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