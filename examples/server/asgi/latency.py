import uvicorn

import engineio_v3

eio = engineio_v3.AsyncServer(async_mode='asgi')
app = engineio_v3.ASGIApp(eio, static_files={
    '/': 'latency.html',
    '/static': 'static',
})


@eio.on('message')
async def message(sid, data):
    await eio.send(sid, 'pong', binary=False)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
