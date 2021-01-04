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
        print("\n")


col_schedule(schedule)
print_schedule(schedule)