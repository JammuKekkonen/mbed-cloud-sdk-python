# coding: utf-8

"""
    Connect CA API

    mbed Cloud Connect CA API allows services to get device credentials.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CredentialsResponseData(object):
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
        'certificate': 'str',
        'url': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'url': 'url'
    }

    def __init__(self, certificate=None, url=None):
        """
        CredentialsResponseData - a model defined in Swagger
        """

        self._certificate = certificate
        self._url = url
        self.discriminator = None

    @property
    def certificate(self):
        """
        Gets the certificate of this CredentialsResponseData.
        PEM format X.509 server certificate that will be used to validate the server certificate that will be received during the TLS/DTLS handshake.

        :return: The certificate of this CredentialsResponseData.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this CredentialsResponseData.
        PEM format X.509 server certificate that will be used to validate the server certificate that will be received during the TLS/DTLS handshake.

        :param certificate: The certificate of this CredentialsResponseData.
        :type: str
        """

        self._certificate = certificate

    @property
    def url(self):
        """
        Gets the url of this CredentialsResponseData.
        Server URI to which the client needs to connect to.

        :return: The url of this CredentialsResponseData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CredentialsResponseData.
        Server URI to which the client needs to connect to.

        :param url: The url of this CredentialsResponseData.
        :type: str
        """

        self._url = url

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
        if not isinstance(other, CredentialsResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
