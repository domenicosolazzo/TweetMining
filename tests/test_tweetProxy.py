import unittest
from tweetMining import TweetProxy, TestProxy, HttpProxy
class TweetProxyTestCase(unittest.TestCase):
    def setUp(self):
        self.proxy = TweetProxy()
    def tearDown(self):
        self.proxy = None
    def test_trends_exists(self):
        self.assertTrue(callable(getattr(self.proxy, "trends")))
    def test_trends_Raises_Exception(self):
        self.assertRaises(NotImplementedError, self.proxy.trends)
    def test_search_exists(self):
        self.assertTrue(callable(getattr(self.proxy, "search")))
    def test_search_Raises_Exception(self):
        self.assertRaises(NotImplementedError, self.proxy.search, *("search",))
    def test_userInfo_exists(self):
        self.assertTrue(callable(getattr(self.proxy, "userInfo")))
    def test_search_Raises_Exception(self):
        self.assertRaises(NotImplementedError, self.proxy.userInfo, "username")

class TestProxyTestCase(unittest.TestCase):
    def setUp(self):
        self.proxy = TestProxy()
    def tearDown(self):
        self.proxy = None
    # Trends
    def test_trends_Returns_Dict(self):
        self.assertIsInstance(self.proxy.trends(), dict)
    # Search
    def test_search_Returns_Dict(self):
        self.assertIsInstance(self.proxy.search("search"), dict)
    # UserInfo
    def test_userInfo_Returns_Dict(self):
        self.assertIsInstance(self.proxy.userInfo("username"), dict)
