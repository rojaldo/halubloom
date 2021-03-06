# coding: utf-8

"""
    Halu API

    This should be a basic guide for the new Halu API. It will be updated as soon as I add new messages (or i'll try). The IP address to communicate with the master lamp is 10.0.0.1 by default.

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Discovery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=1, action=None):
        """
        Discovery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'action': 'list[Discovery]'
        }

        self.attribute_map = {
            'id': 'id',
            'action': 'action'
        }

        self._id = id
        self._action = action

    @property
    def id(self):
        """
        Gets the id of this Discovery.

        :return: The id of this Discovery.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Discovery.

        :param id: The id of this Discovery.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def action(self):
        """
        Gets the action of this Discovery.

        :return: The action of this Discovery.
        :rtype: list[Discovery]
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Discovery.

        :param action: The action of this Discovery.
        :type: list[Discovery]
        """

        self._action = action

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Discovery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
