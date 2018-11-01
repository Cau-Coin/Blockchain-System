# -*- coding: utf-8 -*-
import random

node_list = ["115.68.207.101", "115.68.232.77", "115.68.232.78"]

leader = "115.68.207.101"
my_ip = "115.68.207.101"

tx_limit_num = 5
tx_limit_time = 15


def get_one_node():
    one_node = random.choice(node_list)
    return one_node
