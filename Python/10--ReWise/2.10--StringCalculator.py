sense = input()

x = 0 
count = 0
while x < len(sense) :

    if sense[x].isalpha() :
        count += 1
    x += 1
print(count)

