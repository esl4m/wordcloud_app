import os
from peewee import *

# These environment variables are configured in app.yaml.
CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')

# create a peewee database instance -- our models will use this database to
# persist information
if (os.getenv('SERVER_SOFTWARE') and os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
    database = MySQLDatabase(
        'wordcloudapp',
        unix_socket=os.path.join('/cloudsql', CLOUDSQL_CONNECTION_NAME),
        user=os.getenv('MYSQL_DB_USER', 'root')
    )
else:
    database = MySQLDatabase(
        'wordcloudapp',
        user=os.getenv('MYSQL_DB_USER', 'root'),
        host=os.getenv('MYSQL_DB_HOST', 'localhost'),
        threadlocals=True
    )

# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use. then, any subclasses will automatically
# use the correct storage.


class BaseModel(Model):

    class Meta:
        database = database
