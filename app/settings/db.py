from databases import Database
from ormar import ModelMeta
from sqlalchemy import create_engine, MetaData

from app.settings.config import settings

database = Database(settings.db_url)
metadata = MetaData()


class BaseMeta(ModelMeta):
    metadata = metadata
    database = database


engine = create_engine(settings.db_url)


async def init_db():
    with engine.begin():
        metadata.create_all(engine)
