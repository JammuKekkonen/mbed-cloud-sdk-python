# coding: utf-8

"""
    Deployment Service API

    This is the API Documentation for the mbed deployment service which is part of the update service.

    OpenAPI spec version: 0.1
    
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


class UpdateCampaignPage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, has_more=None, total_count=None, object=None, limit=None, data=None, order=None):
        """
        UpdateCampaignPage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'has_more': 'bool',
            'total_count': 'int',
            'object': 'str',
            'limit': 'int',
            'data': 'list[UpdateCampaignSerializer]',
            'order': 'str'
        }

        self.attribute_map = {
            'has_more': 'has_more',
            'total_count': 'total_count',
            'object': 'object',
            'limit': 'limit',
            'data': 'data',
            'order': 'order'
        }

        self._has_more = has_more
        self._total_count = total_count
        self._object = object
        self._limit = limit
        self._data = data
        self._order = order

    @property
    def has_more(self):
        """
        Gets the has_more of this UpdateCampaignPage.
        Whether there are more results to display

        :return: The has_more of this UpdateCampaignPage.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this UpdateCampaignPage.
        Whether there are more results to display

        :param has_more: The has_more of this UpdateCampaignPage.
        :type: bool
        """

        self._has_more = has_more

    @property
    def total_count(self):
        """
        Gets the total_count of this UpdateCampaignPage.
        Total number of records

        :return: The total_count of this UpdateCampaignPage.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this UpdateCampaignPage.
        Total number of records

        :param total_count: The total_count of this UpdateCampaignPage.
        :type: int
        """

        self._total_count = total_count

    @property
    def object(self):
        """
        Gets the object of this UpdateCampaignPage.
        API Resource name

        :return: The object of this UpdateCampaignPage.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this UpdateCampaignPage.
        API Resource name

        :param object: The object of this UpdateCampaignPage.
        :type: str
        """

        self._object = object

    @property
    def limit(self):
        """
        Gets the limit of this UpdateCampaignPage.
        The number of results to return

        :return: The limit of this UpdateCampaignPage.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this UpdateCampaignPage.
        The number of results to return

        :param limit: The limit of this UpdateCampaignPage.
        :type: int
        """

        self._limit = limit

    @property
    def data(self):
        """
        Gets the data of this UpdateCampaignPage.


        :return: The data of this UpdateCampaignPage.
        :rtype: list[UpdateCampaignSerializer]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this UpdateCampaignPage.


        :param data: The data of this UpdateCampaignPage.
        :type: list[UpdateCampaignSerializer]
        """

        self._data = data

    @property
    def order(self):
        """
        Gets the order of this UpdateCampaignPage.
        Order of returned records

        :return: The order of this UpdateCampaignPage.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this UpdateCampaignPage.
        Order of returned records

        :param order: The order of this UpdateCampaignPage.
        :type: str
        """

        self._order = order

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
