# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

# Task
# Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

# The left side letters and their power:

#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:

#  m - 4
#  q - 3
#  d - 2
#  z - 1
# The other letters don't have power and are only victims. Sum up each side's letters' power values to determine which side wins.

# Example
# alphabetWar("z");        //=> Right side wins!
# alphabetWar("zdqmwpbs"); //=> Let's fight again!
# alphabetWar("zzzzs");    //=> Right side wins!
# alphabetWar("wwwwwwz");  //=> Left side wins!


fight = input("Let the fight began: ")

left = {
    'r' : 4,
    'a' : 3,
    'h' : 2,
    'u' : 1
}

right = {
    'm' : 4,
    'o' : 3,
    'd' : 2,
    'i' : 1
}

lw = 0
rw = 0

for x in range(len(fight)):
    if fight[x] in left:
        lw += left[fight[x]]
    elif fight[x] in right:
        rw += right[fight[x]]
    
if lw > rw:
    print("Left Wins")
elif rw > lw:
    print("Abki baar Modi sarkar")
else:
    print("TRY AGAIN")


# if 'z' in left:
#     print(left['r'])