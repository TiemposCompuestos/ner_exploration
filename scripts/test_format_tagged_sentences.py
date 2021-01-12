import pytest

import format_tagged_sentences as fts

@pytest.fixture
def example_review():
    return ["<restaurant>Dukem</restaurant> is a staple in my rotation of favorite restaurants to eat at within the GTA.  I was skeptical at first of what Ethiopian cuisine was like but after my first visit to <restaurant>Dukem</restaurant> I was hooked.  My regular order is <dish>Awaze Tibs</dish> with the <dish>Vegetable Combo Platter</dish> along with a <dish>mango juice</dish>.  The service is excellent and the owner really knows how to make you feel welcome in his establishment.  I suggest trying Ethiopian at least once to all of my friends and family, but it has to be at <restaurant>Dukem</restaurant>!"]

@pytest.fixture
def example_tagged_texts():
    return {
        'text': ['text0'] * 17 + ['text1'] * 17,
        'token': [
            'My', 'regular', 'order', 'is', 'Awaze', 'Tibs', 'with', 'the', 'Vegetable', 'Combo', 'Platter', 'along', 'with', 'a', 'mango', 'juice', '.'
        ] + [
            'Dukem', 'is', 'a', 'staple', 'in', 'my', 'rotation', 'of', 'favorite', 'restaurants', 'to', 'eat', 'at', 'within', 'the', 'GTA', '.'
        ],
        'tag': [
            'O', 'O', 'O', 'O', 'B-dish', 'L-dish', 'O', 'O', 'B-dish', 'I-dish', 'L-dish', 'O', 'O', 'O', 'B-dish', 'L-dish', 'O'
        ] + [
            'U-restaurant', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'
        ]
    }


def test_tagged_to_bilou(example_review):
    output = fts.tagged_to_bilou(example_review)
    expected = {
        'text': ['text0'] * 98,
        'token': [
            'Dukem', 'is', 'a', 'staple', 'in', 'my', 'rotation', 'of', 'favorite', 'restaurants', 'to', 'eat', 'at', 'within', 'the', 'GTA', '.'
        ] + [
            'I', 'was', 'skeptical', 'at', 'first', 'of', 'what', 'Ethiopian', 'cuisine', 'was', 'like', 'but', 'after', 'my', 'first', 'visit', 'to', 'Dukem', 'I', 'was', 'hooked', '.'
        ] + [
            'My', 'regular', 'order', 'is', 'Awaze', 'Tibs', 'with', 'the', 'Vegetable', 'Combo', 'Platter', 'along', 'with', 'a', 'mango', 'juice', '.'
        ] + [
            'The', 'service', 'is', 'excellent', 'and', 'the', 'owner', 'really', 'knows', 'how', 'to', 'make', 'you', 'feel', 'welcome', 'in', 'his', 'establishment', '.'
        ] + [
            'I', 'suggest', 'trying', 'Ethiopian', 'at', 'least', 'once', 'to', 'all', 'of', 'my', 'friends', 'and', 'family', ',', 'but', 'it', 'has', 'to', 'be', 'at', 'Dukem', '!'
        ],
        'tag': [
            'U-restaurant', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'
        ] + [
            'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'U-restaurant', 'O', 'O', 'O', 'O'
        ] + [
            'O', 'O', 'O', 'O', 'B-dish', 'L-dish', 'O', 'O', 'B-dish', 'I-dish', 'L-dish', 'O', 'O', 'O', 'B-dish', 'L-dish', 'O'
        ] + [
            'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'
        ] + [
            'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'U-restaurant', 'O'
        ]
    }
    assert output == expected

@pytest.mark.parametrize('tag_head,expected', [
    ('', None),
    ('restaurant>Dukem', [('U-restaurant', 'Dukem')]),
    ('/restaurant> I was hooked.  My regular order is ', [('O', 'I'), ('O', 'was'), ('O', 'hooked'), ('O', '.'), ('O', 'My'), ('O', 'regular'), ('O', 'order'), ('O', 'is')]),
    ('dish>Awaze Tibs', [('B-dish', 'Awaze'), ('L-dish', 'Tibs')]),
    ('dish>Vegetable Combo Platter', [('B-dish', 'Vegetable'), ('I-dish', 'Combo'), ('L-dish', 'Platter')])
])
def test_extract_tags_from_tag_head(tag_head, expected):
    output = fts.extract_tags_from_tag_head(tag_head)
    print(output)
    print(expected)
    assert output == expected

def test_bilou_to_flair(example_tagged_texts):
    expected = '\n'.join([
        'My O',
        'regular O',
        'order O',
        'is O',
        'Awaze B-dish',
        'Tibs L-dish',
        'with O',
        'the O',
        'Vegetable B-dish',
        'Combo I-dish',
        'Platter L-dish',
        'along O',
        'with O',
        'a O',
        'mango B-dish',
        'juice L-dish',
        '. O',
        '',
        'Dukem U-restaurant',
        'is O',
        'a O',
        'staple O',
        'in O',
        'my O',
        'rotation O',
        'of O',
        'favorite O',
        'restaurants O',
        'to O',
        'eat O',
        'at O',
        'within O',
        'the O',
        'GTA O',
        '. O',
    ])
    output = fts.bilou_to_flair(example_tagged_texts)
    assert output == expected

def test_bilou_to_crfsuite(example_tagged_texts):
    expected = [
        [
            ('My', 'O'), ('regular', 'O'), ('order', 'O'), ('is', 'O'), ('Awaze', 'B-dish'), ('Tibs', 'L-dish'), ('with', 'O'), ('the', 'O'),
            ('Vegetable', 'B-dish'), ('Combo', 'I-dish'), ('Platter', 'L-dish'), ('along', 'O'), ('with', 'O'), ('a', 'O'), ('mango', 'B-dish'),
            ('juice', 'L-dish'), ('.', 'O')
        ],
        [
            ('Dukem', 'U-restaurant'), ('is', 'O'), ('a', 'O'), ('staple', 'O'), ('in', 'O'), ('my', 'O'), ('rotation', 'O'), ('of', 'O'),
            ('favorite', 'O'), ('restaurants', 'O'), ('to', 'O'), ('eat', 'O'), ('at', 'O'), ('within', 'O'), ('the', 'O'), ('GTA', 'O'), ('.', 'O')
        ]
    ]
    output = fts.bilou_to_crfsuite(example_tagged_texts)
    assert output == expected