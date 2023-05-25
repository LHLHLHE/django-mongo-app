import os

import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

MONGO_USERNAME = os.getenv('MONGO_USERNAME', default='mongo')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', default='mongo')
MONGO_CLUSTER = os.getenv('MONGO_CLUSTER', default='mongo')

mongo_uri = (
    f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}.x4ftjqx.'
    f'mongodb.net/?retryWrites=true&w=majority'
)
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
mongo_db = mongo_client['users_electronics']
