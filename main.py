import sys
import os
from day1 import day1

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


def main():
    runtests = True
    
    day = input("Enter Day #: ")
    data = getData(day)
    
    td1 = getTestData(day, 1)
    td2 = getTestData(day, 2)
    
    match day:
        case "1":
            print ("Part 1")
            print(f"Test: {day1.part1(td1)}")
            print(f"Answer: {day1.part1(data)}")
            
            print ("\nPart 2")
            print(f"Test: {day1.part2(td2)}")
            print(f"Answer: {day1.part2(data)}")

        case 2:
            print("Day 2")
        case default:
            print("Ya dun goof'd")
    
main()