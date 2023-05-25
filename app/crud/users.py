from crud.utils import mongo_db
from schemas.users import Customer, Employee

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
