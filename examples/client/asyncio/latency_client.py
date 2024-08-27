import asyncio
import time
import engineio_v3

loop = asyncio.get_event_loop()
eio = engineio_v3.AsyncClient()
start_timer = None


async def send_ping():
    global start_timer
    start_timer = time.time()
    await eio.send('ping')


@eio.on('connect')
async def on_connect():
    print('connected to server')
    await send_ping()


@eio.on('message')
async def on_message(data):
    global start_timer
    latency = time.time() - start_timer
    print('latency is {0:.2f} ms'.format(latency * 1000))
    await eio.sleep(1)
    await send_ping()


async def start_client():
    await eio.connect('http://localhost:5000')
    await eio.wait()


if __name__ == '__main__':
    loop.run_until_complete(start_client())
