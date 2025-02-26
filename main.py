#################
#### IMPORTS ####
#################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

###################
#### DATA LOAC ####
###################

df = pd.read_csv('crime_data.csv')

###############
#### INFO  ####
###############

print(df.info())

#############################
#### MISSING VALUE CHECK ####
#############################

print("\nMissing values in each column:")
print(df.isnull().sum())

##############################
#### TOTAL CRIMES BY YEAR ####
##############################

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='Total Crimes', hue='City', marker='o')
plt.title('Total Crimes by Year')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45)
plt.legend(title='City')
plt.grid()
plt.tight_layout()
plt.savefig('total_crimes_by_year.png', dpi=300)
plt.close()

#################################
#### MOST COMMON CRIME TYPES ####
#################################

most_common_crime = df.groupby('Crime Type')['Total Crimes'].sum().reset_index()
most_common_crime = most_common_crime.sort_values(by='Total Crimes', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=most_common_crime, x='Total Crimes', y='Crime Type', palette='viridis', hue='Crime Type', legend=False)
plt.title('Most Common Crime Types')
plt.xlabel('Total Crimes')
plt.ylabel('Crime Type')
plt.tight_layout()
plt.savefig('most_common_crime_types.png', dpi=300)
plt.close()

#####################################
#### CRIME SOLVED VS TOTAL CRIME ####
#####################################

plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Total Crimes', y='Crimes Solved', hue='City', alpha=0.7)
plt.title('Crimes Solved vs Total Crimes')
plt.xlabel('Total Crimes')
plt.ylabel('Crimes Solved')
plt.grid()
plt.tight_layout()
plt.savefig('crimes_solved_vs_total.png', dpi=300)
plt.close()