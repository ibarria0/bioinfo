import itertools

nucleotides = set("AGCT")

def distance(string,other_string):
    count = 0
    for i,chars in enumerate(zip(string,other_string)):
        if chars[0] != chars[1]:
            count+=1
    return count

def is_mismatch(string,other_string,d):
    return (distance(string,other_string) <= d)

def windows(genome,l):
    for i,v in enumerate(genome):
        if i + l <= len(genome):
            yield (i,genome[i:i+l])

def max_kmers(kmers):
    m = max(kmers.values())
    return {key for key in kmers.keys() if kmers[key] == m}

def find_kmers(genome,k):
    return {genome[idx:k+idx] for idx,char in enumerate(genome) if (len(genome) > idx+k)}

def possible_kmers(k):
    return itertools.product(nucleotides,repeat=k)

def possible_missmatches(kmer,d):
    nodes = set([kmer])
    for i in range(d):
        for node in list(nodes):
            nodes.update(expand(node))
    return nodes

def expand(kmer):
    nodes = set()
    for i,v in enumerate(kmer):
        t = list(kmer)
        other = nucleotides.difference(set(v))
        for char in other:
            t[i] = char
            nodes.add(''.join(t))
    return nodes



genome,k,d = input().split()
k = int(k)
d = int(d)

kmers = {''.join(kmer):0 for kmer in possible_kmers(k)}
for index,window in windows(genome,k):
    for kmer in possible_missmatches(window,d):
        kmers[kmer] = kmers[kmer] + 1
print(max_kmers(kmers))



