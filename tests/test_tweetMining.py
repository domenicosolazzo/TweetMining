import unittest
from tweetMining import TweetMining, TweetProxy, TestProxy, HttpProxy
import nltk

class TweetMiningTestCase(unittest.TestCase):
    def setUp(self):
        self.tweetMining = TweetMining(proxy='test')
        self.search = self.tweetMining.search(q="twitter")
        self.userInfoResponse = self.tweetMining.userInfo(username="fakeusername")
    def tearDown(self):
        self.tweetMining = None
    def test_instanceIsNotNone(self):
        self.assertIsNotNone(self.tweetMining)
    def test_tweetMiningIsInstanceOf(self):
        self.assertIsInstance(self.tweetMining, TweetMining)
    # setProxy
    def test_setProxy_exists(self):
        self.assertTrue(callable(getattr(self.tweetMining, "setProxy"))) 
    def test_setProxy_Raises_ExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.tweetMining.setProxy, 1)
        self.assertRaises(Exception, self.tweetMining.setProxy, "wrong")
    def test_setProxy_Returns_TweetProxyInstance(self):
        actual = self.tweetMining.setProxy('test')
        self.assertIsInstance(actual, TweetProxy)
    def test_setProxy_Returns_TestProxyInstance(self):
        actual = self.tweetMining.setProxy('test')
        self.assertIsInstance(actual, TestProxy)
    def test_setProxy_Returns_HttpProxyInstance(self):
        actual = self.tweetMining.setProxy('http')
        self.assertIsInstance(actual, HttpProxy)
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
    # _get_rt_sources
    def test_getRTSources_exists(self):
        self.assertTrue(callable(getattr(self.tweetMining, "_getRTSources")))
    def test_getRTSources_returnsAList(self):
        actual = self.tweetMining._getRTSources('RT @user la la la')
        self.assertIsInstance(actual, list)
    def test_getRTSources_raisesAnExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.tweetMining._getRTSources, 1)
        self.assertRaises(Exception, self.tweetMining._getRTSources, [])
        self.assertRaises(Exception, self.tweetMining._getRTSources, {})
    # buildRetweetGraph
    def test_buildRetweetGraph_exists(self):
        self.assertTrue(callable(getattr(self.tweetMining, "buildRetweetGraph")))
    def test_buildRetweetGraph_ReturnsADict(self):
        actual = self.tweetMining.buildRetweetGraph(self.search['results'])
        self.assertIsInstance(actual, dict)
    def test_buildRetweetGraph_Dict_containsGraphKey(self):
        actual = self.tweetMining.buildRetweetGraph(self.search['results'])
        self.assertTrue('graph' in actual.keys())
        self.assertIsNotNone(actual['graph'])
    def test_buildRetweetGraph_RaisesAnExceptionWithWrongInput(self):
        self.assertRaises(Exception ,self.tweetMining.buildRetweetGraph, 1)
        self.assertRaises(Exception ,self.tweetMining.buildRetweetGraph, "1")
        self.assertRaises(Exception ,self.tweetMining.buildRetweetGraph, {})
    # userInfo
    def test_userInfo_exists(self):
        self.assertTrue(callable(getattr(self.tweetMining, "userInfo")))
    def test_userInfo_ReturnsADict(self):
        actual = self.userInfoResponse
        self.assertIsInstance(actual, dict)
    def test_userInfo_Dict_ContainsAProfile_Background_TileKey(self):
        key = 'profile_background_tile'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, bool)
    def test_userInfo_Dict_ContainsAProtectedKey(self):
        key = 'protected'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, bool)
    def test_userInfo_Dict_ContainsAShow_All_Inline_MediaKey(self):
        key = 'show_all_inline_media'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, bool)
    def test_userInfo_Dict_ContainsAListedCountKey(self):
        key = 'listed_count'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, int)
    def test_userInfo_Dict_ContainsAContributorsEnabledKey(self):
        key = 'contributors_enabled'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, bool)
    def test_userInfo_Dict_ContainsAProfile_Sidebar_fill_colorKey(self):
        key = 'profile_sidebar_fill_color'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, unicode)
    def test_userInfo_Dict_ContainsANameKey(self):
        key = 'name'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, unicode)
    def test_userInfo_Dict_Contains_VerifiedKey(self):
        key = 'verified'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, bool)
    def test_userInfo_Dict_Contains_LangKey(self):
        key = 'lang'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, unicode)
    def test_userInfo_Dict_Contains_DescriptionKey(self):
        key = 'description'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, unicode)
    def test_userInfo_Dict_Contains_StatusesCountKey(self):
        key = 'statuses_count'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, int)
    def test_userInfo_Dict_Contains_Profile_Image_Url(self):
        key = 'profile_image_url'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, unicode)
    def test_userInfo_Dict_Contains_StatusKey(self):
        key = 'status'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, dict)
    def test_userInfo_Dict_Contains_UrlKey(self):
        key = 'url'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, unicode)
    def test_userInfo_Dict_Contains_Screen_NameKey(self):
        key = 'screen_name'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value,unicode)
    def test_userInfo_Dict_Contains_Friends_CountKey(self):
        key = 'friends_count'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, int)
    def test_userInfo_Dict_Contains_Followers_CountKey(self):
        key = 'followers_count'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, int)
    def test_userInfo_Dict_Contains_Favourites_CountKey(self):
        key = 'favourites_count'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, int)
    def test_userInfo_Dict_Contains_IdKey(self):
        key = 'id'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, int)
    def test_userInfo_Dict_Contains_IdStrKey(self):
        key = 'id_str'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, unicode)
   # _getFactory
    def test_userInfo_Dict_Contains_Friends_CountKey(self):
        key = 'friends_count'
        value = self.userInfoResponse.get(key)
        self.assertTrue(key in self.userInfoResponse.keys())
        self.assertIsInstance(value, int)
    def test__getFactoryProxy_exists(self):
        self.assertTrue(callable(getattr(self.tweetMining, "_getFactoryProxy")))
    def test__getFactoryProxy_Raises_ExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.tweetMining._getFactoryProxy, "wrong") 
        self.assertRaises(Exception, self.tweetMining._getFactoryProxy, 1)
    def test__getFactoryProxy_Returns_TweetProxyInstance(self):
        actual = self.tweetMining._getFactoryProxy('test')
        self.assertIsInstance(actual, TweetProxy) 
