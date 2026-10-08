import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv('../data/patients.csv')
df.columns = df.columns.str.strip()
df.head()

df.describe()
df['Sex'].value_counts()
df['Diagnosis'].value_counts()

plt.plot(df['Age'], df['Cholesterol'], marker = "o")
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.title('Age vs Cholesterol')
plt.show()