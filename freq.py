import re

def count_kmers(genome,k):
    kmers = {genome[idx:k+idx] for idx,char in enumerate(genome) if (len(genome) > idx+k)}
    return { kmer:len(re.findall(r'(?=(%s))' % kmer,genome)) for kmer in kmers }

def max_kmers(genome,k):
    kmers = count_kmers(genome,k)
    m = max(kmers.values())
    return {key for key in kmers.keys() if kmers[key] == m}

    
    

genome = str(input())
k = int(input())

for kmer in max_kmers(genome,k):
    print(kmer,end=' ')
