import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder

# Let's assume df is already defined
# If it's not, create a sample df for testing
# df = pd.read_csv('your_data.csv')

# Handle missing values if any (example: for 'fever')
si = SimpleImputer()
df['fever'] = si.fit_transform(df[['fever']])

# ================= Label Encoding =================
df_label = df.copy()

lb = LabelEncoder()
df_label['gender'] = lb.fit_transform(df_label['gender'])
df_label['cough'] = lb.fit_transform(df_label['cough'])  # You had 'city' by mistake

print("Label Encoded:")
print(df_label.head(2))

# =============== Ordinal Encoding =================
df_ordinal = df.copy()
df_ordinal = df_ordinal.drop(columns=['age', 'fever', 'city'])  # Drop numerical/irrelevant cols

# Check values before defining categories
# print(df_ordinal['gender'].unique()) 
# print(df_ordinal['cough'].unique()) 
# print(df_ordinal['has_covid'].unique()) 

oe = OrdinalEncoder(categories=[['Male', 'Female'],
                                ['Mild', 'Strong'],
                                ['Yes', 'No']])

df_oe = oe.fit_transform(df_ordinal)

df_new = pd.DataFrame(df_oe, columns=df_ordinal.columns)
print("Ordinal Encoded:")
print(df_new.head(2))

# =============== OneHot Encoding ==================
df_one = df.copy()

oe = OneHotEncoder(drop='first', sparse_output=False)  # 'sparse_output' for sklearn >=1.2
oe_arr = oe.fit_transform(df_one[['gender', 'cough', 'city', 'has_covid']])

# Convert to DataFrame
oe_df = pd.DataFrame(oe_arr, columns=oe.get_feature_names_out(['gender', 'cough', 'city', 'has_covid']))

# Concatenate with the rest of the dataframe
df_one_final = pd.concat([df_one.drop(columns=['gender', 'cough', 'city', 'has_covid']), oe_df], axis=1)

print("OneHot Encoded:")
print(df_one_final.head(2))

# =============== get_dummies =====================
df_get = df.copy()
df_get = pd.get_dummies(df_get, columns=['gender', 'cough', 'city', 'has_covid'], drop_first=True)

# Optional: Convert bool to int
df_get = df_get.astype(int)

print("get_dummies Encoded:")
print(df_get.head(2))
