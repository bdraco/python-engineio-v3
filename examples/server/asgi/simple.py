import os
import uvicorn

import engineio_v3

eio = engineio_v3.AsyncServer(async_mode='asgi')
app = engineio_v3.ASGIApp(eio, static_files={
    '/': 'simple.html',
    '/static': 'static',
})


@eio.on('connect')
def connect(sid, environ):
    print("connect ", sid)


@eio.on('message')
async def message(sid, data):
    print('message from', sid, data)
    await eio.send(sid, 'Thank you for your message!', binary=False)


@eio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
