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


class Scheduling(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, min=None, hour=None, active=None, dow=None):
        """
        Scheduling - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'min': 'int',
            'hour': 'int',
            'active': 'bool',
            'dow': 'list[int]'
        }

        self.attribute_map = {
            'min': 'min',
            'hour': 'hour',
            'active': 'active',
            'dow': 'dow'
        }

        self._min = min
        self._hour = hour
        self._active = active
        self._dow = dow

    @property
    def min(self):
        """
        Gets the min of this Scheduling.

        :return: The min of this Scheduling.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this Scheduling.

        :param min: The min of this Scheduling.
        :type: int
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")

        self._min = min

    @property
    def hour(self):
        """
        Gets the hour of this Scheduling.

        :return: The hour of this Scheduling.
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """
        Sets the hour of this Scheduling.

        :param hour: The hour of this Scheduling.
        :type: int
        """
        if hour is None:
            raise ValueError("Invalid value for `hour`, must not be `None`")

        self._hour = hour

    @property
    def active(self):
        """
        Gets the active of this Scheduling.

        :return: The active of this Scheduling.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Scheduling.

        :param active: The active of this Scheduling.
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")

        self._active = active

    @property
    def dow(self):
        """
        Gets the dow of this Scheduling.

        :return: The dow of this Scheduling.
        :rtype: list[int]
        """
        return self._dow

    @dow.setter
    def dow(self, dow):
        """
        Sets the dow of this Scheduling.

        :param dow: The dow of this Scheduling.
        :type: list[int]
        """

        self._dow = dow

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
        if not isinstance(other, Scheduling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
