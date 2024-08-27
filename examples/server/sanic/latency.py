from sanic import Sanic
from sanic.response import html

import engineio_v3

eio = engineio_v3.AsyncServer(async_mode='sanic')
app = Sanic()
eio.attach(app)


@app.route('/')
async def index(request):
    with open('latency.html') as f:
        return html(f.read())


@eio.on('message')
async def message(sid, data):
    await eio.send(sid, 'pong', binary=False)


app.static('/static', './static')


if __name__ == '__main__':
    app.run()
