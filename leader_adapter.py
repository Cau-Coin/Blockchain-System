from block import *


def receive_tx_msg():
    # http로 tx 받음
    return


def propose_block(last_block, tx_list):
    b = new_block(last_block, tx_list)
    # b를 http 전송
    pass


def broadcast_next_leader():
    # http로 다음 리더 ip를 브로드캐스트
    pass
