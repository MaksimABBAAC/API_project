import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey

from src.database import metadata
from src.auth.models import user

comments = Table(
    "comment",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("id_coin", Integer, nullable=False),
    Column("id_user", Integer, ForeignKey(user.c.id)),
    Column("message", String, nullable=False),
    Column("data_time", TIMESTAMP, default=datetime.datetime.utcnow)
)