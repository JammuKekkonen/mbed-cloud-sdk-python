# coding: utf-8

"""
    IAM Identities REST API

    REST API to manage accounts, groups, users and API keys

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class CACertificateResp(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account_id=None, service=None, created_at=None, object=None, subject=None, validity=None, etag=None, creation_time_millis=None, issuer=None, cert_data=None, id=None, name=None):
        """
        CACertificateResp - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_id': 'str',
            'service': 'str',
            'created_at': 'str',
            'object': 'str',
            'subject': 'str',
            'validity': 'str',
            'etag': 'str',
            'creation_time_millis': 'int',
            'issuer': 'str',
            'cert_data': 'str',
            'id': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'account_id': 'account_id',
            'service': 'service',
            'created_at': 'created_at',
            'object': 'object',
            'subject': 'subject',
            'validity': 'validity',
            'etag': 'etag',
            'creation_time_millis': 'creationTimeMillis',
            'issuer': 'issuer',
            'cert_data': 'cert_data',
            'id': 'id',
            'name': 'name'
        }

        self._account_id = account_id
        self._service = service
        self._created_at = created_at
        self._object = object
        self._subject = subject
        self._validity = validity
        self._etag = etag
        self._creation_time_millis = creation_time_millis
        self._issuer = issuer
        self._cert_data = cert_data
        self._id = id
        self._name = name

    @property
    def account_id(self):
        """
        Gets the account_id of this CACertificateResp.
        The UUID of the account.

        :return: The account_id of this CACertificateResp.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this CACertificateResp.
        The UUID of the account.

        :param account_id: The account_id of this CACertificateResp.
        :type: str
        """

        self._account_id = account_id

    @property
    def service(self):
        """
        Gets the service of this CACertificateResp.
        Service name where the certificate is to be used.

        :return: The service of this CACertificateResp.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this CACertificateResp.
        Service name where the certificate is to be used.

        :param service: The service of this CACertificateResp.
        :type: str
        """
        allowed_values = ["lwm2m", "bootstrap", "provisioning"]
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def created_at(self):
        """
        Gets the created_at of this CACertificateResp.
        Creation UTC time RFC3339.

        :return: The created_at of this CACertificateResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CACertificateResp.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this CACertificateResp.
        :type: str
        """

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this CACertificateResp.
        entity name: 'user', 'apikey', 'group', 'account' or error

        :return: The object of this CACertificateResp.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CACertificateResp.
        entity name: 'user', 'apikey', 'group', 'account' or error

        :param object: The object of this CACertificateResp.
        :type: str
        """
        allowed_values = ["user", "apikey", "group", "account", "account_template", "ca_cert", "list", "error"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def subject(self):
        """
        Gets the subject of this CACertificateResp.
        Subject of the certificate.

        :return: The subject of this CACertificateResp.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this CACertificateResp.
        Subject of the certificate.

        :param subject: The subject of this CACertificateResp.
        :type: str
        """

        self._subject = subject

    @property
    def validity(self):
        """
        Gets the validity of this CACertificateResp.
        Expiration time in UTC formatted as RFC3339.

        :return: The validity of this CACertificateResp.
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this CACertificateResp.
        Expiration time in UTC formatted as RFC3339.

        :param validity: The validity of this CACertificateResp.
        :type: str
        """

        self._validity = validity

    @property
    def etag(self):
        """
        Gets the etag of this CACertificateResp.
        API resource entity version.

        :return: The etag of this CACertificateResp.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this CACertificateResp.
        API resource entity version.

        :param etag: The etag of this CACertificateResp.
        :type: str
        """

        self._etag = etag

    @property
    def creation_time_millis(self):
        """
        Gets the creation_time_millis of this CACertificateResp.


        :return: The creation_time_millis of this CACertificateResp.
        :rtype: int
        """
        return self._creation_time_millis

    @creation_time_millis.setter
    def creation_time_millis(self, creation_time_millis):
        """
        Sets the creation_time_millis of this CACertificateResp.


        :param creation_time_millis: The creation_time_millis of this CACertificateResp.
        :type: int
        """

        self._creation_time_millis = creation_time_millis

    @property
    def issuer(self):
        """
        Gets the issuer of this CACertificateResp.
        Issuer of the certificate.

        :return: The issuer of this CACertificateResp.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this CACertificateResp.
        Issuer of the certificate.

        :param issuer: The issuer of this CACertificateResp.
        :type: str
        """

        self._issuer = issuer

    @property
    def cert_data(self):
        """
        Gets the cert_data of this CACertificateResp.
        X509.v3 CA certificate in PEM or base64 encoded DER format.

        :return: The cert_data of this CACertificateResp.
        :rtype: str
        """
        return self._cert_data

    @cert_data.setter
    def cert_data(self, cert_data):
        """
        Sets the cert_data of this CACertificateResp.
        X509.v3 CA certificate in PEM or base64 encoded DER format.

        :param cert_data: The cert_data of this CACertificateResp.
        :type: str
        """

        self._cert_data = cert_data

    @property
    def id(self):
        """
        Gets the id of this CACertificateResp.
        Entity ID.

        :return: The id of this CACertificateResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CACertificateResp.
        Entity ID.

        :param id: The id of this CACertificateResp.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CACertificateResp.
        Certificate name.

        :return: The name of this CACertificateResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CACertificateResp.
        Certificate name.

        :param name: The name of this CACertificateResp.
        :type: str
        """

        self._name = name

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
