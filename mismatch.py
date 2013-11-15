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
    
pattern = input()
genome = input()
d = int(input())

print(pattern,d)
for index in [idx for idx,window in windows(genome,len(pattern)) if is_mismatch(window,pattern,d)]:
    print(index, end=' ')
print('')
