def part1(input):
    total = 0
    if (len(input) == 0):
        return total
    
    for card in input:
        [ w, m ] = card.split(":")[1].split("|")
        w = w.split()
        m = m.split()
        c = [n for n in m if n in w]
        
        if len(c) == 0:
            continue
        
        total += pow(2, len(c) - 1)
        
    return total
    
def part2(input):
    total = 0
    
    if (len(input) == 0):
        return total
    
    multipliers = []
    
    for i in range(0, len(input)):
        multipliers.append(1)
    
    ci = 0
    
    for card in input:
        mult = multipliers[ci]
        total += multipliers[ci]
        
        [ w, m ] = card.split(":")[1].split("|")
        w = w.split()
        m = m.split()
        c = [n for n in m if n in w]
        
        cnt = len(c)
        if cnt > 0:
            for i in range(0, cnt):
                multipliers[ci + i + 1] = multipliers[ci + i + 1] + mult
        
        ci += 1
        
    return total