import pprint
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer

pp = pprint.PrettyPrinter(width=41, compact=True)

vegeta_quotes = [
    ('voce nao e derrotado quando perde, mais sim quando voce desiste.', 'confiante'),
    ('O melhor guerreiro nao e aquele que sempre ganha, mas o que mantem o seu orgulho mesmo na derrota', 'orgulhoso'),
    ('Enquanto o inimigo estiver na minha frente, eu lutarei.', 'confiante'),
    ('Eu sou calmo e tenho o coracao puro... mas e pura maldade.', 'sincero'),
    ('Meu coracao e puro... pura maldade!', 'sincero'),
    ('Verme insolente nao entre na frente.', 'bravo'),
    ('O miseravel e um genio.', 'feliz')
]

stop_words = set(stopwords.words('portuguese') + [
    ',',
    'eu',
    '!'
])

# Steamming words, derrota or derrotar or derrotei == derrot
stemmer = RSLPStemmer()
quotes = [(stemmer.stem(q.lower()), f) for (q, f) in vegeta_quotes]

filtered = []

for (quote, felling) in quotes:
    filtered.append(
        (
            [w for w in word_tokenize(quote)
             if not w in stop_words and w.isalpha()],
            felling
        )
    )

pp.pprint(filtered)
# [..., ['melhor', 'guerreiro', 'nao', 'sempre', 'ganha', 'mantem', 'orgulho', 'derrot'], ... ]
