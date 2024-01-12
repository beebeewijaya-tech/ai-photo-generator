import requests

from db.conn import db
from models.sessions import sessions


class AuthManager:
    @staticmethod
    async def get_api_info():
        host = "https://ipinfo.io/"
        r = requests.get(host)
        r.raise_for_status()

        body = r.json()
        return body

    @staticmethod
    async def insert_session(data):
        query = sessions.insert().values(**data)
        last_record_id = await db.database.fetch_one(query)
        return last_record_id

    @staticmethod
    async def get_session(ip):
        query = sessions.select().where(sessions.c.ip_address == ip)
        return await db.database.fetch_one(query)

    @staticmethod
    async def update_session(data):
        query = "UPDATE sessions SET usage = :usage WHERE ip_address = :ip_address"

        return await db.database.execute(query, values=data)
