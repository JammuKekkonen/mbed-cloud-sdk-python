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


class AccountCreationReq(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address_line2=None, city=None, address_line1=None, display_name=None, country=None, company=None, state=None, contact=None, postal_code=None, admin_password=None, admin_name=None, parent_id=None, tier=None, admin_email=None, phone_number=None, email=None, aliases=None):
        """
        AccountCreationReq - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address_line2': 'str',
            'city': 'str',
            'address_line1': 'str',
            'display_name': 'str',
            'country': 'str',
            'company': 'str',
            'state': 'str',
            'contact': 'str',
            'postal_code': 'str',
            'admin_password': 'str',
            'admin_name': 'str',
            'parent_id': 'str',
            'tier': 'str',
            'admin_email': 'str',
            'phone_number': 'str',
            'email': 'str',
            'aliases': 'list[str]'
        }

        self.attribute_map = {
            'address_line2': 'address_line2',
            'city': 'city',
            'address_line1': 'address_line1',
            'display_name': 'display_name',
            'country': 'country',
            'company': 'company',
            'state': 'state',
            'contact': 'contact',
            'postal_code': 'postal_code',
            'admin_password': 'admin_password',
            'admin_name': 'admin_name',
            'parent_id': 'parentID',
            'tier': 'tier',
            'admin_email': 'admin_email',
            'phone_number': 'phone_number',
            'email': 'email',
            'aliases': 'aliases'
        }

        self._address_line2 = address_line2
        self._city = city
        self._address_line1 = address_line1
        self._display_name = display_name
        self._country = country
        self._company = company
        self._state = state
        self._contact = contact
        self._postal_code = postal_code
        self._admin_password = admin_password
        self._admin_name = admin_name
        self._parent_id = parent_id
        self._tier = tier
        self._admin_email = admin_email
        self._phone_number = phone_number
        self._email = email
        self._aliases = aliases

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this AccountCreationReq.
        Postal address line 2.

        :return: The address_line2 of this AccountCreationReq.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this AccountCreationReq.
        Postal address line 2.

        :param address_line2: The address_line2 of this AccountCreationReq.
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """
        Gets the city of this AccountCreationReq.
        The city part of the postal address.

        :return: The city of this AccountCreationReq.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AccountCreationReq.
        The city part of the postal address.

        :param city: The city of this AccountCreationReq.
        :type: str
        """

        self._city = city

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this AccountCreationReq.
        Postal address line 1.

        :return: The address_line1 of this AccountCreationReq.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this AccountCreationReq.
        Postal address line 1.

        :param address_line1: The address_line1 of this AccountCreationReq.
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def display_name(self):
        """
        Gets the display_name of this AccountCreationReq.
        The display name for the account.

        :return: The display_name of this AccountCreationReq.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AccountCreationReq.
        The display name for the account.

        :param display_name: The display_name of this AccountCreationReq.
        :type: str
        """

        self._display_name = display_name

    @property
    def country(self):
        """
        Gets the country of this AccountCreationReq.
        The country part of the postal address.

        :return: The country of this AccountCreationReq.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this AccountCreationReq.
        The country part of the postal address.

        :param country: The country of this AccountCreationReq.
        :type: str
        """

        self._country = country

    @property
    def company(self):
        """
        Gets the company of this AccountCreationReq.
        The name of the company.

        :return: The company of this AccountCreationReq.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this AccountCreationReq.
        The name of the company.

        :param company: The company of this AccountCreationReq.
        :type: str
        """

        self._company = company

    @property
    def state(self):
        """
        Gets the state of this AccountCreationReq.
        The state part of the postal address.

        :return: The state of this AccountCreationReq.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AccountCreationReq.
        The state part of the postal address.

        :param state: The state of this AccountCreationReq.
        :type: str
        """

        self._state = state

    @property
    def contact(self):
        """
        Gets the contact of this AccountCreationReq.
        The name of the contact person for this account.

        :return: The contact of this AccountCreationReq.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this AccountCreationReq.
        The name of the contact person for this account.

        :param contact: The contact of this AccountCreationReq.
        :type: str
        """

        self._contact = contact

    @property
    def postal_code(self):
        """
        Gets the postal_code of this AccountCreationReq.
        The postal code part of the postal address.

        :return: The postal_code of this AccountCreationReq.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this AccountCreationReq.
        The postal code part of the postal address.

        :param postal_code: The postal_code of this AccountCreationReq.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def admin_password(self):
        """
        Gets the admin_password of this AccountCreationReq.
        The password when creating a new user. It will be generated when not present in the request.

        :return: The admin_password of this AccountCreationReq.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this AccountCreationReq.
        The password when creating a new user. It will be generated when not present in the request.

        :param admin_password: The admin_password of this AccountCreationReq.
        :type: str
        """

        self._admin_password = admin_password

    @property
    def admin_name(self):
        """
        Gets the admin_name of this AccountCreationReq.
        The username of the admin user to be created, containing alphanumerical letters and -,._@+= characters.

        :return: The admin_name of this AccountCreationReq.
        :rtype: str
        """
        return self._admin_name

    @admin_name.setter
    def admin_name(self, admin_name):
        """
        Sets the admin_name of this AccountCreationReq.
        The username of the admin user to be created, containing alphanumerical letters and -,._@+= characters.

        :param admin_name: The admin_name of this AccountCreationReq.
        :type: str
        """
        if admin_name is None:
            raise ValueError("Invalid value for `admin_name`, must not be `None`")

        self._admin_name = admin_name

    @property
    def parent_id(self):
        """
        Gets the parent_id of this AccountCreationReq.
        The ID of the parent account, if it has any.

        :return: The parent_id of this AccountCreationReq.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this AccountCreationReq.
        The ID of the parent account, if it has any.

        :param parent_id: The parent_id of this AccountCreationReq.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def tier(self):
        """
        Gets the tier of this AccountCreationReq.
        The tier level of the account; '0': free tier, '1': commercial account. Other values are reserved for the future.

        :return: The tier of this AccountCreationReq.
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """
        Sets the tier of this AccountCreationReq.
        The tier level of the account; '0': free tier, '1': commercial account. Other values are reserved for the future.

        :param tier: The tier of this AccountCreationReq.
        :type: str
        """

        self._tier = tier

    @property
    def admin_email(self):
        """
        Gets the admin_email of this AccountCreationReq.
        The email address of the account admin.

        :return: The admin_email of this AccountCreationReq.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this AccountCreationReq.
        The email address of the account admin.

        :param admin_email: The admin_email of this AccountCreationReq.
        :type: str
        """
        if admin_email is None:
            raise ValueError("Invalid value for `admin_email`, must not be `None`")

        self._admin_email = admin_email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this AccountCreationReq.
        The phone number of the company.

        :return: The phone_number of this AccountCreationReq.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this AccountCreationReq.
        The phone number of the company.

        :param phone_number: The phone_number of this AccountCreationReq.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def email(self):
        """
        Gets the email of this AccountCreationReq.
        The company email address for this account.

        :return: The email of this AccountCreationReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AccountCreationReq.
        The company email address for this account.

        :param email: The email of this AccountCreationReq.
        :type: str
        """

        self._email = email

    @property
    def aliases(self):
        """
        Gets the aliases of this AccountCreationReq.
        An array of aliases.

        :return: The aliases of this AccountCreationReq.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this AccountCreationReq.
        An array of aliases.

        :param aliases: The aliases of this AccountCreationReq.
        :type: list[str]
        """

        self._aliases = aliases

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
        if not isinstance(other, AccountCreationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
