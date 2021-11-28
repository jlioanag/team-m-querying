import unittest
from query import remove_stop_words, lemmatize_query, stem_query, autocorrect, create_query_result 


class TestQueryComponents(unittest.TestCase):

    '''
    Unit tests for remove_stop_words
    '''

    def test_no_stop_words(self):
        pass

    def test_only_stop_words(self):
        pass

    def test_stop_words_empty(self):
        pass

    '''
    Unit tests for lemmatize_query
    '''

    def test_lemmatize_same_lemma(self):
        pass

    def test_lemmatize_invalid_chars(self):
        pass

    def test_lemmatize_empty(self):
        pass

    '''
    Unit tests for stem_query
    '''

    def test_stem_valid_string(self):
        pass

    def test_stem_empty_string(self):
        pass

    def test_stem_invalid_string(self):
        pass

    '''
    Unit tests for autocorrect
    '''

    def test_autocorrect_correct(self):
        pass

    def test_autocorrect_typos_light(self):
        pass

    def test_autocorrect_typos_heavy(self):
        pass

    '''
    Unit tests for create_query_result
    '''
    # TBD
