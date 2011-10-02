import unittest
from tweetMining import TweetMining

class TweetMiningTestCase(unittest.TestCase):
    def setUp(self):
        self.tweetMining = TweetMining()
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
        self.assertIsInstance(self.tweetMining.search(), type({}))
    def test_search_containsResultsKey(self):
        result = self.tweetMining.search()
        actual = 'results' in result.keys()
        self.assertTrue(actual)
    def test_ResultsKeyIsAnArray(self):
        result = self.tweetMining.search()
        actual = result['results']
        self.assertTrue(isinstance(actual, list)) 
    def test_search_containsSince_IdKey(self):
        result = self.tweetMining.search()
        actual = 'since_id' in result.keys()
        self.assertTrue(actual)
    def test_ResultsKeyIsAnArray(self):
        result = self.tweetMining.search()
        actual = result['since_id']
        self.assertTrue(isinstance(actual, int)) 
    def test_search_containsQueryKey(self):
        result = self.tweetMining.search()
        actual = 'query' in result.keys()
        self.assertTrue(actual)
    def test_QueryKeyIsAString(self):
        result = self.tweetMining.search()
        actual = result['query']
        self.assertTrue(isinstance(actual, (str, unicode))) 
    def test_search_containsResults_per_pageKey(self):
        result = self.tweetMining.search()
        actual = 'results_per_page' in result.keys()
        self.assertTrue(actual)
    def test_Results_Per_PageKeyIsAnInt(self):
        result = self.tweetMining.search()
        actual = result['results_per_page']
        self.assertTrue(isinstance(actual, int)) 
    def test_search_containsMaxIdKey(self):
        result = self.tweetMining.search()
        actual = 'max_id' in result.keys()
        self.assertTrue(actual)
    def test_Max_IdKeyIsAnInteger(self):
        result = self.tweetMining.search()
        actual = result['max_id']
        self.assertTrue(isinstance(actual, (int, long))) 
    def test_serach_containsPageKey(self):
        result = self.tweetMining.search()
        actual = 'page' in result.keys()
        self.assertTrue(actual)
    def test_PageKeyIsAnInt(self):
        result = self.tweetMining.search()
        actual = result['page']
        self.assertTrue(isinstance(actual, int)) 
    def test_search_containsNextPageKey(self):
        result = self.tweetMining.search()
        actual = 'next_page' in result.keys()
        self.assertTrue(actual)
    def test_NextPageKeyIsAString(self):
        result = self.tweetMining.search()
        actual = result['next_page']
        self.assertTrue(isinstance(actual, (str, unicode))) 
    def test_search_containsCompleted_InKey(self):
        result = self.tweetMining.search()
        actual = 'completed_in' in result.keys()
        self.assertTrue(actual)
    def test_CompletedInKeyIsFloat(self):
        result = self.tweetMining.search()
        actual = result['completed_in']
        self.assertTrue(isinstance(actual, (float)))
    def test_search_containsRefreshUrlKey(self):
        result = self.tweetMining.search()
        actual = 'refresh_url' in result.keys()
        self.assertTrue(actual)
    def test_RefreshUrlKeyIsAString(self):
        result = self.tweetMining.search()
        actual = result['refresh_url']
        self.assertTrue(isinstance(actual, (str, unicode))) 
