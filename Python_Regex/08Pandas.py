import pandas as pd

# a = pd.Series([1, 45, 30, 21])
# print(a)


# Data Frame


a = {
    "cgpa" : [1,2,3,4,5,6,7,8,9,0],
    "Resume_Score" : [5,6,7,8,9,0,1,2,3,4],
    "placed" : [8,9,5,6,0,7,2,1,3,5]
}

df = pd.DataFrame(a)
print(df)