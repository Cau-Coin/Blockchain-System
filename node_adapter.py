import json
from flask import request, Blueprint
from block import to_block
from transaction import new_transaction
import requests

node_adapter = Blueprint('node_adapter', __name__)


def send_tx_msg(tx_json, ip):
    # http로 리더에게 tx 전송
    dst = "http://" + ip + ":4444" + "/transaction"
    requests.post(url=dst, json=tx_json)


@node_adapter.route("/block", methods=["POST"])
def accept_block():
    # http로 리더에게 block 받음
    if request.method == "POST":
        block = to_block(request.json)
        block_json = block.to_json()
        print(block_json)
        return block_json
    else:
        print("[Error] Not defined request method!")


@node_adapter.route("/leader", methods=["POST"])
def receive_next_leader():
    # http로 새 리더 ip 받음
    if request.method == "POST":
        next_leader = request.data.decode('utf-8')
        print(next_leader)
        return next_leader
    else:
        print("[Error] Not defined request method!")


@node_adapter.route("/input", methods=["POST"])
def receive_tx_request():
    if request.method == "POST":
        tx_data = request.json
        tx = new_transaction(tx_data)
        tx_json = tx.to_json()
        print(tx_json)
        return tx_json
    else:
        print("[Error] Not defined request method!")
