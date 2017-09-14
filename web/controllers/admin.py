from ..models import WordCount
from ..utils import Paginator
from .base import BaseHandler


class AdminHandler(BaseHandler):
    def get(self):
        paginator = Paginator(
            WordCount.select().order_by(
                WordCount.count.desc(),
                WordCount.created.desc()
            ),
            int(self.get_argument('page', 1))
        )
        self.render_template(
            'admin.html',
            wordcounts=paginator.results(),
            paginator=paginator,
        )


__all__ = ['AdminHandler']
