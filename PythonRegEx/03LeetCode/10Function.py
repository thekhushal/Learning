# Function

# no of arguments must be same as the number of parameters of function

# Positional Argument


# Keywoard Argument


# Default Argument
# Over here we set the default value of parameters, so that if any argument for the parameter isnt passe the code must not fail


# Variable length argument
# Eg:
def func(*x): #x is tupple type
    print("Details are: ", x, type(x))

func(12, 34 , 56 , 78, 90)

# Keywoard Variable length argument
def func(**x): # x is dictioanry type
    print("Details are: ", x, type(x))

func(age = 45, id = 199, name = "xyz")


