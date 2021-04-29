import motor.motor_asyncio

# setup the database
async def setup():
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
        db = client.projects
    except Exception as e:
        print(e)
    return db