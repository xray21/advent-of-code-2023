def part1(input):
    total = 0 
    
    rl = 12
    gl = 13
    bl = 14
    
    for line in input:
        gameParts = line.split(':')
        id = gameParts[0].split()[1] # Format is "Game {num}"
        canAdd = True
        
        sets = gameParts[1].split(';')
        
        for set in sets:
            marbleGroups = set.split(',')
            
            for marbleGroup in marbleGroups:
                count, color = marbleGroup.split() # Format is {count} {color}. For example, 3 Blue
                
                l = -1
                
                match color:
                    case "red": l = rl
                    case "blue": l = bl
                    case "green": l = gl
                    case default:
                        l = -1
                        
                if (int(count) > l):
                    canAdd = False
                    break
                
            if not canAdd:
                break
                  
        if canAdd:
            total += int(id)
                
    return total
    
def part2(input):
    total = 0
    
    for line in input:
        rm = 1
        bm = 1
        gm = 1
        
        gameParts = line.split(':')
        sets = gameParts[1].split(';')
        
        for set in sets:
            marbleGroups = set.split(',')
            
            for marbleGroup in marbleGroups:
                n, color = marbleGroup.split() # Format is {count} {color}. For example, 3 Blue
                num = int(n)
                
                match color:
                    case "red":
                        if num > rm:
                            rm = num  
                    case "blue":
                        if num > bm:
                            bm = num  
                    case "green": 
                        if num > gm:
                            gm = num  

        # print(f"{gameParts[0]}: {rm} {bm} {gm}")

        total += (rm * bm * gm)
                
    return total