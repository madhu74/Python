import time
 
class LRUCache(object):
    def __init__(self, max_keys):
        """
        Constructor: creates an LRUCache that can hold max_keys items.
        """
        self.max_keys = max_keys
        self.storage = [] # Stores (key, value, last_access_ts), ts stands for timestamp :D
 
    def get(self, query_key):
        """
        Returns the value associated with query_key (or None if it doesn't exist).
        """
        for (key, value, last_access_ts) in self.storage:
            if key == query_key:
                return value
        return None
 
    def set(self, new_key, new_value):
        """
        Stores new_value, which can be retrieved using new_key.
        This may cause the oldest item to be evicted if adding the item would
        cause there to be more than max_keys items.
        """
        new_item = (new_key, new_value, time.time())
        # Python tip: time.time() gives you the current time in seconds as a float
        self.storage.append(new_item)
 
        # Remove the last accessed item
        if len(self.storage) > self.max_keys:
            least_recent_item = new_item
            for (key, value, last_access_ts) in self.storage:
                if last_access_ts < least_recent_item[2]:
                    least_recent_item = (key, value, last_access_ts)
            # Python tip: remove(x) removes the first item from the list whose value is x
            self.storage.remove(least_recent_item)
 
def testLRUCache():
    cache = LRUCache(2)
 
    print "Running test...",
    cache.set('a', 'b')
    cache.set('b', 'c')
    cache.set('c', 'a')
    assert cache.get('b') == 'c'
    assert cache.get('c') == 'a'
    assert cache.get('a') == None
    print "passed!"
 
testLRUCache()   
#cache = LRUCache(2)   