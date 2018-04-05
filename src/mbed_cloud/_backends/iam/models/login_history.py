# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LoginHistory(object):
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
        'date': 'datetime',
        'ip_address': 'str',
        'success': 'bool',
        'user_agent': 'str'
    }

    attribute_map = {
        'date': 'date',
        'ip_address': 'ip_address',
        'success': 'success',
        'user_agent': 'user_agent'
    }

    def __init__(self, date=None, ip_address=None, success=None, user_agent=None):
        """
        LoginHistory - a model defined in Swagger
        """

        self._date = date
        self._ip_address = ip_address
        self._success = success
        self._user_agent = user_agent
        self.discriminator = None

    @property
    def date(self):
        """
        Gets the date of this LoginHistory.
        UTC time RFC3339 for this login attempt.

        :return: The date of this LoginHistory.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this LoginHistory.
        UTC time RFC3339 for this login attempt.

        :param date: The date of this LoginHistory.
        :type: datetime
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")

        self._date = date

    @property
    def ip_address(self):
        """
        Gets the ip_address of this LoginHistory.
        IP address of the client.

        :return: The ip_address of this LoginHistory.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this LoginHistory.
        IP address of the client.

        :param ip_address: The ip_address of this LoginHistory.
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")

        self._ip_address = ip_address

    @property
    def success(self):
        """
        Gets the success of this LoginHistory.
        Flag indicating whether login attempt was successful or not.

        :return: The success of this LoginHistory.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this LoginHistory.
        Flag indicating whether login attempt was successful or not.

        :param success: The success of this LoginHistory.
        :type: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")

        self._success = success

    @property
    def user_agent(self):
        """
        Gets the user_agent of this LoginHistory.
        User Agent header from the login request.

        :return: The user_agent of this LoginHistory.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this LoginHistory.
        User Agent header from the login request.

        :param user_agent: The user_agent of this LoginHistory.
        :type: str
        """
        if user_agent is None:
            raise ValueError("Invalid value for `user_agent`, must not be `None`")

        self._user_agent = user_agent

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
        if not isinstance(other, LoginHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
