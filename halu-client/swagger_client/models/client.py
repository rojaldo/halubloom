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


class Client(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, essid=None, passwd=None, bssid=None, channel=None, ip=None):
        """
        Client - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'essid': 'str',
            'passwd': 'str',
            'bssid': 'str',
            'channel': 'int',
            'ip': 'str'
        }

        self.attribute_map = {
            'essid': 'essid',
            'passwd': 'passwd',
            'bssid': 'bssid',
            'channel': 'channel',
            'ip': 'ip'
        }

        self._essid = essid
        self._passwd = passwd
        self._bssid = bssid
        self._channel = channel
        self._ip = ip

    @property
    def essid(self):
        """
        Gets the essid of this Client.

        :return: The essid of this Client.
        :rtype: str
        """
        return self._essid

    @essid.setter
    def essid(self, essid):
        """
        Sets the essid of this Client.

        :param essid: The essid of this Client.
        :type: str
        """
        if essid is None:
            raise ValueError("Invalid value for `essid`, must not be `None`")

        self._essid = essid

    @property
    def passwd(self):
        """
        Gets the passwd of this Client.

        :return: The passwd of this Client.
        :rtype: str
        """
        return self._passwd

    @passwd.setter
    def passwd(self, passwd):
        """
        Sets the passwd of this Client.

        :param passwd: The passwd of this Client.
        :type: str
        """
        if passwd is None:
            raise ValueError("Invalid value for `passwd`, must not be `None`")

        self._passwd = passwd

    @property
    def bssid(self):
        """
        Gets the bssid of this Client.

        :return: The bssid of this Client.
        :rtype: str
        """
        return self._bssid

    @bssid.setter
    def bssid(self, bssid):
        """
        Sets the bssid of this Client.

        :param bssid: The bssid of this Client.
        :type: str
        """
        if bssid is None:
            raise ValueError("Invalid value for `bssid`, must not be `None`")

        self._bssid = bssid

    @property
    def channel(self):
        """
        Gets the channel of this Client.

        :return: The channel of this Client.
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this Client.

        :param channel: The channel of this Client.
        :type: int
        """

        self._channel = channel

    @property
    def ip(self):
        """
        Gets the ip of this Client.

        :return: The ip of this Client.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this Client.

        :param ip: The ip of this Client.
        :type: str
        """

        self._ip = ip

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
        if not isinstance(other, Client):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
