import redis
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    pubsub = r.pubsub()
    pubsub.subscribe('test_channel')

    logger.info("Subscriber is listening...")

    for message in pubsub.listen():
        if message and message['type'] == 'message':
            logger.info(f"Received message: {message['data']}")


if __name__ == "__main__":
    main()
