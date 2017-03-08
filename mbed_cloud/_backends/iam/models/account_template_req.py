# coding: utf-8

"""
    IAM Identities REST API

    REST API to manage accounts, groups, users and API keys

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AccountTemplateReq(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, parent=None, name=None, limits=None, template_type=None, reason=None, resources=None, description=None):
        """
        AccountTemplateReq - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'parent': 'str',
            'name': 'str',
            'limits': 'dict(str, str)',
            'template_type': 'str',
            'reason': 'str',
            'resources': 'list[Policy]',
            'description': 'str'
        }

        self.attribute_map = {
            'parent': 'parent',
            'name': 'name',
            'limits': 'limits',
            'template_type': 'template_type',
            'reason': 'reason',
            'resources': 'resources',
            'description': 'description'
        }

        self._parent = parent
        self._name = name
        self._limits = limits
        self._template_type = template_type
        self._reason = reason
        self._resources = resources
        self._description = description

    @property
    def parent(self):
        """
        Gets the parent of this AccountTemplateReq.
        ID of the parent template, can be null.

        :return: The parent of this AccountTemplateReq.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this AccountTemplateReq.
        ID of the parent template, can be null.

        :param parent: The parent of this AccountTemplateReq.
        :type: str
        """

        self._parent = parent

    @property
    def name(self):
        """
        Gets the name of this AccountTemplateReq.
        Account template name.

        :return: The name of this AccountTemplateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AccountTemplateReq.
        Account template name.

        :param name: The name of this AccountTemplateReq.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def limits(self):
        """
        Gets the limits of this AccountTemplateReq.
        List of limits as name-value pairs.

        :return: The limits of this AccountTemplateReq.
        :rtype: dict(str, str)
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """
        Sets the limits of this AccountTemplateReq.
        List of limits as name-value pairs.

        :param limits: The limits of this AccountTemplateReq.
        :type: dict(str, str)
        """

        self._limits = limits

    @property
    def template_type(self):
        """
        Gets the template_type of this AccountTemplateReq.
        Account template type.

        :return: The template_type of this AccountTemplateReq.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """
        Sets the template_type of this AccountTemplateReq.
        Account template type.

        :param template_type: The template_type of this AccountTemplateReq.
        :type: str
        """

        self._template_type = template_type

    @property
    def reason(self):
        """
        Gets the reason of this AccountTemplateReq.
        Account template update reason.

        :return: The reason of this AccountTemplateReq.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this AccountTemplateReq.
        Account template update reason.

        :param reason: The reason of this AccountTemplateReq.
        :type: str
        """

        self._reason = reason

    @property
    def resources(self):
        """
        Gets the resources of this AccountTemplateReq.
        List of resource-action-allow triplets, policies.

        :return: The resources of this AccountTemplateReq.
        :rtype: list[Policy]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this AccountTemplateReq.
        List of resource-action-allow triplets, policies.

        :param resources: The resources of this AccountTemplateReq.
        :type: list[Policy]
        """

        self._resources = resources

    @property
    def description(self):
        """
        Gets the description of this AccountTemplateReq.
        Account template description.

        :return: The description of this AccountTemplateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AccountTemplateReq.
        Account template description.

        :param description: The description of this AccountTemplateReq.
        :type: str
        """

        self._description = description

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
        if not isinstance(other, AccountTemplateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
