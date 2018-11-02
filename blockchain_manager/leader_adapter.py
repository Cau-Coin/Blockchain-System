# -*- coding: utf-8 -*-
import requests
from flask import request

from blockchain_manager.block import create_block, block_to_json
from blockchain_manager.transaction import json_to_tx
from node_info import get_one_node


def receive_tx_msg(json_data):
    # http로 tx 받음
    tx = json_to_tx(json_data)
    return tx


def propose_block(last_block, tx_list, my_address):
    b = create_block(last_block, tx_list, my_address)
    block_json = block_to_json(b)

    # b를 http 전송
    dst = "http://0.0.0.0:4444/block_delivery"

    requests.post(url=dst, json=block_json)
    return b


def broadcast_next_leader():
    # http로 다음 리더 ip를 브로드캐스트
    dst = "http://0.0.0.0:4444/leader_delivery"
    next_leader = get_one_node()

    requests.post(url=dst, data=next_leader)
    return next_leader
