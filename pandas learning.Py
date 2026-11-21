import pandas as pd

data = {'EMP_ID':[101,102,103,104,105],
    "EMP_name": ["Asha", "Ben", "Chen",'Shalu','Anu'],
    "EMP_age": [25, 30, 22,26,35],
    'EMP_dept':['hr','it','sales','manager','analyst'],
    'EMP_salary':[25000,10000,30000,40000,60000]
}

df = pd.DataFrame(data)
print(df)
df.to_csv('shalu.csv', index=False)
print ('DataFrame is written to csv file successfully.')


df =pd.read_csv("C:\python learning\coffee_sales.csv")
print(df)
print(df.head(5))
print(df.tail(5))
print(df.shape)
df =pd.read_csv("c:\python learning\shalu.csv")
print(df)
print(df.info(4))
print(df["EMP_name"])
print(df[['EMP_salary',"EMP_name"]])
print(df[df['EMP_salary'] > 20000])
print(df.loc[0])


