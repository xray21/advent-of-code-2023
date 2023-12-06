import os
from day1 import day1
from day2 import day2
from day3 import day3
from day4 import day4

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def getPath(filename):
    return os.path.join(__location__, filename)

def getInput(day, filename):
    f = open(getPath(f"day{day}\{filename}"), "r")
    return f.readlines()

def getData(day):
    return getInput(day, "input.txt")

def getTestData(day, num):
    return getInput(day, f"testInput{num}.txt")

def getDay():
    return int(input("Enter Day #: "))

def main():
    dm = None
    
    day = getDay()
    while (type(day) == int):
        match day:
            case 1:  dm = day1
            case 2:  dm = day2
            case 3:  dm = day3
            case 4:  dm = day4
            case 5:  dm = None
            case 6:  dm = None
            case 7:  dm = None
            case 8:  dm = None
            case 9:  dm = None
            case 10: dm = None
            case 11: dm = None
            case 12: dm = None
            case 13: dm = None
            case 14: dm = None
            case 15: dm = None
            case 16: dm = None
            case 17: dm = None
            case 18: dm = None
            case 19: dm = None
            case 20: dm = None
            case 21: dm = None
            case 22: dm = None
            case 23: dm = None
            case 24: dm = None
            case 25: dm = None
            case default: break
                
        if (dm != None):
            print(f"\nDay {day}")
            print("-----------------------------------\n")
            
            data = getData(day)
            td1 = getTestData(day, 1)
            td2 = getTestData(day, 2)    
                
            print("Part 1")
            print(f"Test: {dm.part1(td1)}")
            print(f"Answer: {dm.part1(data)}")
            print()
            print("Part 2")
            print(f"Test: {dm.part2(td2)}")
            print(f"Answer: {dm.part2(data)}")

        print()
        day = getDay()
    
main()