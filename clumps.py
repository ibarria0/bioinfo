def find_kmers(genome,k):
    return {genome[idx:k+idx] for idx,char in enumerate(genome) if (len(genome) > idx+k)}

def is_clump(genome,pattern,l,t):
    for idx,val in enumerate(genome):
        if genome[idx:idx+l].count(pattern) >= t:
            return True
    return False

def find_clumps(genome,kmers,l,t):
    clumps = []
    done = set()
    for idx,val in enumerate(genome):
        section = genome[idx:idx+l]
        for kmer in kmers:
            if kmer not in done:
                if section.count(kmer) >= t:
                    clumps.append(kmer)
                    done.add(kmer)
    return clumps

def find_kmer_clumps(genome,k,l,t):
    kmers = find_kmers(genome,k)
    return find_clumps(genome,kmers,l,t)
    

genome = input()
k,L,t = [int(i) for i in input().split()]
for kmer in find_kmer_clumps(genome,k,L,t):
    print(kmer,end=' ')


