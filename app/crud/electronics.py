from crud.utils import mongo_db
from schemas.electronics import Electronic

electronics_collection = mongo_db.electronics


async def get(electronic_id: int | None = None):
    if not electronic_id:
        res = await electronics_collection.find({}, {'_id': 0}).to_list(1000)
    else:
        res = await electronics_collection.find_one(
            {'id': electronic_id},
            {'_id': 0}
        )

    return res


async def create(electronic: Electronic):
    try:
        await electronics_collection.insert_one(electronic.dict())
        return electronic.dict()
    except Exception as e:
        return e


async def delete(electronic_id: int):
    await electronics_collection.delete_one({'id': electronic_id})
