import re

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

def reduce_kmers(kmers,d):
    reduced = {kmer:[] for kmer in kmers}
    for kmer in kmers:
        for other_kmer in kmers:
            if is_mismatch(kmer,other_kmer,d) and kmer != other_kmer:
                reduced[kmer].append(other_kmer)
    return reduced



#genome,k,d = input().split()
#k = int(k)
#d = int(d)

kmers = find_kmers('ACGTTGCATGTCGCATGATGCATGAGAGCT',4)
reduced = reduce_kmers(kmers,1)
print(kmers)
print(reduced)
print(max_kmers(reduced))


