import json
class TweetMining( object ):
    def __init__(self, proxy='http'):
        self.__proxy  = self.setProxy(proxy) 
    def setProxy(self, proxyName):
        proxy = self._getFactoryProxy(proxyName)
        return proxy 
    def _getFactoryProxy(self, factoryName):
        validNames = ['test', 'http']
        if not factoryName in validNames:
            raise Exception("Invalid Proxy name")
        proxy = None
        if factoryName == "test":
            proxy = TestProxy()
        elif factoryName == "http":
            proxy = HttpProxy()
        else:  
            raise Exception("This proxy( %s ) is not implemented yet" % (proxyName))
        return proxy
    def trends(self):
        return self.__proxy.trends()
    def search(self, q, rpp=10, firstPage=1, lastPage=2):
        return self.__proxy.search(q, rpp, firstPage, lastPage)
    def userInfo(self, username):
        return self.__proxy.userInfo(username)
    def words(self, search):
        if not isinstance(search, list):
            raise Exception("Wrong Input")
        tweets = [tweet['text'] for tweet in search if 'text' in tweet]
        words = []
        for t in tweets:
            words += [ w for w in t.split() ]
        return words
    def freqDist(self, words):
        if not isinstance(words, list):
            raise Exception("Wrong Input.")
        import nltk
        return nltk.FreqDist(words)
    def _getRTSources(self, tweet):
        if not isinstance(tweet, (str, unicode)):
            raise Exception('Wrong Input')
        import re
        patterns = re.compile(r"(RT|via)((?:\b\W*@\w+)+)", re.IGNORECASE)
        return  [ source.strip() 
                  for tuple in patterns.findall(tweet)
                    for source in tuple
                        if source not in ("RT", "via")
                ]
    def buildRetweetGraph(self, tweets):
        import networkx
        graph = networkx.DiGraph()
        if not isinstance(tweets, list):
            raise Exception('Wrong Input')
        for tweet in tweets:
            rtSources = self._getRTSources(tweet['text'])
            if not rtSources: continue
            for source in rtSources:
                graph.add_edge(source, tweet["from_user"], {"tweet_id" : tweet["id"]})
        return {'graph':graph}
class TweetProxy():
    def trends(self):
        raise NotImplementedError("Not Implemented Yet")
    def userInfo(self, username):
        raise NotImplementedError("Not Implemented Yet")
    def search(self, q, rpp=10, firstPage=1, lastPage=2):
        raise NotImplementedError("Not Implemented Yet")
    def login(self):
        raise NotImplementedError("Not Implemented Yet")
class TestProxy(TweetProxy):
    def trends(self):
        return json.loads(open('tests/fixtures/trends.json').read())
    def search(self, q, rpp=10, firstPage=1, lastPage=2):
        return json.loads(open('tests/fixtures/search.json').read())
    def userInfo(self, username):
        return json.loads(open('tests/fixtures/user.json').read())
    def login(self):
        return {'data':{}, 'error':None}  

class HttpProxy(TweetProxy):
    def __init__(self):
        import twitter
        self.__twitterProxy = twitter.Twitter(domain="api.twitter.com", api_version='1')
        self.__twitterSearchProxy = twitter.Twitter(domain="search.twitter.com")
    def trends(self):
        return self.__twitterProxy.trends()
    def search(self, q, rpp=10, firstPage=1, lastPage=2):
        searchResults = []
        for page in range(firstPage, lastPage):
            searchResults.append(self.__twitterSearchProxy.search(q=q, rpp=rpp, page=page))
        
        return searchResults
    def userInfo(self, username):
        return self.__twitterProxy.users.show(screen_name=username)
