import pandas as pd

# a = pd.Series([1, 45, 30, 21])
# print(a)


a = {
    "cgpa" : [1,2,3,4,5,6,7,8,9,0],
    "Resume_Score" : [5,6,7,8,9,0,1,2,3,4],
    "placed" : [8,9,5,6,0,7,2,1,3,5]
}

# Data Frame

df = pd.DataFrame(a)
# print(df)

# to export Data in dictionary as csv file
# df.to_csv("/home/theta/CODE/Learning/Python_Regex/data.csv")

# Import data from csv
# df = 

# How to check top 5 data in data frame
# print(df.head(4))

# To check last data

# Overall Info
# print(df.info)

# print(df. describe)

# top_left_corner_df = df.iloc[:4, :3]
# print(top_left_corner_df)

# df['Resume_Score'][2:4] = None
# df["placed"][6] = None
# print(df)

# to remove missinf/none values from data

# print(df.dropna())

# to arrange data
# arrange = df.sort_values(by = "Resume_Score")
# print(arrange)

# to change data type of a category
# df["cgpa"] = df["cgpa"].astype(float)
# print(df)

# to make a new column
# df["New cgpa"] = df["cgpa"].astype(int)
# print(df)

# df = df.drop(column = ["New cgpa"], axis = 1)
# print(df)

p = df.rename(columns = {"cgpa": "updated cgpa", "resume_score" : "semister_marks"})
print(p)

