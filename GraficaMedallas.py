import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('athlete_events.csv')

MedalsPerCountry = df.groupby(['NOC'], as_index=False).Medal.count().sort_values(by='Medal',ascending=False).head(10)

MedalsPerCountry.set_index('NOC', inplace=True)
MedalsPerCountry["Medal"].plot(kind='bar')
plt.show()