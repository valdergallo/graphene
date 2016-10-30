# encoding: utf-8
from __future__ import unicode_literals
import json
import traceback
import sys
import six
import re


class GrapheneObject(object):
    __slot__ = ('label', 'value', 'description', 'output')

    def __init__(self, label=None, value=None):
        self.value = value
        if not label:
            (filename, line_number, function_name, text)=traceback.extract_stack()[-2]
            label = text[:text.find('=')].strip()
        self.__dict__['label'] = self.to_camel(label)

    def __setattr__(self, attr, value):
        if attr not in self.__slot__:
            raise AttributeError('Invalid attribute ({})'.format(attr))
        if value is not None:
            try:
                self.__dict__[attr] = self.validate(value)
            except:
                print "Validation error for {}:".format(attr)
                print '-' * 60
                traceback.print_exc(file=sys.stdout)
                print '-' * 60

        self.__dict__[attr] = value

    def to_camel(self, value):
        components = str(value).split('_')
        # We capitalize the first letter of each component except the first one
        # with the 'title' method and join them together.
        return components[0] + "".join(x.title() for x in components[1:])

    def validate(self, value):
        return value

    def to_json(self):
        return json.dumps(self.__dict__)


class String(GrapheneObject):

    def validate(self, value):
        print 'validate '
        return str(value)


class Int(GrapheneObject):

    def validate(self, value):
        return int(value)


class Float(GrapheneObject):

    def validate(self, value):
        return float(value)


class List(GrapheneObject):

    def validate(self, value):
        return list(value)


class Field(GrapheneObject):

    def validate(self, value):
        if not isinstance(value, GrapheQLElement):
            raise ValueError('Elements must be one valid GraphQL.Element')
        return value
