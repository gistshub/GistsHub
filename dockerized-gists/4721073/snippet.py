from __future__ import with_statement
from alembic import context
from alembic.util.compat import configparser
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

import os
import re
import sys
basedir = os.path.abspath(os.path.dirname(__file__) + '/../')
sys.path.append(basedir)
from wakatime.config import SQLALCHEMY_DATABASE_URI
from wakatime.models import db

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_section_option('alembic', 'sqlalchemy.url', SQLALCHEMY_DATABASE_URI)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = db.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def include_object(object, name, obj_type, reflected, compare_to):
    try:
        section = config.get_section('alembic:exclude')
    except configparser.NoSectionError:
        return True

    exclude_tables = []
    tables = section.get('tables', None)
    if tables is not None:
        exclude_tables = [re.compile(pattern.strip(), re.IGNORECASE) for pattern in tables.split("\n")]

    if obj_type == 'table':
        found = False
        for pattern in exclude_tables:
            if pattern.search(name):
                found = True
                break
        if found:
            return False
    return True

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata,
                      include_object=include_object)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    engine = engine_from_config(
                config.get_section(config.config_ini_section),
                prefix='sqlalchemy.',
                poolclass=pool.NullPool)

    connection = engine.connect()
    context.configure(
                connection=connection,
                target_metadata=target_metadata,
                compare_server_default=True,
                compare_type=True,
                include_object=include_object
                )

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()