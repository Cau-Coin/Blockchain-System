# -*- coding: utf-8 -*-
from flask import Blueprint, request

from blockchain_manager.init_blockchain import bc
from blockchain_manager.leader_adapter import receive_tx_msg
from blockchain_manager.node_adapter import receive_tx_request, accept_block, receive_next_leader
from blockchain_manager.validate_service import *

http_handler = Blueprint('http_handler', __name__)


@http_handler.route("/input", methods=["POST"])
def handle_tx_request():
    blockchain = bc

    if request.method == "POST":
        tx = receive_tx_request(bc.my_ip, request.json)
        if validate_tx(blockchain.state, tx):
            blockchain.save_transaction(tx)
        else:
            print("[Error] Validating is failed!")
    else:
        print("[Error] Not defined request method!")

    return 'Handled tx request'


@http_handler.route("/transaction", methods=["POST"])
def handle_tx():
    blockchain = bc

    # http로 tx 받음
    if request.method == "POST":
        tx = receive_tx_msg(request.json)
        blockchain.save_transaction(tx)
    else:
        print("[Error] Not defined request method!")

    return 'Handled tx'


@http_handler.route("/block", methods=["POST"])
def handle_proposed_block():
    blockchain = bc

    # http로 리더에게 block 받음
    if request.method == "POST":
        block = accept_block(request.json)
        blockchain.save_block(block)
    else:
        print("[Error] Not defined request method!")

    return 'Handled proposed block'


@http_handler.route("/leader", methods=["POST"])
def handle_leader_updated():
    blockchain = bc

    # http로 새 리더 ip 받음
    if request.method == "POST":
        leader = receive_next_leader(request.data)
        blockchain.update_leader(leader)
    else:
        print("[Error] Not defined request method!")

    return 'Handled leader updating'
