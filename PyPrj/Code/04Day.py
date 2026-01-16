# B) Repeat the following queries using python (i.e., by reading data from animal.txt, without using a database or SQL language). The idea is to replicate what a database does when the query executes.


# 1. Find the animal names and categories for animals related to a bear

with open('/home/theta/CODE/Learning/PyPrj/TXT/04animal.txt', 'r') as f:
    data = [lines.strip().split(',') for lines in f]

print(*(i for i in data), sep="\n")

# for i in data:
    # if 'bear' in i[1]:
    #     print(i[1], i[2])
    
        
# 2. Find the names of the animals that are not related to the tiger and are common

with open("/home/theta/CODE/Learning/PyPrj/TXT/04animal.txt", 'r') as f:
    for line in f:
        i = line.strip().split(',')
        if 'tiger' not in i[1] and i[2] == 'common':
            print(i[1])

