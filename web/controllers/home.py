from datetime import datetime
import logging
from google.appengine.api import urlfetch
from ..models import WordCount
from ..utils import WordCloud
from .base import BaseHandler


class HomeHandler(BaseHandler):

    def get(self):
        url = self.get_argument('url', None)
        wordcloud = []
        if url:
            wordcloud = self._generate_wordcloud(self._fetch_url(url))
        self.render_template('index.html', url=url, wordcloud=wordcloud)

    def _generate_wordcloud(self, content):
        """
        Generate word cloud from given content
        """
        wordcloud = WordCloud(content).generate()
        self.save_frequencies(wordcloud)
        return wordcloud.iter_words()

    def _fetch_url(self, url):
        """
        Fetch and return content of url
        """
        try:
            res = urlfetch.fetch(self.fix_url(url))
            if res.status_code == 200:
                return res.content
            else:
                logging.exception('Caught exception fetching url')
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

    def fix_url(self, url):
        if url.startswith('http'):
            return url
        return 'http://{}'.format(url)

    def save_frequencies(self, wordcloud):
        """
        Save word frequencies to database
        """
        for word, count in wordcloud.frequencies:
            word_hash = WordCount.generate_hash(word)
            enc_word = WordCount.encrypt(word)
            wc, created = WordCount.create_or_get(id=word_hash)
            wc.word = enc_word
            wc.count += count
            wc.updated = datetime.now()
            wc.save()


__all__ = ['HomeHandler']
