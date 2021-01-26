import pandas as pd

dataset = pd.read_csv('All-seasons.csv/data.csv')
characters = ['Stan','Kyle','Cartman']
dataset = dataset[dataset['Character'].isin(characters)]["Line"]

dataset.to_csv('clean.csv', index=False)

