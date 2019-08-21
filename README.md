## Python Text Mining - Examples
## Activate environment

First of all activate python virtual environment.

```
source .env/bin/activate
```

## Installation

Install packages over pip

```
pip install -r requirements.txt
```

### NLTK Packages

NTLK requires some extra data.

```
python -m nltk.downloader popular rslp
```

### Run samples

```
python 01_stop_words.py
python 02_steamer.py
python 03_words_frequencies.py
```
