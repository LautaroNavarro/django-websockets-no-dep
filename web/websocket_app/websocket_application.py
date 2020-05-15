import asyncio
from websocket_app.redis_cli import RedisCli


async def send_messages(pubsub, done, send):
    while not done:
        message = pubsub.get_message()
        if message:
            await send({
                'type': 'websocket.send',
                'text': "Event triggered",
            })
        else:
            await asyncio.sleep(0.2)


async def websocket_application(scope, receive, send):

    done = False
    while True:
        event = await receive()
        if event['type'] == 'websocket.connect':

            redis_cli = RedisCli.get()
            pubsub = redis_cli.pubsub()
            pubsub.psubscribe('__keyspace@0__:trigger_event')

            await send({
                'type': 'websocket.accept',
                'status_code': 101,
            })
            await send_messages(pubsub, done, send)

        if event['type'] == 'websocket.disconnect':
            print("Disconectin web socket")
            done = True
            break

        if event['type'] == 'websocket.receive':
            if event['text'] == 'ping':
                await send({
                    'type': 'websocket.send',
                    'text': 'pong!'
                })
