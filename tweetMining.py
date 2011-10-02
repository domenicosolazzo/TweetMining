import json
class TweetMining( object ):
    
    def trends(self):
        return json.loads(open('tests/fixtures/trends.json').read())
    def search(self, q, rpp=10, firstPage=1, lastPage=2):
        return json.loads(open('tests/fixtures/search.json').read())
    def words(self, search):
        tweets = [tweet['text'] for tweet in search]
        words = []
        for t in tweets:
            words += [ w for w in t.split() ]
        return words
