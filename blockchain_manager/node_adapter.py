# -*- coding: utf-8 -*-
import json
from flask import request, Blueprint
import requests

from blockchain_manager.transaction import tx_to_json, create_tx

node_adapter = Blueprint('node_adapter', __name__)


def send_tx_msg(tx, ip):
    # http로 리더에게 tx 전송
    dst = "http://" + ip + ":4444" + "/transaction"
    tx_json = tx_to_json(tx)
    requests.post(url=dst, json=tx_json)


def accept_block(block):
    return block


def receive_next_leader(leader_data):
    next_leader = leader_data.decode('utf-8')
    print("Update leader - ", next_leader)
    return next_leader


def receive_tx_request(my_ip, json_input):
    tx = create_tx(my_ip, json_input)
    return tx
