import unittest
from query import remove_stop_words, lemmatize_query, stem_query, autocorrect, create_query_result


class TestQueryComponents(unittest.TestCase):

    '''
    Unit tests for remove_stop_words
    '''

    # Tests if there are no stop words in remove_stop_words input
    def test_no_stop_words(self):
        self.assertEqual(remove_stop_words('pork and beans'), 'pork beans')

    # Tests if there are only stop words in remove_stop_words input
    def test_only_stop_words(self):
        self.assertEqual(remove_stop_words('and of but'), '')

    # Tests if remove_stop_words input is empty string
    def test_stop_words_empty(self):
        self.assertEqual(remove_stop_words(''), '')

    '''
    Unit tests for lemmatize_query
    '''

    # Tests a simple lemmatize
    def test_lemmatize_simple_lemma(self):
        self.assertEqual(lemmatize_query(
            'the boy cries wolf'), 'the boy cry wolf')

    # Tests a simple lemmatize on invalid (non alphanumeric) characters
    def test_lemmatize_invalid_chars(self):
        self.assertEqual(lemmatize_query('እንዴት ኖት'), 'እንዴት ኖት')

    # Tests a simple lemmatize empty input
    def test_lemmatize_empty(self):
        self.assertEqual(lemmatize_query(''), '')

    '''
    Unit tests for stem_query
    '''

    # Tests a simple stem valid string input
    def test_stem_valid_string(self):
        self.assertEqual(stem_query('he bought the newspaper at the store this morning'),
                         'he bought the newspap at the store thi morn')

    # Tests a empty string input
    def test_stem_empty_string(self):
        self.assertEqual(stem_query(''), '')

    # Tests an invalid (non alphanumeric) input
    def test_stem_invalid_string(self):
        self.assertEqual(stem_query('እንዴት ኖት'), 'እንዴት ኖት')

    '''
    Unit tests for autocorrect
    '''

    # Tests autocorrect on an already correct string
    def test_autocorrect_correct(self):
        self.assertEqual(autocorrect('this is a test'), 'this is a test')

    # Tests autocorrect on a string with slight typos
    def test_autocorrect_typos_light(self):
        self.assertEqual(autocorrect('thsi iS a stet'), 'this is a test')

    # Tests autocorrect on a string with heavy typos
    def test_autocorrect_typos_heavy(self):
        self.assertEqual(autocorrect(
            'thisdkfaj is a afdlkjstestsdf'), 'this is a test')

    '''
    Unit tests for create_query_result
    '''

    # Tests simple query result creation
    def test_simple_query_result(self):
        input = ['The quick brown fox jumps over the lazy dog.', 2, 1]

        res = {
            'query_display': 'The quick brown fox jumps over the lazy dog.',
            'document_id': 2,
            'qid': 1
        }

        self.assertEqual(res, create_query_result(input))
    
    # Tests invalid (non alphanumeric) string query result creation
    def test_invalid_string_query_result(self):
        input = ['篠の葉に雪降りつもる冬の夜に豊の遊びをするが愉しさ', 2, 1]

        res = {
            'query_display': '篠の葉に雪降りつもる冬の夜に豊の遊びをするが愉しさ',
            'document_id': 2,
            'qid': 1
        }

        self.assertEqual(res, create_query_result(input))
    
    # Tests empty string for query result creation
    def test_empty_query_result(self):
        input = []

        res = 'No results.'

        self.assertEqual(res, create_query_result(input))


if __name__ == '__main__':
    unittest.main()
