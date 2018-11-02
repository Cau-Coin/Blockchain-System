# -*- coding: utf-8 -*-
from flask import Blueprint, request

from blockchain_manager.init_blockchain import bc
from blockchain_manager.leader_adapter import receive_tx_msg
from blockchain_manager.node_adapter import receive_tx_request, accept_block, receive_next_leader
from blockchain_manager.validate_service import *

http_handler = Blueprint('http_handler', __name__)

blockchain = bc


@http_handler.route("/input", methods=["POST"])
def handle_tx_request():
    r = "Handled tx request"

    if request.method == "POST":
        tx = receive_tx_request(bc.my_ip, request.json)
        if validate_tx(blockchain.state, tx):
            blockchain.save_transaction(tx)
        else:
            r = "[Error] Validating is failed!"
    else:
        r = "[Error] Not defined request method!"

    print(r)
    return r


@http_handler.route("/transaction", methods=["POST"])
def handle_tx():
    r = "Handled tx"

    # http로 tx 받음
    if request.method == "POST":
        tx = receive_tx_msg(request.json)
        blockchain.save_transaction(tx)
    else:
        r = "[Error] Not defined request method!"

    print(r)
    return r


@http_handler.route("/block", methods=["POST"])
def handle_proposed_block():
    r = "Handled proposed block"

    # http로 리더에게 block 받음
    if request.method == "POST":
        block = accept_block(request.json)
        blockchain.save_block(block)
    else:
        r = "[Error] Not defined request method!"

    print(r)
    return r


@http_handler.route("/leader", methods=["POST"])
def handle_leader_updated():
    r = "Handled leader updating"

    # http로 새 리더 ip 받음
    if request.method == "POST":
        leader = receive_next_leader(request.data)
        blockchain.update_leader(str(leader))
    else:
        r = "[Error] Not defined request method!"

    print(r)
    return r


@http_handler.route("/timeout", methods=["GET"])
def handle_timeout():
    blockchain.save_timeout_tx()
    return 'Handled timeout'


@http_handler.route("/read_data", methods=["POST"])
def handle_read_data():
    user_id = str(request.data.decode())
    if blockchain.read_data(user_id):
        return "True"

    return "False"
