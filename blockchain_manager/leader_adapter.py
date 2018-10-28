import requests
from flask import request

from blockchain_manager.block import create_block, block_to_json
from blockchain_manager.transaction import json_to_tx


def receive_tx_msg(json_data):
    # http로 tx 받음
    tx = json_to_tx(json_data)
    print("Receive tx msg - ", tx)
    return tx


def propose_block(last_block, tx_list, my_address):
    b = create_block(last_block, tx_list, my_address)
    block_json = block_to_json(b)

    # b를 http 전송
    dst = "http://" + my_address + ":4444" + "/block"

    requests.post(url=dst, json=block_json)
    return b


def broadcast_next_leader(next_leader, my_address):
    # http로 다음 리더 ip를 브로드캐스트
    dst = "http://" + my_address + ":4444" + "/leader"

    requests.post(url=dst, data=next_leader)
