import pprint
from itertools import chain
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer

pp = pprint.PrettyPrinter(width=41, compact=True)

yoda_quotes = [
    ('o medo e o caminho para o lado negro.', 'sincero'),
    ('treine a si mesmo a deixar partir tudo que teme perder.', 'confiante'),
    ('faca ou nao faca. a tentativa nao existe.', 'sincero'),
    ('que a forca esteja com voce!', 'confiante'),
    ('melhor professor, o fracasso e', 'sincero'),
    ('muito a aprender voce ainda tem.', 'bravo'),
    ('verdadeiramente maravilhosa, a mente de uma crianca.', 'feliz')
]

stop_words = set(stopwords.words('portuguese') + [
    ',',
    'eu',
    '!'
])

stemmer = RSLPStemmer()
quotes = [(stemmer.stem(q.lower()), f) for (q, f) in yoda_quotes]

filtered = []

for (quote, felling) in quotes:
    filtered.append(
        (
            [w for w in word_tokenize(quote.lower())
             if not w in stop_words and w.isalpha()],
            felling
        )
    )

# Just flatten words array [['nao'], ['sim']] to ['nao', 'sim']
all_words = chain.from_iterable([w for (w, _) in filtered])

freq_dist = nltk.FreqDist(all_words)

for word, frequency in freq_dist.most_common(50):
    print(u'{};{}'.format(word, frequency))
