from autocorrect import Speller
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

spell = Speller()


def remove_stop_words(query: str) -> str:
    stop_words = set(stopwords.words('english'))

    return ' '.join([word for word in word_tokenize(query) if word not in stop_words])


def lemmatize_query(query: str) -> str:
    lemmatizer = WordNetLemmatizer()

    return ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(query)])


def stem_query(query: str) -> str:
    stemmer = PorterStemmer()

    return ' '.join([stemmer.stem(word) for word in word_tokenize(query)])


def autocorrect(query: str) -> str:
    spell = Speller()

    return spell(query)


def create_query_result(results: list):
    if not results:
        return 'No results.' 
    
    res = {
        'query_display': results[0], 
        'document_id':  results[1],
        'qid':  results[2]
    }
    
    return res
