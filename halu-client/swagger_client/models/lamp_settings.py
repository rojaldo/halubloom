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


class LampSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, default_color=None, position=None, reset_color=None, button_enable=None):
        """
        LampSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'default_color': 'Color',
            'position': 'Position',
            'reset_color': 'Color',
            'button_enable': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'default_color': 'default_color',
            'position': 'position',
            'reset_color': 'reset_color',
            'button_enable': 'button_enable'
        }

        self._name = name
        self._default_color = default_color
        self._position = position
        self._reset_color = reset_color
        self._button_enable = button_enable

    @property
    def name(self):
        """
        Gets the name of this LampSettings.

        :return: The name of this LampSettings.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LampSettings.

        :param name: The name of this LampSettings.
        :type: str
        """

        self._name = name

    @property
    def default_color(self):
        """
        Gets the default_color of this LampSettings.

        :return: The default_color of this LampSettings.
        :rtype: Color
        """
        return self._default_color

    @default_color.setter
    def default_color(self, default_color):
        """
        Sets the default_color of this LampSettings.

        :param default_color: The default_color of this LampSettings.
        :type: Color
        """

        self._default_color = default_color

    @property
    def position(self):
        """
        Gets the position of this LampSettings.

        :return: The position of this LampSettings.
        :rtype: Position
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this LampSettings.

        :param position: The position of this LampSettings.
        :type: Position
        """

        self._position = position

    @property
    def reset_color(self):
        """
        Gets the reset_color of this LampSettings.

        :return: The reset_color of this LampSettings.
        :rtype: Color
        """
        return self._reset_color

    @reset_color.setter
    def reset_color(self, reset_color):
        """
        Sets the reset_color of this LampSettings.

        :param reset_color: The reset_color of this LampSettings.
        :type: Color
        """

        self._reset_color = reset_color

    @property
    def button_enable(self):
        """
        Gets the button_enable of this LampSettings.

        :return: The button_enable of this LampSettings.
        :rtype: bool
        """
        return self._button_enable

    @button_enable.setter
    def button_enable(self, button_enable):
        """
        Sets the button_enable of this LampSettings.

        :param button_enable: The button_enable of this LampSettings.
        :type: bool
        """

        self._button_enable = button_enable

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
        if not isinstance(other, LampSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
