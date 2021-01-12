import pandas as pd

rnd_state = 1

texts = pd.read_csv('../data/processed/command_line/unique_reviews.csv', names=['text', 'business_id'], sep = '\t')
top_businesses = pd.read_csv('../data/processed/sample_to_tag/top_users.csv')

top_business_reviews_sample = (
    texts.loc[texts.business_id.isin(top_businesses.business_id.unique())][['business_id', 'text']]
    .groupby('business_id')
    .sample(1, random_state = rnd_state)
)

rest_business_reviews_sample = (
    texts.loc[~texts.business_id.isin(top_businesses.business_id.unique())][['business_id', 'text']]
    .sample(10000 - len(top_business_reviews_sample), random_state = rnd_state)
)

top_business_reviews_sample.to_csv('../data/processed/sample_to_tag/top_sample.csv', index = False)
rest_business_reviews_sample.to_csv('../data/processed/sample_to_tag/rest_sample.csv', index = False)