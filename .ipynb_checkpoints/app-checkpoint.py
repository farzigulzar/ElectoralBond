import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sns
import panel as pn

pn.extension('ipywidgets')

filepath = 'Cleaned_merged_data\electoral.csv'
df = pd.read_csv(filepath)


denom_ = df[['Name of the Political Party', 'Denominations']].groupby('Name of the Political Party').sum().sort_values(by='Denominations',ascending=False)
denom_['Percentage'] = (100*denom_['Denominations']/denom_['Denominations'].sum())
# denom_

# plot
fig, ax =plt.subplots()
ax.pie(denom_['Denominations'], labels= denom_.index, autopct='%1.2f%%')
ax.legend(loc='upper left',bbox_to_anchor=(2.1, 1))
plt.show() 
# top line


# df[(df['Name of the Purchaser'].isnull())][['Name of the Political Party','Denominations']].groupby('Name of the Political Party').sum().sort_values(by='Denominations', ascending=False)
nan_ = df[(df['Name of the Purchaser'].isnull())]
t_ = nan_[['Name of the Political Party', 'Denominations']].groupby('Name of the Political Party').sum().sort_values(by='Denominations', ascending=False).rename(columns={'Denominations':'Not accounted'})
t_['Total Denominations'] = denom_['Denominations']
t_['Not accounted denom of total denominations']=100*t_['Not accounted']/t_['Total Denominations']
nan_=nan_.sort_values(by ='Date of Encashment')

fig,ax=plt.subplots()
ax.pie(t_['Not accounted'], labels = t_.index, autopct='%1.2f%%')
plt.show()

party = 'BHARATIYA JANATA PARTY'

sns.set_theme(style='ticks')
f, ax= plt.subplots()
sns.despine(f)

sns.histplot(
    nan_[['Date of Encashment', 'Name of the Political Party', 'Denominations']].sort_values(by=['Date of Encashment', 'Denominations'], ascending=[True, False]),
    x='Date of Encashment',
    hue='Name of the Political Party',
    multiple='stack',
    edgecolor=".3",
    linewidth=.5
)

sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
plt.xticks(rotation='vertical')
plt.show()


