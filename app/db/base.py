import sys
sys.path = ['', '..'] + sys.path[1:]
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
from db.session import Base
from db.models import *
