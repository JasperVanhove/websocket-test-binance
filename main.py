from datetime import datetime
import json
import logging

import websocket

socket = "wss://fstream.binance.com/ws/btcusdt@kline_1m"
interval = 10
ping_start = 0

#
# def _prepare_channel_data():
#     return {"method": "SUBSCRIBE", "params": ["BTCUSDT@kline_1m"]}


# def _get_ping_payload():
#     return json.dumps({'op': 'ping'})


def on_open(ws):
    print(f'Start: {datetime.now()}')

    # ws.send(_get_ping_payload())

    # channel_data = _prepare_channel_data()
    #
    # ws.send(json.dumps(channel_data))


def on_message(ws, message):
    global interval
    global ping_start

    message = json.loads(message)

    print(message)

    # if ping_start == interval:
    #     ws.send(json.dumps({'method': 'ping'}))
    # else:
    #     ping_start += 1


def _restart_websocket():
    wsn = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
    wsn.run_forever(ping_interval=interval)


def on_close(ws, test1, test2):
    print(f'End: {datetime.now()}')
    print('Restarting Websocket!')
    _restart_websocket()
    print(test1 + '\n---------------\n' + test2)


ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever(ping_interval=interval)
