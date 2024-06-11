# from fastapi import FastAPI, Request
# import redis
# import logging
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# app = FastAPI()
#
# # Connect to Redis
# r = redis.Redis(host='redis-server', port=6379, decode_responses=True)
#
# @app.post("/publish")
# async def publish_message(request: Request):
#     body = await request.json()
#     message = body.get("message")
#     if message:
#         r.publish('my_channel', message)
#         logger.info(f"Published message: {message}")
#         return {"status": "Message published"}
#     else:
#         logger.warning("No message provided")
#         return {"status": "No message provided"}, 400
from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()

# Connect to Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)

class Message(BaseModel):
    message: str

@app.post("/publish")
async def publish_message(message: Message):
    r.publish('test_channel', message.message)
    return {"status": "Message published"}
