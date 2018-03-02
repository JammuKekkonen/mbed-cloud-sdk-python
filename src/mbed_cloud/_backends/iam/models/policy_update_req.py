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


class PolicyUpdateReq(object):
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
        'status': 'str',
        'valid_until': 'datetime',
        'grant_expires_in': 'int',
        'name': 'str',
        'error_message': 'str',
        'not_resources': 'list[str]',
        'actions': 'dict(str, bool)',
        'not_conditions': 'list[str]',
        'valid_from': 'datetime',
        'users': 'list[str]',
        'groups': 'list[str]',
        'tag': 'str',
        'not_actions': 'list[str]',
        'apikeys': 'list[str]',
        'conditions': 'list[str]',
        'resources': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'status': 'status',
        'valid_until': 'valid_until',
        'grant_expires_in': 'grant_expires_in',
        'name': 'name',
        'error_message': 'error_message',
        'not_resources': 'not_resources',
        'actions': 'actions',
        'not_conditions': 'not_conditions',
        'valid_from': 'valid_from',
        'users': 'users',
        'groups': 'groups',
        'tag': 'tag',
        'not_actions': 'notActions',
        'apikeys': 'apikeys',
        'conditions': 'conditions',
        'resources': 'resources',
        'description': 'description'
    }

    def __init__(self, status=None, valid_until=None, grant_expires_in=None, name=None, error_message=None, not_resources=None, actions=None, not_conditions=None, valid_from=None, users=None, groups=None, tag=None, not_actions=None, apikeys=None, conditions=None, resources=None, description=None):
        """
        PolicyUpdateReq - a model defined in Swagger
        """

        self._status = status
        self._valid_until = valid_until
        self._grant_expires_in = grant_expires_in
        self._name = name
        self._error_message = error_message
        self._not_resources = not_resources
        self._actions = actions
        self._not_conditions = not_conditions
        self._valid_from = valid_from
        self._users = users
        self._groups = groups
        self._tag = tag
        self._not_actions = not_actions
        self._apikeys = apikeys
        self._conditions = conditions
        self._resources = resources
        self._description = description
        self.discriminator = None

    @property
    def status(self):
        """
        Gets the status of this PolicyUpdateReq.
        The new status of this policy.

        :return: The status of this PolicyUpdateReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PolicyUpdateReq.
        The new status of this policy.

        :param status: The status of this PolicyUpdateReq.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def valid_until(self):
        """
        Gets the valid_until of this PolicyUpdateReq.
        Specifies the date and time until the policy is valid in UTC time RFC3339. E.g. '2018-02-05T09:43:44Z'

        :return: The valid_until of this PolicyUpdateReq.
        :rtype: datetime
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """
        Sets the valid_until of this PolicyUpdateReq.
        Specifies the date and time until the policy is valid in UTC time RFC3339. E.g. '2018-02-05T09:43:44Z'

        :param valid_until: The valid_until of this PolicyUpdateReq.
        :type: datetime
        """

        self._valid_until = valid_until

    @property
    def grant_expires_in(self):
        """
        Gets the grant_expires_in of this PolicyUpdateReq.
        Specifies the value in seconds for how long an authorization result is valid.

        :return: The grant_expires_in of this PolicyUpdateReq.
        :rtype: int
        """
        return self._grant_expires_in

    @grant_expires_in.setter
    def grant_expires_in(self, grant_expires_in):
        """
        Sets the grant_expires_in of this PolicyUpdateReq.
        Specifies the value in seconds for how long an authorization result is valid.

        :param grant_expires_in: The grant_expires_in of this PolicyUpdateReq.
        :type: int
        """

        self._grant_expires_in = grant_expires_in

    @property
    def name(self):
        """
        Gets the name of this PolicyUpdateReq.
        The new name of this policy, must be unique and not longer than 100 character.

        :return: The name of this PolicyUpdateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyUpdateReq.
        The new name of this policy, must be unique and not longer than 100 character.

        :param name: The name of this PolicyUpdateReq.
        :type: str
        """

        self._name = name

    @property
    def error_message(self):
        """
        Gets the error_message of this PolicyUpdateReq.
        Custom error message returned when this policy matches with not allowed result.

        :return: The error_message of this PolicyUpdateReq.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this PolicyUpdateReq.
        Custom error message returned when this policy matches with not allowed result.

        :param error_message: The error_message of this PolicyUpdateReq.
        :type: str
        """

        self._error_message = error_message

    @property
    def not_resources(self):
        """
        Gets the not_resources of this PolicyUpdateReq.
        New list of not_resources in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. Previous list will be overwritten.

        :return: The not_resources of this PolicyUpdateReq.
        :rtype: list[str]
        """
        return self._not_resources

    @not_resources.setter
    def not_resources(self, not_resources):
        """
        Sets the not_resources of this PolicyUpdateReq.
        New list of not_resources in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. Previous list will be overwritten.

        :param not_resources: The not_resources of this PolicyUpdateReq.
        :type: list[str]
        """

        self._not_resources = not_resources

    @property
    def actions(self):
        """
        Gets the actions of this PolicyUpdateReq.
        New list of actions as key-pairs of '{action}': 'true' or 'false', not more than 100. For enabling all actions use { '*': true }. Previous list will be overwritten.

        :return: The actions of this PolicyUpdateReq.
        :rtype: dict(str, bool)
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this PolicyUpdateReq.
        New list of actions as key-pairs of '{action}': 'true' or 'false', not more than 100. For enabling all actions use { '*': true }. Previous list will be overwritten.

        :param actions: The actions of this PolicyUpdateReq.
        :type: dict(str, bool)
        """

        self._actions = actions

    @property
    def not_conditions(self):
        """
        Gets the not_conditions of this PolicyUpdateReq.
        New list of not_conditions in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. Previous list will be overwritten.

        :return: The not_conditions of this PolicyUpdateReq.
        :rtype: list[str]
        """
        return self._not_conditions

    @not_conditions.setter
    def not_conditions(self, not_conditions):
        """
        Sets the not_conditions of this PolicyUpdateReq.
        New list of not_conditions in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. Previous list will be overwritten.

        :param not_conditions: The not_conditions of this PolicyUpdateReq.
        :type: list[str]
        """

        self._not_conditions = not_conditions

    @property
    def valid_from(self):
        """
        Gets the valid_from of this PolicyUpdateReq.
        Specifies the date and time when the policy will become valid in UTC time RFC3339. E.g. '2018-02-05T09:43:44Z'

        :return: The valid_from of this PolicyUpdateReq.
        :rtype: datetime
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """
        Sets the valid_from of this PolicyUpdateReq.
        Specifies the date and time when the policy will become valid in UTC time RFC3339. E.g. '2018-02-05T09:43:44Z'

        :param valid_from: The valid_from of this PolicyUpdateReq.
        :type: datetime
        """

        self._valid_from = valid_from

    @property
    def users(self):
        """
        Gets the users of this PolicyUpdateReq.
        New list of user IDs this policy is attached to, not more than 100. Previous list will be overwritten.

        :return: The users of this PolicyUpdateReq.
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this PolicyUpdateReq.
        New list of user IDs this policy is attached to, not more than 100. Previous list will be overwritten.

        :param users: The users of this PolicyUpdateReq.
        :type: list[str]
        """

        self._users = users

    @property
    def groups(self):
        """
        Gets the groups of this PolicyUpdateReq.
        New list of group IDs this policy is attached to, not more than 100. Previous list will be overwritten.

        :return: The groups of this PolicyUpdateReq.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this PolicyUpdateReq.
        New list of group IDs this policy is attached to, not more than 100. Previous list will be overwritten.

        :param groups: The groups of this PolicyUpdateReq.
        :type: list[str]
        """

        self._groups = groups

    @property
    def tag(self):
        """
        Gets the tag of this PolicyUpdateReq.
        New policy tag that can be used for various purposes to be able to distinguish between policies. Not longer than 100 characters.

        :return: The tag of this PolicyUpdateReq.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this PolicyUpdateReq.
        New policy tag that can be used for various purposes to be able to distinguish between policies. Not longer than 100 characters.

        :param tag: The tag of this PolicyUpdateReq.
        :type: str
        """

        self._tag = tag

    @property
    def not_actions(self):
        """
        Gets the not_actions of this PolicyUpdateReq.
        New list of not_actions, not more than 100. Previous list will be overwritten.

        :return: The not_actions of this PolicyUpdateReq.
        :rtype: list[str]
        """
        return self._not_actions

    @not_actions.setter
    def not_actions(self, not_actions):
        """
        Sets the not_actions of this PolicyUpdateReq.
        New list of not_actions, not more than 100. Previous list will be overwritten.

        :param not_actions: The not_actions of this PolicyUpdateReq.
        :type: list[str]
        """

        self._not_actions = not_actions

    @property
    def apikeys(self):
        """
        Gets the apikeys of this PolicyUpdateReq.
        New list of API key IDs this policy is attached to, not more than 100. Previous list will be overwritten.

        :return: The apikeys of this PolicyUpdateReq.
        :rtype: list[str]
        """
        return self._apikeys

    @apikeys.setter
    def apikeys(self, apikeys):
        """
        Sets the apikeys of this PolicyUpdateReq.
        New list of API key IDs this policy is attached to, not more than 100. Previous list will be overwritten.

        :param apikeys: The apikeys of this PolicyUpdateReq.
        :type: list[str]
        """

        self._apikeys = apikeys

    @property
    def conditions(self):
        """
        Gets the conditions of this PolicyUpdateReq.
        New list of conditions in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. Previous list will be overwritten.

        :return: The conditions of this PolicyUpdateReq.
        :rtype: list[str]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this PolicyUpdateReq.
        New list of conditions in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. Previous list will be overwritten.

        :param conditions: The conditions of this PolicyUpdateReq.
        :type: list[str]
        """

        self._conditions = conditions

    @property
    def resources(self):
        """
        Gets the resources of this PolicyUpdateReq.
        New list of resources in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. Previous list will be overwritten.

        :return: The resources of this PolicyUpdateReq.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this PolicyUpdateReq.
        New list of resources in urn:mbed-cloud:{resource-type}:{resource-name} format, not more than 100. Previous list will be overwritten.

        :param resources: The resources of this PolicyUpdateReq.
        :type: list[str]
        """

        self._resources = resources

    @property
    def description(self):
        """
        Gets the description of this PolicyUpdateReq.
        The new description of this policy, not longer than 500 character.

        :return: The description of this PolicyUpdateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PolicyUpdateReq.
        The new description of this policy, not longer than 500 character.

        :param description: The description of this PolicyUpdateReq.
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
        if not isinstance(other, PolicyUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other