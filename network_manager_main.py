# -*- coding: utf-8 -*-
import threading
import time

from flask import Flask, request
import json
import requests

from blockchain_manager.init_blockchain import bc
from network_manager.db_manager import DataManager
from node_info import *

app = Flask(__name__)

ip_list = node_list
blockchain = bc

data_manager = DataManager('0.0.0.0', "caucoin_db", "blocks", "states", "coins")


@app.route("/write_transaction", methods=["POST"])
def receive_input():
    dst = "http://0.0.0.0:5303/input"
    data = request.json
    requests.post(url=dst, json=data)
    return "Write tx is delivered"


@app.route("/read_all_data", methods=["GET"])
def read_all_data():
    data = data_manager.get_all_data()
    return json.dumps(data)


@app.route("/read_one_data/<evaluate_id>", methods=["GET"])
def read_one_data(evaluate_id):
    data = data_manager.get_one_data(evaluate_id)
    return json.dumps(data)


@app.route("/read_one_data/<evaluate_id>/<user_id>", methods=["GET"])
def read_one_data_by_user(evaluate_id, user_id):
    dst = "http://0.0.0.0:5303/read_data"
    data = user_id
    res = requests.post(url=dst, data=data)
    result = res.content.decode()

    if result == "True":
        data = data_manager.get_one_data(evaluate_id)
    else:
        data = {"eval": "False"}

    return json.dumps(data)


@app.route("/tx_delivery", methods=["POST"])
def send_tx():
    dst = "http://" + blockchain.leader + ":4444/tx_receive"
    data = request.json
    requests.post(url=dst, json=data)
    return ""


@app.route("/tx_receive", methods=["POST"])
def receive_tx():
    dst = "http://0.0.0.0:5303/transaction"
    data = request.json
    requests.post(url=dst, json=data)
    return ""


@app.route("/block_delivery", methods=["POST"])
def broadcast_block():
    for node in node_list:
        dst = "http://" + node + ":4444/block_receive"
        data = request.json
        requests.post(url=dst, json=data)
    return "Broadcasting a block is finished"


@app.route("/block_receive", methods=["POST"])
def receive_block():
    dst = "http://0.0.0.0:5303/block"
    data = request.json
    requests.post(url=dst, json=data)
    return ""


@app.route("/leader_delivery", methods=["POST"])
def broadcast_leader():
    for node in node_list:
        dst = "http://" + node + ":4444/leader_receive"
        data = request.data
        requests.post(url=dst, data=data)
    return "Broadcasting new leader is finished"


@app.route("/leader_receive", methods=["POST"])
def receive_leader():
    dst = "http://0.0.0.0:5303/leader"
    data = request.data
    requests.post(url=dst, data=data)
    return ""


@app.route("/coin/<user_id>", methods=["GET"])
def read_coin_data(user_id):
    data = data_manager.get_coin_data(user_id)
    return json.dumps(data)


def send_time_out():
    for node in node_list:
        dst = "http://"+node+":5303/timeout"

        if node == my_ip:
            dst = "http://0.0.0.0:5303/timeout"

        requests.get(url=dst)


def timer_check():
    time.sleep(2)
    timer = threading.Timer(tx_limit_time, timer_check)
    send_time_out()
    timer.start()


if __name__ == '__main__':
    timer_check()
    app.run(host='0.0.0.0', port=4444)
