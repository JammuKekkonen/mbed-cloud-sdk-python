# coding: utf-8

"""
    Third party CA management API

    API for managing third party CA for creating certificates on Pelion Device Management

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CertificateIssuerVerifyResponse(object):
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
        'message': 'str',
        'successful': 'bool'
    }

    attribute_map = {
        'message': 'message',
        'successful': 'successful'
    }

    def __init__(self, message=None, successful=None):
        """
        CertificateIssuerVerifyResponse - a model defined in Swagger
        """

        self._message = message
        self._successful = successful
        self.discriminator = None

    @property
    def message(self):
        """
        Gets the message of this CertificateIssuerVerifyResponse.
        Provides details in case of failure. 

        :return: The message of this CertificateIssuerVerifyResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CertificateIssuerVerifyResponse.
        Provides details in case of failure. 

        :param message: The message of this CertificateIssuerVerifyResponse.
        :type: str
        """

        self._message = message

    @property
    def successful(self):
        """
        Gets the successful of this CertificateIssuerVerifyResponse.
        Indicates whether the certificate issuer was verified successfully. 

        :return: The successful of this CertificateIssuerVerifyResponse.
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """
        Sets the successful of this CertificateIssuerVerifyResponse.
        Indicates whether the certificate issuer was verified successfully. 

        :param successful: The successful of this CertificateIssuerVerifyResponse.
        :type: bool
        """

        self._successful = successful

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
        if not isinstance(other, CertificateIssuerVerifyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
