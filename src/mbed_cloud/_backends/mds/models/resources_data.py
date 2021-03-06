# coding: utf-8

"""
    Connect API

    Pelion Device Management Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. Device Management Connect allows connectivity to devices by queueing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ResourcesData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ct': 'str',
        '_if': 'str',
        'obs': 'bool',
        'path': 'str',
        'rt': 'str'
    }

    attribute_map = {
        'ct': 'ct',
        '_if': 'if',
        'obs': 'obs',
        'path': 'path',
        'rt': 'rt'
    }

    def __init__(self, ct=None, _if=None, obs=None, path=None, rt=None):
        """
        ResourcesData - a model defined in Swagger
        """

        self._ct = ct
        self.__if = _if
        self._obs = obs
        self._path = path
        self._rt = rt
        self.discriminator = None

    @property
    def ct(self):
        """
        Gets the ct of this ResourcesData.
        Content type.

        :return: The ct of this ResourcesData.
        :rtype: str
        """
        return self._ct

    @ct.setter
    def ct(self, ct):
        """
        Sets the ct of this ResourcesData.
        Content type.

        :param ct: The ct of this ResourcesData.
        :type: str
        """

        self._ct = ct

    @property
    def _if(self):
        """
        Gets the _if of this ResourcesData.
        Interface description that defines a name or URI that indicates how to interact with the target resource. It describes a generic interface type, such as a \"sensor\".

        :return: The _if of this ResourcesData.
        :rtype: str
        """
        return self.__if

    @_if.setter
    def _if(self, _if):
        """
        Sets the _if of this ResourcesData.
        Interface description that defines a name or URI that indicates how to interact with the target resource. It describes a generic interface type, such as a \"sensor\".

        :param _if: The _if of this ResourcesData.
        :type: str
        """

        self.__if = _if

    @property
    def obs(self):
        """
        Gets the obs of this ResourcesData.
        Whether the resource is observable or not (true/false).

        :return: The obs of this ResourcesData.
        :rtype: bool
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        """
        Sets the obs of this ResourcesData.
        Whether the resource is observable or not (true/false).

        :param obs: The obs of this ResourcesData.
        :type: bool
        """

        self._obs = obs

    @property
    def path(self):
        """
        Gets the path of this ResourcesData.
        Resource's URI path.

        :return: The path of this ResourcesData.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ResourcesData.
        Resource's URI path.

        :param path: The path of this ResourcesData.
        :type: str
        """

        self._path = path

    @property
    def rt(self):
        """
        Gets the rt of this ResourcesData.
        Application-specific resource type that describes this resource. [It is created by the client side application](/docs/current/connecting/resource-setup-in-mbed-cloud-client.html). Not meant to be a human-readable name for the resource. Multiple resource types may be included, they are separated by a space.

        :return: The rt of this ResourcesData.
        :rtype: str
        """
        return self._rt

    @rt.setter
    def rt(self, rt):
        """
        Sets the rt of this ResourcesData.
        Application-specific resource type that describes this resource. [It is created by the client side application](/docs/current/connecting/resource-setup-in-mbed-cloud-client.html). Not meant to be a human-readable name for the resource. Multiple resource types may be included, they are separated by a space.

        :param rt: The rt of this ResourcesData.
        :type: str
        """

        self._rt = rt

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
        if not isinstance(other, ResourcesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
