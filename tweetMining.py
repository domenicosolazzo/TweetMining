import json
class TweetMining( object ):
    
    def trends(self):
        return json.loads(open('tests/fixtures/trends.json').read())
    def search(self, q, rpp=10, firstPage=1, lastPage=2):
        return json.loads(open('tests/fixtures/search.json').read())
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
        patterns = re.compile(r" (RT|via) ((?:\b\W*@\w+)+)", re.IGNORECASE)
        return  [ source.strip() 
                  for tuple in patterns.findall(tweet)
                    for source in tuple
                        if source not in ("RT", "via")
                ]
    def buildRetweetGraph(self, tweets):
        pass
