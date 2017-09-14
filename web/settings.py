import os
import uuid
from tornado.options import define
import tornado.template

# Make filepaths relative to settings.
path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

DEBUG = os.environ.get('GAE_PARTITION', 'prod') != 'dev'

define("port", default=8080, help="run on the given port", type=int)

tornado.options.parse_command_line()

template_dir = path(ROOT, 'templates')
static_dir = path(ROOT, 'static')


settings = dict(
    static_path=static_dir,
    template_loader=tornado.template.Loader(template_dir),
    xsrf_cookies=True,
    cookie_secret=os.getenv('COOKIE_SECRET', str(uuid.uuid4())),
    page_size=20
)
