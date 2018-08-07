import pandas
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')


# Load stage data from csv file
stages = pandas.read_csv('stages.csv', index_col=0)
stages.sort_values(by='Launch Vehicle', inplace=True)
stages.sort_values(by='Fuel', inplace=True)

# Compute the inert mass fractions.
stages['Gross mass'] = stages['Propellant mass'] + stages['Inert mass']
stages['Gross mass [Mg]'] = stages['Gross mass'] / 1000
stages['Inert mass fraction'] = stages['Inert mass'] / stages['Gross mass']

# Split into first stages / boosters vs. upper stages
boost_stages = stages.loc[stages['Stage Number'] <= 1]
upper_stages = stages.loc[stages['Stage Number'] > 1]

# Exclude  booster stages that cannot liftoff under own thrust w/o strap-ons.
boost_stages = boost_stages.loc[boost_stages['Liftoff under own thrust']]

fuel_order = ['H2', 'kero']
matl_order = ['steel', 'aluminum', 'composite']


plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.title('Upper stages')
sns.scatterplot(data=upper_stages, x='Year of first flight', y='Inert mass fraction',
                hue='Fuel', style='Fuel',
                hue_order=fuel_order)
plt.ylim([0, plt.ylim()[1]])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.subplot(2, 1, 2)
plt.title('Boosters')
sns.scatterplot(data=boost_stages, x='Year of first flight', y='Inert mass fraction',
                hue='Fuel', style='Fuel',
                hue_order=fuel_order)
plt.ylim([0, plt.ylim()[1]])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.title('Upper stages')
sns.scatterplot(data=upper_stages, x='Gross mass [Mg]', y='Inert mass fraction',
                hue='Fuel', style='Fuel',
                hue_order=fuel_order)
plt.xlim([0, plt.xlim()[1]])
plt.ylim([0, plt.ylim()[1]])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.subplot(2, 1, 2)
plt.title('Boosters')
sns.scatterplot(data=boost_stages, x='Gross mass [Mg]', y='Inert mass fraction',
                hue='Fuel', style='Fuel',
                hue_order=fuel_order)
plt.xlim([0, plt.xlim()[1]])
plt.ylim([0, plt.ylim()[1]])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()


plt.figure(figsize=(8, 4))
ax1 = plt.subplot(2, 1, 1)
sns.stripplot(data=upper_stages, x='Inert mass fraction', y='Fuel', hue='Common bulkhead',
              jitter=False, dodge=True, order=fuel_order, palette=sns.color_palette(['C2', 'C3']))
plt.title('Inert mass fraction of Upper Stages')
plt.xlim([0, plt.xlim()[1]])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.subplot(2, 1, 2, sharex=ax1)
sns.stripplot(data=boost_stages, x='Inert mass fraction', y='Fuel', hue='Common bulkhead',
              jitter=False, dodge=True, order=fuel_order, palette=sns.color_palette(['C2', 'C3']))
plt.title('Inert mass fraction of Booster Stages')
plt.xlim([0, plt.xlim()[1]])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()

plt.figure(figsize=(8, 4))
ax1 = plt.subplot(2, 1, 1)
sns.stripplot(data=upper_stages, x='Inert mass fraction', y='Fuel', hue='Tank material',
              jitter=False, dodge=True, order=fuel_order, hue_order=matl_order,
              palette=sns.color_palette(['C6', 'C7', 'C8']))
plt.title('Inert mass fraction of Upper Stages')
plt.xlim([0, plt.xlim()[1]])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.subplot(2, 1, 2, sharex=ax1)
sns.stripplot(data=boost_stages, x='Inert mass fraction', y='Fuel', hue='Tank material',
              jitter=False, dodge=True, order=fuel_order, hue_order=matl_order,
              palette=sns.color_palette(['C6', 'C7', 'C8']))
plt.title('Inert mass fraction of Booster Stages')
plt.xlim([0, plt.xlim()[1]])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()

plt.show()
