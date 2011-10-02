import unittest
from tweetMining import TweetMining
import nltk

class TweetMiningTestCase(unittest.TestCase):
    def setUp(self):
        self.tweetMining = TweetMining()
        self.search = self.tweetMining.search(q="twitter")
    def tearDown(self):
        self.tweetMining = None
    def test_instanceIsNotNone(self):
        self.assertIsNotNone(self.tweetMining)
    def test_tweetMiningIsInstanceOf(self):
        self.assertIsInstance(self.tweetMining, TweetMining) 
    # Trends
    def test_Trends_exists(self):
        self.assertTrue(callable(getattr(self.tweetMining, "trends")))
    def test_Trends_returnsADict(self):
        self.assertIsInstance(self.tweetMining.trends(), type({}))
    def test_Trends_containsTrendsKey(self):
        result = self.tweetMining.trends()
        actual = 'trends' in result.keys()
        self.assertTrue(actual)
    def test_TrendsKeyIsAnArray(self):
        result = self.tweetMining.trends()
        actual = result['trends']
        self.assertTrue(isinstance(actual, list)) 
    def test_Trends_containsAs_OfKey(self):
        result = self.tweetMining.trends()
        actual = 'as_of' in result.keys()
        self.assertTrue(actual)
    def test_As_OfKeyIsAString(self):
        result = self.tweetMining.trends()
        actual = str(result['as_of'])
        self.assertTrue(isinstance(actual, str))
    # Search 
    def test_search_exists(self):
        self.assertTrue(callable(getattr(self.tweetMining, "search")))
    def test_search_returnsADict(self):
        self.assertIsInstance(self.search, type({}))
    def test_search_containsResultsKey(self):
        actual = 'results' in self.search.keys()
        self.assertTrue(actual)
    def test_ResultsKeyIsAnArray(self):
        actual = self.search['results']
        self.assertTrue(isinstance(actual, list)) 
    def test_search_containsSince_IdKey(self):
        actual = 'since_id' in self.search.keys()
        self.assertTrue(actual)
    def test_ResultsKeyIsAnArray(self):
        actual = self.search['since_id']
        self.assertTrue(isinstance(actual, int)) 
    def test_search_containsQueryKey(self):
        actual = 'query' in self.search.keys()
        self.assertTrue(actual)
    def test_QueryKeyIsAString(self):
        actual = self.search['query']
        self.assertTrue(isinstance(actual, (str, unicode))) 
    def test_search_containsResults_per_pageKey(self):
        actual = 'results_per_page' in self.search.keys()
        self.assertTrue(actual)
    def test_Results_Per_PageKeyIsAnInt(self):
        actual = self.search['results_per_page']
        self.assertTrue(isinstance(actual, int)) 
    def test_search_containsMaxIdKey(self):
        actual = 'max_id' in self.search.keys()
        self.assertTrue(actual)
    def test_Max_IdKeyIsAnInteger(self):
        actual = self.search['max_id']
        self.assertTrue(isinstance(actual, (int, long))) 
    def test_serach_containsPageKey(self):
        actual = 'page' in self.search.keys()
        self.assertTrue(actual)
    def test_PageKeyIsAnInt(self):
        actual = self.search['page']
        self.assertTrue(isinstance(actual, int)) 
    def test_search_containsNextPageKey(self):
        actual = 'next_page' in self.search.keys()
        self.assertTrue(actual)
    def test_NextPageKeyIsAString(self):
        actual = self.search['next_page']
        self.assertTrue(isinstance(actual, (str, unicode))) 
    def test_search_containsCompleted_InKey(self):
        actual = 'completed_in' in self.search.keys()
        self.assertTrue(actual)
    def test_CompletedInKeyIsFloat(self):
        actual = self.search['completed_in']
        self.assertTrue(isinstance(actual, (float)))
    def test_search_containsRefreshUrlKey(self):
        actual = 'refresh_url' in self.search.keys()
        self.assertTrue(actual)
    def test_RefreshUrlKeyIsAString(self):
        actual = self.search['refresh_url']
        self.assertTrue(isinstance(actual, (str, unicode)))
    # Words
    def test_words_exists(self):
        self.assertTrue(callable(getattr(self.tweetMining, "words")))
    def test_words_raisesAnExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.tweetMining.words, 1)
        self.assertRaises(Exception, self.tweetMining.words, "1")
        self.assertRaises(Exception, self.tweetMining.words, (1,))
        self.assertRaises(Exception, self.tweetMining.words, {1:1})
    def test_words_acceptsAListAsInput(self):
        self.assertIsInstance(self.tweetMining.words([]), list)
    def test_words_returnsAnArray(self):
        actual = self.tweetMining.words(self.search['results'])
        self.assertIsInstance(actual, list)
    # FreqDist
    def test_freqDist_exists(self):
        self.assertTrue(callable(getattr(self.tweetMining, "freqDist")))
    def test_freqDist_raisesAnExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.tweetMining.freqDist, 1)
        self.assertRaises(Exception, self.tweetMining.freqDist, "1")
        self.assertRaises(Exception, self.tweetMining.freqDist, (1,))
        self.assertRaises(Exception, self.tweetMining.freqDist, {1:1})
    def test_freqDist_acceptsAListAsInput(self):
        self.assertEquals(type(self.tweetMining.freqDist([])), nltk.probability.FreqDist)
    def test_freqDist_returnsAnArray(self):
        words = self.tweetMining.words(self.search['results'])
        actual = self.tweetMining.freqDist(words)
        self.assertEquals(type(actual), nltk.probability.FreqDist)
