pattern = input()
genome = input()

indexes = [idx for idx,val in enumerate(genome) if genome[idx:len(pattern)+idx] == pattern]
for idx in indexes:
    print(idx,end=' ')
