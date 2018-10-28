# -*- coding: utf-8 -*-
import random

node_list = ["115.68.207.11"]


def get_one_node():
    one_node = random.choice(node_list)
    print(one_node)
    return random.choice(one_node)