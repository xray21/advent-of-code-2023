import re

def part1(input):
    total = 0
    
    for line in input:
        nl = re.sub("\D", "", line)
        num = nl[0] + "" + nl[len(nl) - 1]
        total += int(num)
        
    return total
    
def part2(input):
    total = 0
    
    numstrs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for line in input:
        # Get Left
        left = 0
        l = 0
        r = 0
        
        #print(line)
        while(left == 0):
            if (line[r].isdigit()):
                left = int(line[r])
            else:
                curstr = line[l:r + 1]
                
                for i in range(1, len(numstrs)):
                    if (numstrs[i] in curstr):
                        left = i
            
            r += 1
            if (r - l > 5):
                l += 1
        
        # Get Right
        right = 0
        l = len(line) - 1
        r = l
        
        while(right == 0):
            if (line[l].isdigit()):
                right = int(line[l])
            else:
                curstr = line[l:r]
                
                for i in range(1, len(numstrs)):
                    if (numstrs[i] in curstr):
                        right = i
            
            l -= 1
            if (r - l > 5):
                r -= 1
                
        num = str(left) + "" + str(right)
        total += int(num)

    return total