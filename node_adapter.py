import json
from flask import request, Flask
from block import Block, to_block
from transaction import Transaction, new_transaction
import requests

app = Flask(__name__)


def send_tx_msg(tx_json, ip):
    # http로 리더에게 tx 전송
    dst = "http://" + ip + ":4444" + "/transaction"
    requests.post(url=dst, json=tx_json)


@app.route("/block", methods=["POST", "GET"])
def accept_block():
    # http로 리더에게 block 받음
    if request.method == "POST":
        json_block = request.json
        block_data = json.dumps(json_block)

        block = to_block(block_data)

        return block

    else:
        print("[Error] Not defined request method!")


@app.route("/leader", methods=["POST", "GET"])
def receive_next_leader():
    # http로 새 리더 ip 받음
    if request.method == "POST":
        json_data = json.dumps(request.json)
        next_leader = json_data["leader"]
        return next_leader
    else:
        print("[Error] Not defined request method!")


@app.route("/input", methods=["POST", "GET"])
def receive_tx_request():
    if request.method == "POST":
        json_data = json.dumps(request.json)

        tx = new_transaction(json_data)

        return tx

    else:
        print("[Error] Not defined request method!")
