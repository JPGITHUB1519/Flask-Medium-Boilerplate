#!flask/bin/python
""" It is not a common need to have to downgrade a database to an old format, but just in case, 
SQLAlchemy-migrate supports this as well (file db_downgrade.py):
This script will downgrade the database one revision. You can run it multiple times to downgrade several revisions.
"""
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))