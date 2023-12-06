import math

def canAdd(input, y, xl, xr):
    #print(f"CanAdd {input[y][xl:xr]}?: {y}, {xl}, {xr}")
    
    for x in range(xl, xr):
        if checkDigit(input, y, x):
            #print(f"{input[y][xl:xr]}: Is Good!")
            return True
        
    return False
    
def checkDigit(input, y, x):
    lineWidth = len(input[0]) - 1
    lineHeight = len(input) - 1
    
    #print(f"{lineWidth}, {lineHeight}, {y}, {x}, {input[y][x]}")
    
    # Check Top
    if (y > 0):
        # Check TL
        if (x > 0 and isValidChar(input[y - 1][x - 1])):
            return True
        
        # Check TM
        if (isValidChar(input[y - 1][x])):
            return True
        
        # Check TR
        if (x + 1 < lineWidth and isValidChar(input[y - 1][x + 1])):
            return True
    
    # Check ML
    if (x > 0 and isValidChar(input[y][x - 1])):
        return True
    
    # Check MR
    if (x + 1 < lineWidth and isValidChar(input[y][x + 1])):
        return True
    
    # Check Bottom
    if y < lineHeight:
        # Check BL
        if (x > 0 and isValidChar(input[y + 1][x - 1])):
            return True
        
        # Check BM
        if (isValidChar(input[y + 1][x])):
            return True
        
        # Check BR
        if (x + 1 < lineWidth and isValidChar(input[y + 1][x + 1])):
            return True

    return False
    
def isValidChar(char):
    #if (not char.isdigit() and char != '.' and ord(char) != 10):
    #    print (f"{char} {ord(char)} is the one I've been looking for!")
    # print (f"Checking char: {char}")
    return not char.isdigit() and char != '.' and ord(char) != 10

def part1(input):
    total = 0
    y = 0
    
    lineWidth = len(input[0]) - 1
    
    for line in input:
        xl = 0
        xr = 0
        inNum = False
        
        if (line[xl].isdigit()):
            inNum = True
            
        while (xr < lineWidth):
            xr += 1
            
            if (xr >= lineWidth):
                break
             
            # print(f"{y}, {xl}-{xr}: {inNum} {line[xl:xr]} ")
            
            if (line[xr].isdigit()):
                if not inNum:
                    inNum = True
                    xl = xr
                
                continue
            else: 
                if inNum:
                    curNum = line[xl:xr]
                    
                    if canAdd(input, y, xl, xr):
                        # print(f"{total} + {curNum} = {total + int(curNum)}")
                        total += int(curNum)
                        
                    inNum = False
                xl = xr

        if inNum:
            curNum = line[xl:xr]
            if canAdd(input, y, xl, xr):
                # print(f"{total} + {curNum}")
                total += int(curNum)
            
        y += 1
    
    return total
    
def part2(input):
    total = 0
    
    if (len(input) == 0):
        return total
    
    # Loop through each line
    # Loop through each character
    # if character is not asterisk, continue
    # else 
    #   get seven characters above 
    #   extract numbers from string
    #       loop through characters
    #       if not inNum and char.isDigit, isNum = true
    #       if inNum and char.IsDigit, continue loop
    #       if inNum and not char.isDigit(), push number onto list, inNum = false
    #   get seven characters below and extract numbers
    #   Check ML
    #       if edge or not isDigit, bounce out
    #       if isDigit and numberCount >= 2, bounce out
    #       if isDigit, scan left until edge or not isDigit, then push onto list 
    #   Check MR and scan right
    # Check Number List
    # if not numberList.count == 2
    #   continue character search
    # else
    #   total += numberList[0] * numberList[1]
    h = len(input)
    w = len(input[0])
    
    for y in range(0, h - 1):
        line = input[y]
        
        for x in range(0, w - 1):
            c = line[x]
            
            if not c == '*':
                continue
            
            numberList = []
            numberList += checkTBStrs(input, x, y, h, w, 1)
            numberList += checkTBStrs(input, x, y, h, w, 0)
            
            if (len(numberList) > 2):
                continue
            
            # Check ML
            if x > 0 and line[x - 1].isdigit():
                xl = max(x - 3, 0)
                numberList.append(int(line[xl:x].split('.')[-1]))

            # Check MR
            if x < w and line[x + 1].isdigit():
                xr = max(x + 4, w)
                numberList.append(int(line[(x + 1):xr].split('.')[0]))
                
            if (len(numberList) != 2):
                 continue
             
            # print (f"({y}, {x}):", numberList)
             
            total += numberList[0] * numberList[1]
            
    return total

def checkTBStrs(input, x, y, h, w, top = 0):
    x1 = max(x - 3, 0)
    x2 = min(x + 4, w)
    
    if top == 1:
        y = y - 1 if y > 0 else y
    else:
        y = y + 1 if y < h else y
        
    str = input[y][x1:x2]
    
    i1 = 0
    inNum = False
    numberList = []
    strlen = len(str)
    
    for i2 in range(0, strlen):
        if (str[i2].isdigit()):
            if not inNum:
                inNum = True
                i1 = i2
        elif inNum:
            if (i2 in [3,4,5] or i1 in [3,4,5]):
                numberList.append(int(str[i1:i2]))
            inNum = False
        
        if i2 >= 4 and not inNum:
            break
            
    if inNum and i1 in [3,4,5]:
        numberList.append(int(str[i1:strlen]))
    
    return numberList