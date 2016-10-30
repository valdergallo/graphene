# encoding: utf-8
from __future__ import unicode_literals
import six


class GraphQL(object):
    def __init__(self, *kwarg):
        self.__TYPE__ = None

    def __repr__(self):
        return 'GraphQL Type({0}) {1}'.format(self.__TYPE__, self.__class__.__name__)

    def to_grapheql(self):
        return "{}"


class Node(GraphQL):
    __TYPE__ = 'node'


class Query(GraphQL):
    __TYPE__ = 'query'


class Mutation(GraphQL):
    __TYPE__ = 'mutation'
