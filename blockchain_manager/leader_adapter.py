# -*- coding: utf-8 -*-
import requests
from flask import request

from blockchain_manager.block import create_block, block_to_json
from blockchain_manager.transaction import json_to_tx
from node_list import *


def receive_tx_msg(json_data):
    # http로 tx 받음
    tx = json_to_tx(json_data)
    print("Receive tx msg - ", tx)
    return tx


def propose_block(last_block, tx_list, my_address):
    tx_limit_num = 3

    if len(tx_list) < 3:
        return None, 0

    b = create_block(last_block, tx_list[:tx_limit_num], my_address)
    block_json = block_to_json(b)

    # b를 http 전송
    dst = "http://0.0.0.0:4444/block"

    requests.post(url=dst, json=block_json)
    return b, tx_limit_num


def broadcast_next_leader():
    # http로 다음 리더 ip를 브로드캐스트
    dst = "http://0.0.0.0:4444/leader"
    next_leader = get_one_node()

    requests.post(url=dst, data=next_leader)
    return next_leader
