# encoding: utf-8
from __future__ import unicode_literals
from ..base import Node
from ..elements import String


def test_node_elements():

    class MyNode(Node):
        action_type = String()
        name = String()

    my = MyNode()

    assert my.action_type.label == 'actionType'
