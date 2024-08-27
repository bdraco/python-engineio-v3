import time
import engineio_v3

eio = engineio_v3.Client()
start_timer = None


def send_ping():
    global start_timer
    start_timer = time.time()
    eio.send('ping')


@eio.on('connect')
def on_connect():
    print('connected to server')
    send_ping()


@eio.on('message')
def on_message(data):
    global start_timer
    latency = time.time() - start_timer
    print('latency is {0:.2f} ms'.format(latency * 1000))
    eio.sleep(1)
    send_ping()


if __name__ == '__main__':
    eio.connect('http://localhost:5000')
    eio.wait()
