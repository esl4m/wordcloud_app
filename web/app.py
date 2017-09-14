from tornado import web
from .controllers import HomeHandler, AdminHandler
from .settings import settings
from .models import database, init_db


class Application(web.Application):
    def make_app(self):
        handlers = (
            (r"/", HomeHandler),
            (r"/admin", AdminHandler),
        )

        app = web.Application(handlers, **settings)
        app.db = database
        init_db()
        return app
