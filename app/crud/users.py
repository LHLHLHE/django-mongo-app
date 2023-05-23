import os
from pprint import pprint

import motor.motor_asyncio
from dotenv import load_dotenv

from schemas.users import Customer, Employee

load_dotenv()

MONGO_USERNAME = os.getenv('MONGO_USERNAME', default='mongo')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', default='mongo')
MONGO_CLUSTER = os.getenv('MONGO_CLUSTER', default='mongo')

mongo_uri = (
    f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}.x4ftjqx.'
    f'mongodb.net/?retryWrites=true&w=majority'
)
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
mongo_db = mongo_client['users_cars']
users_collection = mongo_db.users


async def get(user_id: int | None = None):
    if not user_id:
        res = await users_collection.find({}, {'_id': 0}).to_list(1000)
    else:
        res = await users_collection.find_one({'id': user_id}, {'_id': 0})

    return res


async def create(user: Employee | Customer):
    try:
        await users_collection.insert_one(user.dict())
        return user.dict()
    except Exception as e:
        return e


async def delete(user_id: int):
    await users_collection.delete_one({'id': user_id})
