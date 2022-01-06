import pandas as pd

#converting the units - for dwarf
df = pd.read_csv("dwarf_stars.csv")
df = df.dropna()
df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)
df.to_csv("Final_data/unit_converted_stars.csv")