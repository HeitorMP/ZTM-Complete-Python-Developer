# useful modules
import pyjokes
from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

joke = pyjokes.get_joke('en', 'neutral')
print(joke)

# collections
li = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = 'blah blah blah thinking about python'

print(Counter(li))
print(Counter(sentence))

# set a default value to a not found key
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['b'])

# keep the insertion order
d2 = OrderedDict()

d2['a'] = 1
d2['b'] = 2

print(d2)

"""
Recently, the Python has made Dictionaries ordered by default!
So unless you need to maintain older version of Python (older than 3.7),
you no longer need to use ordered dict, you can just use regular dictionaries!
"""
# datetime
print(datetime.date.today())

# array

arr = array('i', [1, 2, 3])
print(arr[0])
