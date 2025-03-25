# Accept the marks scored and tell student's grade
# 	>= 75 Distiction
# 	< 75 and >= 60 First divison
# 	< 60 and >= 48 Second division
# 	< 48 and >= 36 Third division
# 	< 36 Fail

M = int(input("Enter your Marks : "))

if M >= 75 : # We can add "100 >" before M that'll make it more pratical but as per given instructions code is sufficient
    print("Distiction")
elif M >= 60 :
    print("First Division")
elif M >= 48 :
    print("Second Division")
elif M >= 36 :
    print("Third Division")
else : # over her with elif we can make it b\w 0 to 36 but again as per given instruction code is complete
    print("Fail")