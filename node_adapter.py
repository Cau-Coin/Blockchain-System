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


def accept_block(json_data):
    block = to_block(json_data)
    print(block)
    return block


def receive_next_leader(leader_data):
    next_leader = leader_data.decode('utf-8')
    print(next_leader)
    return next_leader


def receive_tx_request(json_data):
    tx = new_transaction(json_data)
    print(tx)
    return tx
