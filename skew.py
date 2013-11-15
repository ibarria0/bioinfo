def gc_skew(substring):
    if len(substring) == 0:
        return 0
    else:
        g,c = count_gc(substring)
        return (g-c)

def count_gc(substring):
    return (substring.count("G"),substring.count("C"))

def genome_skew(genome):
    return [gc_skew(genome[:i]) for i in range(len(genome) + 1)]

def find_min_skews(genome):
    skew = genome_skew(genome)
    min_skew = min(skew)
    return [i for i,v in enumerate(skew) if v == min_skew]
        


genome = input()
print(find_min_skews(genome))
