import pandas as pd

data = pd.read_csv (r'/Users/obult/hackathon/survey.csv')
pasiv = ['ConvertedSalary', 'Country', 'YearsCoding']
ethic = ['EthicsChoice', 'EthicsReport', 'EthicsResponsible']

n = 2

df = pd.DataFrame(data, columns= ['ConvertedSalary', ethic[n], pasiv[1], pasiv[2], 'Gender'])

df = df.dropna(axis=0,how='any',thresh=None,subset=None,inplace=False)
df = df[df.ConvertedSalary != 0.0]
df = df[df.Country == 'United States']
df = df[df.YearsCoding == '9-11 years']

df['Gender'] = df['Gender'].str[:1]

pt = df.groupby([pasiv[1],pasiv[2], ethic[n], 'Gender']).mean()
print(pt)