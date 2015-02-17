from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
person = Table('person', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=120), nullable=False),
    Column('password', String(length=120), nullable=False),
    Column('nickname', String(length=120), nullable=False),
    Column('sex', String(length=50), nullable=False),
    Column('firstname', String(length=120)),
    Column('lastname', String(length=120)),
    Column('birthdate', DateTime),
    Column('weight', Float),
    Column('height', Float),
    Column('category', Enum('etudiant', 'enseignant', 'iatos'), nullable=False),
    Column('type', String(length=50)),
    Column('etat', Enum('PREREGISTERED', 'REGISTERED', 'DROPPED'), nullable=False),
    Column('token', String(length=128)),
    Column('image', String(length=120)),
    Column('group_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].columns['group_id'].create()
    post_meta.tables['person'].columns['image'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].columns['group_id'].drop()
    post_meta.tables['person'].columns['image'].drop()
