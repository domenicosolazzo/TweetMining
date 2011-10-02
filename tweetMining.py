class TweetMining( object ):
    
    def trends(self):
        return {'trends':[], 'as_of':''}
    def search(self):
        return {
            'results':[], 'since_id':0, 'query':'twitter', 
            'results_per_page':10, 'max_id':10L, 'page':1,
            'next_page':'?page=2?max_id=222&q=twitter&rpp=10',
            'completed_in':0.106, 'refresh_url':'?since_id=222&q=twitter'
        }

