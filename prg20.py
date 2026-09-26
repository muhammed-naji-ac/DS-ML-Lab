import pandas as pd

details={
    'Name':['a','b','c','d','e'],
    'Occupation':['A1','A1','A1','B1','B1'],
    'salary':[20,30,40,27,23]
}
df=pd.DataFrame(details)
print(df)
occ_average_age=df.groupby('Occupation')['salary'].mean()
print("Averasge salary")
print(occ_average_age)