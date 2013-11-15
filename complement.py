def complement_nucleotide(nucleotide):
    if nucleotide == "A":
        return "T"
    elif nucleotide == "T":
        return "A"
    elif nucleotide == "C":
        return "G"
    elif nucleotide == "G":
        return "C"

def reverse_complement(genome):
    return ''.join([complement_nucleotide(nucleotide) for nucleotide in reversed(genome)])

genome = input()

print(reverse_complement(genome))
