# add-and-search-word-data-structure-design
Looks like I am taking too much time solving this.
It feels like wherever I am headed towards is not optimal.
I am thinking very brute force.

So I start seeing solutions.

```python
class WordDictionary():
    def __init__(self):
        self.trie = dict()

    def add_word(self, word):
        cur = self.trie
        for c in word + "$": cur = cur.setdefault(c, {})

    def search(self, word, cur=None):
        if not cur: cur = self.trie
        return "$" in cur if not word \
            else self.search(word[1:], cur[word[0]]) if word[0] in cur \
            else False if 'a' <= word[0] <= 'z' \
            else any(self.search(word[1:], cur[c]) for c in cur if c!="$")
```

Lets's dissect.

```python
def __init__(self):
    self.trie = dict()
```
Makes a trie with a dict. Okay.

```python
def add_word(self, word):
    cur = self.trie
    for c in word + "$": cur = cur.setdefault(c, {})
```
Inserts c into dict using `setdefault`. Good call.
`$` is used to determine ending key.
Cool.

```python
def search(self, word, cur=None):
    if not cur: cur = self.trie
    return "$" in cur if not word \
        else self.search(word[1:], cur[word[0]]) if word[0] in cur \
        else False if 'a' <= word[0] <= 'z' \
        else any(self.search(word[1:], cur[c]) for c in cur if c!="$")
```
This is a recursive method.

So `cur` gives the current trie node.
If `word is None`, then returns `True` or `False` depending on whether `$` in `cur`.
So now `word` is not None.
If `word[0] in cur` we return `search(word[1:], curr[word[0]]`.
So now `word[0]` is not in `cur`.
If `word[0]` is between `"a"` and `"z"` then return False.
So now `word[0] == "."`.
So now `search(word[1:], cur[c]) for c in cur if c!="$"`.

This means the complexity is no better than what I expected.
It is exponential in number of `.`s in the word.

It is always good to think in term of recursion in case of exponential complexities.

A trick I picked up:
```python
from collections import defaultdict
    
def _trie():
    return defaultdict(_trie)
```

This is a very short way of making a trie.
