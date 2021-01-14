import re

import spacy
import pandas as pd


SPACY_MODEL = spacy.load('en_core_web_sm')


def tagged_to_bilou(tagged_text):
    bilou = {
        'text': [],
        'token': [],
        'tag': []
    }
    for item in enumerate(tagged_text):
        index, text = item
        tag_heads = text.split('<')
        for head in tag_heads:
            pairs = extract_tags_from_tag_head(head)
            if pairs:
                for pair in pairs:
                    tag, token = pair
                    bilou['text'].append(f'text{index}')
                    bilou['token'].append(token)
                    bilou['tag'].append(tag)
    return bilou

def extract_tags_from_tag_head(tag_head):
    if len(tag_head) == 0:
        pass
    else:
        content = tag_head.split('>')
        if len(content) == 1:
            head, tokens = ('/', content[0])
        else:
            head, tokens = content
        tokenized = SPACY_MODEL(re.sub(' +', ' ', tokens.strip()))
        if head[0] == '/':
            return [('O', token.text) for token in tokenized]
        elif len(tokenized) == 1:
            return [(f'U-{head}', token.text) for token in tokenized]
        else:
            inside = [(f'I-{head}', token.text) for token in tokenized[1:-1]]
            beggining = [(f'B-{head}', tokenized[0].text)]
            last = [(f'L-{head}', tokenized[-1].text)]
            return beggining + inside + last

def bilou_to_flair(bilou_dict):
    bilou_frame = pd.DataFrame(bilou_dict)
    values = []
    for source in bilou_frame['text'].unique():
        text = bilou_frame.loc[bilou_frame.text == source][['token', 'tag']].values
        for row in text:
            token, tag = row
            newtag = tag.replace('L-', 'E-').replace('U-', 'S-')
            values.append(' '.join([token, newtag]))
        values.append('')
    return '\n'.join(values[:-1])

def bilou_to_crfsuite(bilou_dict):
    bilou_frame = pd.DataFrame(bilou_dict)
    values = []
    for source in bilou_frame['text'].unique():
        values.append([(token, tag) for token, tag in bilou_frame.loc[bilou_frame.text == source][['token', 'tag']].values])
    return values
