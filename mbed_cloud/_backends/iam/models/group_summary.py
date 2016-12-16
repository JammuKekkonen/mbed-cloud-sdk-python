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


class GroupSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, last_update_time=None, api_key_count=None, created_at=None, object=None, creation_time=None, etag=None, creation_time_millis=None, id=None, user_count=None):
        """
        GroupSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'last_update_time': 'int',
            'api_key_count': 'int',
            'created_at': 'str',
            'object': 'str',
            'creation_time': 'int',
            'etag': 'str',
            'creation_time_millis': 'int',
            'id': 'str',
            'user_count': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'last_update_time': 'lastUpdateTime',
            'api_key_count': 'apiKeyCount',
            'created_at': 'created_at',
            'object': 'object',
            'creation_time': 'creationTime',
            'etag': 'etag',
            'creation_time_millis': 'creationTimeMillis',
            'id': 'id',
            'user_count': 'userCount'
        }

        self._name = name
        self._last_update_time = last_update_time
        self._api_key_count = api_key_count
        self._created_at = created_at
        self._object = object
        self._creation_time = creation_time
        self._etag = etag
        self._creation_time_millis = creation_time_millis
        self._id = id
        self._user_count = user_count

    @property
    def name(self):
        """
        Gets the name of this GroupSummary.
        The name of the group.

        :return: The name of this GroupSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupSummary.
        The name of the group.

        :param name: The name of this GroupSummary.
        :type: str
        """

        self._name = name

    @property
    def last_update_time(self):
        """
        Gets the last_update_time of this GroupSummary.
        A timestamp of the latest group update, in milliseconds.

        :return: The last_update_time of this GroupSummary.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """
        Sets the last_update_time of this GroupSummary.
        A timestamp of the latest group update, in milliseconds.

        :param last_update_time: The last_update_time of this GroupSummary.
        :type: int
        """

        self._last_update_time = last_update_time

    @property
    def api_key_count(self):
        """
        Gets the api_key_count of this GroupSummary.
        The number of API keys in this group.

        :return: The api_key_count of this GroupSummary.
        :rtype: int
        """
        return self._api_key_count

    @api_key_count.setter
    def api_key_count(self, api_key_count):
        """
        Sets the api_key_count of this GroupSummary.
        The number of API keys in this group.

        :param api_key_count: The api_key_count of this GroupSummary.
        :type: int
        """

        self._api_key_count = api_key_count

    @property
    def created_at(self):
        """
        Gets the created_at of this GroupSummary.
        Creation UTC time RFC3339.

        :return: The created_at of this GroupSummary.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this GroupSummary.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this GroupSummary.
        :type: str
        """

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this GroupSummary.
        Entity name: always 'group'

        :return: The object of this GroupSummary.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this GroupSummary.
        Entity name: always 'group'

        :param object: The object of this GroupSummary.
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
    def creation_time(self):
        """
        Gets the creation_time of this GroupSummary.
        A timestamp of the group creation in the storage, in milliseconds.

        :return: The creation_time of this GroupSummary.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this GroupSummary.
        A timestamp of the group creation in the storage, in milliseconds.

        :param creation_time: The creation_time of this GroupSummary.
        :type: int
        """

        self._creation_time = creation_time

    @property
    def etag(self):
        """
        Gets the etag of this GroupSummary.
        API resource entity version.

        :return: The etag of this GroupSummary.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this GroupSummary.
        API resource entity version.

        :param etag: The etag of this GroupSummary.
        :type: str
        """

        self._etag = etag

    @property
    def creation_time_millis(self):
        """
        Gets the creation_time_millis of this GroupSummary.


        :return: The creation_time_millis of this GroupSummary.
        :rtype: int
        """
        return self._creation_time_millis

    @creation_time_millis.setter
    def creation_time_millis(self, creation_time_millis):
        """
        Sets the creation_time_millis of this GroupSummary.


        :param creation_time_millis: The creation_time_millis of this GroupSummary.
        :type: int
        """

        self._creation_time_millis = creation_time_millis

    @property
    def id(self):
        """
        Gets the id of this GroupSummary.
        The UUID of the group.

        :return: The id of this GroupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GroupSummary.
        The UUID of the group.

        :param id: The id of this GroupSummary.
        :type: str
        """

        self._id = id

    @property
    def user_count(self):
        """
        Gets the user_count of this GroupSummary.
        The number of users in this group.

        :return: The user_count of this GroupSummary.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this GroupSummary.
        The number of users in this group.

        :param user_count: The user_count of this GroupSummary.
        :type: int
        """

        self._user_count = user_count

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
