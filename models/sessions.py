import sqlalchemy

from db.conn import db

sessions = sqlalchemy.Table(
    "sessions",
    db.metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("ip_address", sqlalchemy.String, index=True),
    sqlalchemy.Column("usage", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime)
)
