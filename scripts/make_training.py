import pandas as pd

import format_tagged_sentences as fts

tagged = pd.read_csv('../data/tagged/some_tagged.csv', sep = ',').fillna(0)
filtered = tagged.loc[tagged.restaurant == "1"]
shuffled = filtered.sample(len(filtered), random_state = 1)

train_percentage = .8
train_index = int(train_percentage * len(shuffled))
eval_index = train_index + int(((1 - train_percentage) / 2) * len(shuffled))

train_flair_set = shuffled[:train_index][['text']]
eval_flair_set = shuffled[train_index:eval_index][['text']]
train_crf_set = shuffled[:eval_index][['text']]
test_set = shuffled[eval_index:][['text']]

train_crf_set.to_csv('../data/processed/NER/crf/training_set.csv', header = None, index = None)
test_set.to_csv('../data/processed/NER/crf/test_set.csv', header = None, index = None)

name_file_pairs = [('train_set', train_flair_set), ('test_set', test_set), ('eval_set', eval_flair_set)]
for name, content in name_file_pairs:
    with open(f'../data/processed/NER/flair/{name}', 'w+') as file:
        file.writelines(
            fts.bilou_to_flair(fts.tagged_to_bilou(content.text.to_list()))
        )

full_texts = pd.read_csv('../data/processed/command_line/unique_reviews.csv', names=['text', 'business_id'], sep = '\t')
embeddings_texts = full_texts.loc[full_texts.business_id.isin(filtered.business_id.unique())]
shuffled_embeddings = embeddings_texts.sample(len(embeddings_texts), random_state = 1)[['text']]

train_test_split_index = int(.9 * len(shuffled_embeddings))
train_embeddings = shuffled_embeddings[:train_test_split_index]
test_embeddings = shuffled_embeddings[train_test_split_index:]
train_embeddings.to_csv('../data/processed/embeddings/flair/corpus/train/train_split_1', index = False, header = None)
test_embeddings.to_csv('../data/processed/embeddings/flair/corpus/test.txt', index = False, header = False)