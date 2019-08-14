import pprint
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

pp = pprint.PrettyPrinter(width=41, compact=True)

vegeta_quotes = [
    ('voce nao e derrotado quando perde, mais sim quando você desiste.', 'confiante'),
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

filtered = []

for (quote, felling) in vegeta_quotes:
    filtered.append(
        (
            [w for w in word_tokenize(quote.lower())
             if not w in stop_words and w.isalpha()],
            felling
        )
    )

pp.pprint(filtered)
# [ (['voce', 'nao', 'derrotado', 'perde', 'sim', 'desiste'], 'confiante'), ... ]
