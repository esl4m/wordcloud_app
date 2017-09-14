from collections import Counter, namedtuple
import re
from BeautifulSoup import BeautifulSoup, Comment
from .stopwords import STOPWORDS

Wordcount = namedtuple('Wordcount', ('word', 'count'))


class WordCloud(object):
    """
    WordCloud generates word frequencies for a given text
    Attributes:
        html - text to extract word and frequencies
        max_words - number of top words to show, default 100
        min_words - length of words to ignore, default 3

    >>> wc = WordCloud(html_content).generate()
    >>> wc.frequencies
    """

    def __init__(self, html, max_words=100, min_words=3):
        self._html = html
        self.max_words = max_words
        self.min_words = min_words
        self.frequencies = []

    def _sanitize(self, html):
        """
        Clean html by removing tags, comments etc
        Returns: str
        """
        blacklist = ['style', 'script', '[document]', 'head', 'title', 'meta']
        soup = BeautifulSoup(html)

        for s in soup(blacklist):
            s.extract()
        for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
            comment.extract()
        return soup.getText()

    def tokenize(self):
        """
        Split text into words
        Returns: list
        """
        clean_text = self._sanitize(self._html)
        words = re.findall(r"\w+", clean_text.lower())
        return [word for word in words if word not in STOPWORDS and
                len(word) > self.min_words]

    def generate(self):
        """
        Generate word frequencies for word list
        """
        words = self.tokenize()
        self.frequencies = Counter(words).most_common(self.max_words)
        return self

    def iter_words(self):
        """
        Returns generator of word and scaled count as tuple
        """
        max_count = self.frequencies[0][1]
        for word, count in self.frequencies:
            yield Wordcount(word, self._scale(count, max_count))

    def _scale(self, count, max_count):
        """
        Normalize word count for css style classes
        """
        return int(10 * count / max_count)


__all__ = ['WordCloud']
