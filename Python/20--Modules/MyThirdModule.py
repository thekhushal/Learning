import MyFirstModule as mfm # we use as just because using whole title is just too long so insted we cut it small
# if we remove "as mfm" from import statement we'll have to use "MyFirstModule" (name of the module imported) in print lines or where ever it is used basically well have to replace "mfm" with "MyFirstModule"
#func = MyFirstModule.myFirstFunction()

print(mfm.myFirstFunction())
print("\n DONE \n")
print(mfm.mySecondFunction())