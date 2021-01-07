import pandas as pd
data = pd.read_csv('C:/users/richard/downloads/interactions.csv', low_memory=False)
df1 = data[data['sourceTaxonPathNames'].str.contains("Virus", na=False)]
print(df1)

pd.DataFrame.to_csv(df1, 'C:/users/richard/desktop/smallInteractions.csv')