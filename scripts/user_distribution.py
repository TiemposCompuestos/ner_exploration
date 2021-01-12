import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

texts = pd.read_csv(
    '../data/processed/command_line/unique_reviews.csv',
    names = ['text', 'business_id'],
    sep = '\t'
)

business_distribution = (
    texts
    .groupby('business_id')
    .size()
    .reset_index()
    .rename({0:'quant'}, axis = 1)
    .sort_values('quant', ascending = False)
    .reset_index(drop = True)
    .reset_index()
    .rename({'index': 'rank'}, axis = 1)
)
business_distribution['cumulative'] = business_distribution.quant.cumsum()

plt.figure(figsize = (10, 10))
sns.lineplot(x = 'rank', y = 'quant', data = business_distribution)
plt.title('Distribución de usuarios en escala lineal')
plt.savefig('../output/linear_dist.png')
plt.close()

plt.figure(figsize = (10, 10))
sns.lineplot(x = 'rank', y = 'cumulative', data = business_distribution)
sns.lineplot(x = 'rank', y = 'quant', data = business_distribution)
plt.gca().set(xscale = 'log', yscale = 'log')
plt.title('Distribución de usuarios en escala logarítmica')
plt.savefig('../output/log_dist.png')
plt.close()

most_coverage = business_distribution.loc[business_distribution.cumulative < len(texts) * .8]
most_coverage.to_csv('../data/processed/sample_to_tag/top_users.csv', index = False)