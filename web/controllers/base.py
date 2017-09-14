from datetime import datetime
from tornado import web


class BaseHandler(web.RequestHandler):
    def prepare(self, *args, **kwargs):
        self.context = dict(
            page_title="WordCloud",
            page_desc="WordCloud analyzer from url",
            date=datetime.utcnow()
        )
        super(BaseHandler, self).prepare(*args, **kwargs)

    def on_finish(self, *args, **kwargs):
        # self.application.db.close()
        super(BaseHandler, self).on_finish(*args, **kwargs)

    @property
    def db(self):
        return self.application.db

    def render_template(self, template, **kwargs):
        self.context.update(kwargs)
        self.render(template, **self.context)


__all__ = ['BaseHandler']
